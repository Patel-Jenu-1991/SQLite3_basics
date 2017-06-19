#!/usr/bin/env python3

# Calculate the total number of orders
# for each make and model using COUNT()

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # crate a dictionary of sql queries
    sql = {
        'Focus' : "SELECT count(Make) FROM orders WHERE model = 'Focus'",
        'Explorer' : "SELECT count(Make) FROM orders WHERE model = 'Explorer'",
        'Taurus' : "SELECT count(Make) FROM orders WHERE model = 'Taurus'",
        'Pilot' : "SELECT count(Make) FROM orders WHERE model = 'Pilot'",
        'CR-V' : "SELECT count(Make) FROM orders WHERE model = 'CR-V'"
    }

    # run each sql query item in the dictionary
    for keys, values in sql.items():
        # run sql
        cursor.execute(values)

        # fetchone retrieves one record from the query
        result = cursor.fetchone()

        # output the result to screen
        print(f"\n{keys}:", result[0])
