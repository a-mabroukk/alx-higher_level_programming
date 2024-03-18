#!/usr/bin/python3
"""import myfrom MySQLdb module"""

import MySQLdb
from sys import argv
if __name__ == '__main__':
    """we a connect method to create a connection to database(MySQL server)"""
    sql_connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                     password=argv[2], db=argv[3])
    """Here, we perform a query, so we call cursor method and
    then execute queries on it"""
    c = sql_connection.cursor()
    state_name = argv[4]
    c.execute("SELECT cities.name FROM cities INNER\
             JOIN states ON cities.state_id = states.id WHERE\
             states.name = %s ORDER BY cities.id ASC", (state_name, ))
    """Now we store results in a variable to desiplay it"""
    results = c.fetchall()
    for r in range(len(results)):
        print(results[r][0], end=", ")
    print("")
    """Finally, we close a cursor"""
    c.close()
    sql_connection.close()
