import streamlit as st
import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
import os
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords
import tensorflow as tf
from dotenv import load_dotenv

load_dotenv()
lemmatizer = WordNetLemmatizer()

MODEL_PATH = "models/final.h5"
VECTORIZER_PATH = "models/vectorizer.pkl"
#ANN MODEL
model = tf.keras.models.load_model(MODEL_PATH)

#Vectorizer
with open(VECTORIZER_PATH,"rb") as file:
    vectorizer = pickle.load(file)

st.title("Welcome to Feedback Prediction System")

data = st.file_uploader("Please Upload a file",type="csv")
if data is not None:
    df = pd.read_csv(data)
    col_name = df.columns[0]
    df.rename(columns={col_name:"message"},inplace=True)
    df = df.astype(str).fillna("")
    if df.empty:
        print("df is empty")
    corpus = []
    for i in range(len(df)):
        review = re.sub("[^a-zA-Z]"," ",df["message"][i])
        review = review.lower()
        review = review.split()
        review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words("english"))]
        review = " ".join(review)
        corpus.append(review)
    #y = pd.DataFrame(corpus)
    y_transform = vectorizer.transform(corpus)
    values = []
    for i in range(y_transform.shape[0]):
        y_probs = model.predict(y_transform[i].toarray().reshape(-1,50000))
        y_pred_class = np.argmax(y_probs,axis=1)
        if y_pred_class == 0:
            values.append("negative")
        elif y_pred_class == 1:
            values.append("neutral")
        else:
            values.append("positive")
    final_df = pd.DataFrame({"message":corpus,"output":values})
    st.download_button(label="Download CSV", data=final_df.to_csv(index=False), file_name="predictions.csv", mime="text/csv")

if st.button("Reset"):
    st.rerun()



    
    
