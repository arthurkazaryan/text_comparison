from database.main import con, cur, table_name
import numpy as np


def add_company(company_name: str, company_encoded_array: np.ndarray):

    cur.execute(f"INSERT INTO {table_name}(name, encoded) VALUES (?, ?)", (company_name, company_encoded_array))
    con.commit()


def get_companies():

    companies_data = cur.execute(f"SELECT name, encoded FROM {table_name} ORDER BY timestamp DESC").fetchall()

    return companies_data
