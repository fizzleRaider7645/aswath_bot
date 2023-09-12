import sqlite3
def create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stocks (date text, trans text, symbol text, qty real, price real)')
    conn.commit()
    conn.close()
