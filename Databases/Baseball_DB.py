import sqlite3

conn = sqlite3.connect('BaseballDB.sqlite')

cur = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS Players (
    playerID    INTEGER PRIMARY KEY      NOT NULL,
    batOrder    INTEGER                  NOT NULL,
    firstName   TEXT                     NOT NULL,
    lastName    TEXT                     NOT NULL,
    position    TEXT                     NOT NULL,
    atBats      INTEGER                  NULL,
    hits        INTEGER                  NULL
    );"""
cur.execute(query)
