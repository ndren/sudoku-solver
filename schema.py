import sqlite3
conn = sqlite3.connect("times.db")
conn.execute("CREATE TABLE times (sudoku TEXT PRIMARY KEY, time INTEGER)")
