#!/usr/bin/env python3

# Create a new database called cars
# that has a table inventory

# I'm gonna use a functional approach this time

import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

def main(): create_inventory()

def create_inventory():
    ''' This function creates a table in
        the cars database called inventory '''
    query = """CREATE TABLE IF NOT EXISTS cars
            (Make TEXT, Model TEXT, Quantity INT)"""
    cursor.execute(query)

if __name__ == "__main__": main()

# close the cursor and connection
cursor.close()
conn.close()
