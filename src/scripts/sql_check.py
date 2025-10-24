import os, pyodbc
from dotenv import load_dotenv

load_dotenv()

conn_str = os.getenv('SQL_CONN_RO')
if not conn_str:
    raise SystemExit('Missing env var: SQL_CONN_RO')

with pyodbc.connect(conn_str, timeout=15) as conn:
    cur = conn.cursor()
    cur.execute('SELECT TOP (5) * FROM dbo.ticketsales;')
    rows = cur.fetchall()
    print('Rows returned:', len(rows))
