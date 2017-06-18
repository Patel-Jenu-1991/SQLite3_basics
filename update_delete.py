#!/usr/bin/env python3

# UPDATE and DELETE statements

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # update data
    qry = """UPDATE population SET population = 9000000
    WHERE city = 'New York City'"""
    c.execute(qry)

    # delete data
    c.execute("DELETE FROM population WHERE city = 'Boston'")

    print("\nNEW DATA:\n")

    c.execute("SELECT * FROM population")

    rows = c.fetchall()

    for row in rows:
        print(row[0], row[1], row[2])
