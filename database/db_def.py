import sqlite3

def CreateDB(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PLC_1 (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TIMESTAMP TEXT,
        TEMPERATURE REAL,
        PRESSURE REAL)
    """)
    conn.commit()
    conn.close()

def InsertDB(path, timestamp, temperature, pressure):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO PLC_1
        (TIMESTAMP, TEMPERATURE, PRESSURE)
        VALUES (?, ?, ?)
    """, (timestamp, temperature, pressure))
    conn.commit()
    conn.close()

def ResetDB(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM PLC_1
    """)
    conn.commit()
    conn.close()