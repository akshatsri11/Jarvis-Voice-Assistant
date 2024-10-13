import sqlite3

conn = sqlite3.connect("jarvis.db") 
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id INTEGER PRIMARY KEY, name VARCHAR(255), path VARCHAR(1000))"
cursor.execute(query)