#!/usr/bin/env python3

# Output the car's make and model on one line
# the quantity on another line, and then the
# order_dates on subsequent lines below that

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # retrieve data
    cursor.execute(""" SELECT inventory.Make, inventory.Model,
                inventory.Quantity, orders.order_date
                FROM inventory INNER JOIN orders
                ON inventory.Model = orders.model """)

    rows = cursor.fetchall()

    for row in rows:
        print("Make: {} | Model: {}".format(row[0], row[1]))
        print("Quantity:", row[2])
        print("Order Date:", row[3])
        print()
