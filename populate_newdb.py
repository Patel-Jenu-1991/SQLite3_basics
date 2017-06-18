#!/usr/bin/env python3

# We're gonna add more records to our new.db
# using the executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    # insert multiple records using a tuple
    cities = [
        ('Boston', 'MA', 600000),
        ('Los Angeles', 'CA', 38000000),
        ('Houston', 'TX', 2100000),
        ('Philadelphia', 'PA', 15000000),
        ('San Antonio', 'TX', 140000000),
        ('San Diego', 'CA', 130000),
        ('Dallas', 'TX', 1200000),
        ('San Jose', 'CA', 9000000),
        ('Jacksonville', 'FL', 8000000),
        ('Indianapolis', 'IN', 8000000),
        ('Austin', 'TX', 8000000),
        ('Detroit', 'MI', 700000)
    ]

    cursor.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)

    cursor.execute("SELECT * FROM population WHERE population > 1000000")

    rows = cursor.fetchall()

    for row in rows:
        print(row[0], row[1], row[2])
