import sqlite3
from extract_sqlite_db import extract_tables
from plantuml import create_uml
from client import make_request
import sys

def make_erd(path):
    con, cursor = connection(path)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cursor.fetchall()
    tbl_arr = extract_tables(cursor,tables)
    uml = create_uml(tbl_arr)
    info = make_request(uml)
    con.close()
    return info

def connection(path):
    try:
        con = sqlite3.connect(path)
        cursor = con.cursor()
        return con, cursor
    except Exception as e:
        print(f"Error occured when connecting to database: {e}")
        sys.exit(1)