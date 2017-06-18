#!/usr/bin/env python3

# Update the inventory table
# change the quantity of two records

import sqlite3

with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # Update the quantity of Focus
    qry = "UPDATE inventory SET Quantity = 400000 WHERE Model = 'Focus'"
    cursor.execute(qry)

    # Update teh quantity of CR-V
    qry = "UPDATE inventory SET Quantity = 900000 WHERE Model = 'CR-V'"
    cursor.execute(qry)

    # Output all of the records from the table
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    print("\n{:-^91}".format(" INVENTORY "))
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
