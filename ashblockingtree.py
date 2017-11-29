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


def main():

    # initialize
    appversion = '0.0.1.0'
    log_entry('SQL Text Reader [v.' + appversion + ']')




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

