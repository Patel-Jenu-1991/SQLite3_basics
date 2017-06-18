#!/usr/bin/env python3

# Ouput only records that are for Ford vehicles

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # retrieve all Ford vehicles
    cursor.execute("SELECT * FROM inventory WHERE Make = 'Ford'")
    rows = cursor.fetchall()
    print()
    print("-" * 91)
    print("{:-^91}".format(" INVENTORY "))
    print("-" * 91)
    print("-" * 91)
    print("\t| {: ^20} | {: ^20} | {: ^20} |".format(
        "Make", "Model", "Quantity")
    )
    print("-" * 91)
    for row in rows:
        print("\n\t| {: ^20} | {: ^20} | {: ^20} |".format(
            row[0], row[1], row[2])
        )
    print()
    print("-" * 91)
    print("-" * 91)
    print()
