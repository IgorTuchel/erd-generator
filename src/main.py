import sys
import os
from create import make_erd

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <database_name.db>")
        sys.exit(1)
    
    db = sys.argv[1]
    if not os.path.exists(db):
        print(f"Error: Cannot find database file: {db}")
        sys.exit(1)

    try:
        print(make_erd(db))
    except Exception as e:
        print(f"** ERROR: {e}")

if __name__ == "__main__":
    main()