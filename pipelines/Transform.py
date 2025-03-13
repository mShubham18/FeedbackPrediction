from pipelines.Extract import Extract
import os
from dotenv import load_dotenv
from typing import List
load_dotenv()
DB_PATH = os.getenv("DB_PATH")
df = Extract(DB_PATH)
def Transform(DB_PATH):
    X = df[]
    y= df["output"]
