#!/usr/bin/env python3

# Populating the inventory table in our car database

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # create a tuple of data
    # (Make, Model, Quantity)
    car_data = [
        ("Ford", "Focus", 200000),
        ("Ford", "Explorer", 500000),
        ("Ford", "Taurus", 700000),
        ("Honda", "Pilot", 800000),
        ("Honda", "CR-V", 400000)
    ]

    # insert data into table
    cursor.executemany("INSERT INTO inventory VALUES(?, ?, ?)", car_data)
