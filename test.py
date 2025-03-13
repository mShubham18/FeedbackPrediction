import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
DB_PATH = os.getenv("DB_PATH")
conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM Corpus")
print(cursor.fetchall())
conn.close()