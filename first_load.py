import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
CSV_PATH = os.getenv("CSV_PATH")
conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

## creating a table if does not exists
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Corpus(
    id INTEGER PRIMARY KEY AUTOINCREMENT, Feedback TEXT,Output INTEGER)
    """
)

df = pd.read_csv(CSV_PATH,encoding="latin1")

for i in range(len(df)):
    output = int(df["output"][i])
    feedback = df["message"][i]
    cursor.execute("""INSERT INTO Corpus(Feedback,Output)
                   VALUES(?,?)""",(feedback,output))

conn.commit()
print(cursor.fetchall())
conn.close()