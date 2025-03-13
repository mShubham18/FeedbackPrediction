import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
import tensorflow as tf
model = tf.keras.models.load_model("models/final.h5")
if model:
    print("success")
else:
    print('Failure')