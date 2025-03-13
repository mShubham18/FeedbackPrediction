import streamlit as st
import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
import os
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords
from tensorflow as tf
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
model = tf.keras.models.load_model(MODEL_PATH)

st.title("Welcome to Feedback Prediction System")

data = st.file_uploader("Please Upload a file",type="csv")
if data is not None:
    df = pd.read_csv(data)
    df.rename({df.columns[0]:"message"},inplace=True)
corpus = []
for i in range(len(df)):
    review = re.sub("^a-zA-Z"," ",df["message"][i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopwords.words("english"))]
    review = " ".join(review)
    corpus.append(review)



    
    
