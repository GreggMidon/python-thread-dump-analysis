'''
Name....: .py
Date....:
Author..: Gregg Midon
Desc....:
Usage...:

Version History:
---------------


Example Records...


'''
import cx_Oracle

def main():

    s = "41y2xuzbskxk7"

    sqlstr = "select get_sql_text('{}') from dual".format(s)
    #print(s)

    dbcon = cx_Oracle.connect('demki/dem18ki92@demp')
    curs = dbcon.cursor()
    curs.execute(sqlstr)

    for rows in curs:

        for col in rows:
            print(col)

    curs.close
    dbcon.close


if __name__ == '__main__':
    main()

