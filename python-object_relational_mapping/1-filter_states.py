"""
List all states starting with 'N' from a MySQL database.

Usage:
    ./1-filter_states.py <user> <password> <database>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    "Retrive command argument"
    username = sys.argv[1]
    passeword = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=passeword,
        db=db_name
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    )
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
