import sqlite3

def save_to_db(df, table_name="fintechs_vagas", db_path="database/data.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
