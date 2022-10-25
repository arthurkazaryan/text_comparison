from settings import MODEL_SELECTION
import numpy as np
import sqlite3
import io


def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())


def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)


sqlite3.register_adapter(np.ndarray, adapt_array)
sqlite3.register_converter("array", convert_array)


table_name = f'company_names_{MODEL_SELECTION}'
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute(f"""CREATE TABLE IF NOT EXISTS 
                {table_name}(name TEXT, encoded ARRAY, timestamp DATE DEFAULT (datetime('now','localtime')))""")
