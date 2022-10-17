import sqlite3

table_name = 'company_names'
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute(f"""CREATE TABLE IF NOT EXISTS 
                {table_name}(name TEXT, timestamp DATE DEFAULT (datetime('now','localtime')))""")
