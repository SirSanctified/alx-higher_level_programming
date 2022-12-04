#!/usr/bin/python3

"""
    Select states from a database
"""

from sys import argv
import MySQLdb as mysqldb


def select(username, password, dbname):
    """
    Make a connection and perform tge select
    """
    try:
        db = mysqldb.connect(host='localhost', user=username,
                             passwd=password, port=3306)
        cur = db.cursor()
        cur.execute('SELECT id, name FROM states WHERE name LIKE "N%" ORDER BY id ASC')
        rows = cur.fetchall()
        for row in rows:
            if row[1][0] == 'N':
                print(row)
        cur.close()
        db.close()
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    if len(argv) == 3:
        select(argv[1], argv[2], argv[3])
