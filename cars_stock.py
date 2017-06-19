#!/usr/bin/env python3

# Output the car's make and model on one line
# The quantity on another line
# The order count on the next line

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # retrieve data
    cursor.execute(""" SELECT * FROM inventory """)

    # fetchall retrieves all records from the query
    rows = cursor.fetchall()

    # output the rows to the screen, row by row
    for row in rows:
        # output the car make, model and quantity ot screen
        print(f"{row[0]} {row[1]} \n{row[2]}")

        # retrieve order_date for the current car make and model
        cursor.execute("""SELECT count(order_date) FROM orders WHERE
                        make = ? and model = ?""", (row[0], row[1]))

        # fetchone() retrieves one record from the query
        order_count = cursor.fetchone()[0]

        # output the order count to the screen
        print(order_count)
        print()
