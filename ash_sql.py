'''
Name....: .py
Date....:
Author..: Gregg Midon
Desc....:
Usage...:

Version History:
---------------
0.0.1   07/19/2017  Original version

'''
import time
import datetime
from dbobj import getsqlid,getsqltext,connect_to_db

def main():

    # initialize
    appversion = '0.0.1.0'
    log_entry('SQL Text Reader [v.' + appversion + ']')


    # open the source file
    log_entry('-> opening output file.')
    f = open("C:\\Data\\sqldump.txt", "w")

    # connect to the database
    log_entry('-> connect to database.')
    dbc = connect_to_db('demki/dem18ki92@demp')
    #dbc = connect_to_db('demhl/anf0729@demppf')

    # retrieve list of SQL_IDs
    log_entry('-> retrieving SQL_ID list.')
    sqlidrecs = getsqlid(dbc)

    if sqlidrecs:

        log_entry('-> navigating thru SQL_ID list.')

        counter = 1
        for rec in sqlidrecs:

            instance = rec[0]
            session_id = rec[1]
            session_sernum = rec[2]
            sql_id = rec[3]

            out_str = "{} [{},{}]".format(sql_id, session_id, session_sernum)
            write_to_file("----------------------------------------------------------------------------------------", f)
            write_to_file(out_str, f)
            write_to_file("----------------------------------------------------------------------------------------", f)
            #log_entry(out_str)

            # get sql_text
            c = getsqltext(dbc, sql_id)
            for rows in c:
                for col in rows:
                    write_to_file(col, f)


    dbc.close()
    f.close()


def log_entry(s):
    #date_str = strftime('%X %x') + ': '
    #print(date_str + s)
    print(s)


def write_to_file(s, fil):
    if s:
        fil.write(s + '\n')


def to_date(s):
    date_parts = s.split('-')
    yr_part = int(date_parts[0])
    mo_part = int(date_parts[1])
    dy_part = int(date_parts[2])
    return datetime.date(yr_part, mo_part, dy_part)


def to_float(s):
    if s == '':
        return 0.0

    return float(s)


if __name__ == '__main__':
    main()

