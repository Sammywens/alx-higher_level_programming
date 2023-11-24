#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    # Check if all three command-line arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(argv[0]))
        exit(1)

    # Extract command-line arguments
    username, password, database_name = argv[1:4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", user=username, port=3306,
                         passwd=password, db=database_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
