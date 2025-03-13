import sqlite3
import pandas as pd

def Extract(DB_PATH):
    """
    Returns the formed dataframe after extraction
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT Feedback, Output FROM Corpus")
    data = cursor.fetchall()
    message, output = zip(*data)
    df = pd.DataFrame({"Message":message,"output":output})
    return df
