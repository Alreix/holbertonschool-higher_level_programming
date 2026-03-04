#!/usr/bin/python3
"""
Display states where the name matches the user input.

Usage:
    ./2-my_filter_states.py <user> <password> <database> <state_name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )
    cur = db.cursor()

    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    ).format(state_name_searched)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
