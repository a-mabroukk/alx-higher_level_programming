#!/usr/bin/python3
"""import myfrom MySQLdb module"""

import MySQLdb
from sys import argv
if __name__ == '__main__':
    """we a connect method to create a connection to database(MySQL server)"""
    ll = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    """Here, we perform a query, so we call cursor method and
    then execute queries on it"""
    c = ll.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    """Now we store results in a variable to desiplay it"""
    results = c.fetchall()
    for r in results:
        print(r)
        """Finally, we close a cursor"""
    c.close()
