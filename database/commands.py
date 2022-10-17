from database.main import con, cur, table_name


def add_company(company_name: str):
    cur.execute(f"INSERT INTO {table_name}(name) VALUES (?)", (company_name,))
    con.commit()


def get_companies():
    companies_data = cur.execute(f"SELECT name FROM {table_name} ORDER BY timestamp DESC").fetchall()
    return [company[0] for company in companies_data]


print(get_companies())
