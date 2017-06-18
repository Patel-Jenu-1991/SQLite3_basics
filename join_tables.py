#!/usr/bin/env python3

# JOINing data from multiple tables - cleanup

import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    # retrieve data
    cursor.execute(""" SELECT population.city, population.population,
                    regions.region FROM population, regions WHERE
                    population.city = regions.city ORDER by
                    population.city ASC""")

    rows = cursor.fetchall()

    for row in rows:
        print("City:", row[0])
        print("population:", row[1])
        print("region:", row[2])
        print()
