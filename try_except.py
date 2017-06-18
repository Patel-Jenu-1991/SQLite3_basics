#!/usr/bin/env python3

# INSERT command with Error Handler

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    query = "INSERT INTO population VALUES('New Orleans', 'LA', 7000000)"
    cursor.execute("INSERT INTO population VALUES('Austin', 'TX', 9000000)")
    cursor.execute(query)

    # commit the changes
    conn.commit()
    print("Data inserted successfully!!")
except sqlite3.OperationalError as e:
    print("\nOops! Something went wrong. Try again...")
    print("\nThe following Error has occured:")
    print(f"\n\t{e}\n")
