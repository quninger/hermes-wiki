import sqlite3
conn = sqlite3.connect(r'C:\Users\54367\.hermes\state.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
for t in tables:
    print('Table:', t[0])
    cursor.execute(f'SELECT * FROM "{t[0]}"')
    rows = cursor.fetchall()
    for r in rows[:50]:
        print(' ', r)
conn.close()
