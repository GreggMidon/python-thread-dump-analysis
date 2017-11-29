"""
Name....: .py
Date....:
Author..: Gregg Midon
Desc....:
"""
import cx_Oracle
import sqlrepo

def connect_to_db(constr):
    return cx_Oracle.connect(constr)


def getsqlid(dbc):

    # retrieve SQL
    sql = sqlrepo.sqlids

    # get cursor from connection
    curs = dbc.cursor()

    # execute cursor and return results
    rs = curs.execute(sql)

    # fetch and return single record
    return rs


def getsqltext(dbc, sqlid):

    # retrieve SQL
    sqlstr = "select get_sql_text('{}') from dual".format(sqlid)

    # get cursor from connection and exec sql
    curs = dbc.cursor()
    return curs.execute(sqlstr)


