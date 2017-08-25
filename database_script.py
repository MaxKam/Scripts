# Script for creating and updating a PostgreSQL DB
import psycopg2

connection_string = "dbname='testdb' user='test' password='test' host='localhost' port='5432'"

def create_table():
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity, item):
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=? WHERE item=?", (quantity, item))
    conn.commit()
    conn.close()
    
