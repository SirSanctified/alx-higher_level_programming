#!/usr/bin/python3

"""
    lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def select():
    """
        connect to a MySQL server running on localhost at port 3306
    """
    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cur = db.cursor()
        search = sys.argv[4]
        cur.execute("""SELECT cities.name FROM
                        cities JOIN states on cities.state_id = states.id
                        WHERE states.name = %s""", (search,)
                    )
        rows = cur.fetchall()

        for row in rows:
            if row != rows[-1]:
                print(row[0], end=', ')
            else:
                print(row[0])

        cur.close()
        db.close()
    except Exception as er:
        print(str(er))


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        select()
