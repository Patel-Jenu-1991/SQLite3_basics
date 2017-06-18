#!/usr/bin/env python3

# Search/Retrieve data from a database

# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # execute the SELECT query
    c.execute("SELECT firstname, lastname FROM employees")

    # use a for loop to iterate through the database,
    # printing the results line by line

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for row in rows:
        print(row[0], row[1])
