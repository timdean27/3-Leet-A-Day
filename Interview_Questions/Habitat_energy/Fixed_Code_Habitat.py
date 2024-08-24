#!/usr/bin/python2

# This code sums the squares of all numbers between start_number and end_number,
# Added to any numbers in the optional argument initial_series,
# Then writes that number out to a file.
# It also stores the inputs and outputs to a database, which has been separately set up.

# e.g. sum(2, 4, [7, 9]) = 4 + 9 + 7 + 9 = 29

import psycopg2

database_connection_string = 'dbname=postgres user=postgres password=changeme host=localhost'


def create_table():
    """
    Before you do this, bring up a database with:
        docker run -p 5432:5432 -e POSTGRES_PASSWORD=changeme -d postgres
    """
    conn = psycopg2.connect('dbname=postgres user=postgres password=changeme host=localhost')
    cur = conn.cursor()
    cur.execute("CREATE TABLE answers (answer_id SERIAL PRIMARY KEY, input VARCHAR(255), output REAL)")
    conn.commit()


def sum(database_details, start_number, end_number, initial_series=[]):

    conn = psycopg2.connect(database_details)
    cur = conn.cursor()
    log = file('output.txt', 'w')

    for number in range(start_number, end_number):
        square = number * number
        initial_series.append(square)

    sum = 0
    for number in initial_series:
        sum = sum + number

    cur.execute("INSERT INTO answers (input, output) "
                 "VALUES (%s, %s)"
                 %(
                     "'" + str(start_number) + ',' + str(end_number) + ',' + str(initial_series) + "'",
                     sum
                   )
                 )

    log.write("%s" % sum)


# Now test
sum(database_connection_string, 2, 4, [7, 9])
