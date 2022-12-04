#!/usr/bin/python3

"""
    Select states from a database
"""

import sys.argv as argv
import MySQLdb as mysqldb


def select(username, password, dbname):
    """
    Make a connection and perform tge select
    """
    try:
        db = mysqldb.connect(host='localhost', user=username,
                             passwd=password, port=3306)
        cur = db.cursor()
        cur.execute('SELECT * FROM states ORDERED BY states.id ASC')
        return cur.fetchall()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    if argv.len >= 3:
        for i in select(argv[1], argv[2], argv[3]):
            print(i)
