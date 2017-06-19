#!/usr/bin/env python3

# Assignment 3a - insert random data

# import the sqlite3 library
import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database table if exists
    c.execute("DROP TABLE IF EXISTS numbers")

    # create database table
    c.execute("CREATE TABLE numbers(num INT)")

    # insert each number to the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100),))
