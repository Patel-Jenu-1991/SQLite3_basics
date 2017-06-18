#!/usr/bin/env python3

# Add another table orders to accompany your car.db

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders
                (make TEXT, model TEXT, order_date DATE)""")

    # insert multiple records using a tuple

    orders = [
        ("Ford", "Focus", "2016-01-16"),
        ("Ford", "Focus", "2017-03-19"),
        ("Ford", "Focus", "2017-01-16"),
        ("Ford", "Explorer", "2017-02-01"),
        ("Ford", "Explorer", "2017-03-12"),
        ("Ford", "Explorer", "2017-05-17"),
        ("Ford", "Taurus", "2017-06-25"),
        ("Ford", "Taurus", "2017-02-14"),
        ("Ford", "Taurus", "2017-05-27"),
        ("Honda", "Pilot", "2017-03-18"),
        ("Honda", "Pilot", "2017-08-22"),
        ("Honda", "Pilot", "2017-09-25"),
        ("Honda", "CR-V", "2017-11-16"),
        ("Honda", "CR-V", "2017-12-16"),
        ("Honda", "CR-V", "2017-10-24")
    ]

    cursor.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)

    cursor.execute("SELECT * FROM orders ORDER by order_date ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2])
