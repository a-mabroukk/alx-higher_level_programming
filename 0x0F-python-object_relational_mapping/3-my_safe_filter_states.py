#!/usr/bin/python3
"""import myfrom MySQLdb module"""

import MySQLdb
from sys import argv
if __name__ == '__main__':
    """we a connect method to create a connection to database(MySQL server)"""
    ll = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])
    """Here, we perform a query, so we call cursor method and
    then execute queries on it but before that we pre-compile the SQL statement
    structure on the server side to prevent malicious code injection attempts
    within the query itself"""
    sql = """SELECT * FROM states WHERE name = %s ORDER BY id ASC"""
    c = ll.cursor()
    searched_name = argv[4]
    c.execute((sql), (searched_name,))
    """Now we store results in a variable to desiplay it"""
    results = c.fetchall()
    for r in results:
        print(r)
        """Finally, we close a cursor"""
    c.close()
