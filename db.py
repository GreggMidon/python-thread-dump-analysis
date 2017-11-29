"""
Name....: orcldb.py
Date....: 04/04/2017
Author..: Gregg Midon
Desc....:
Usage...:
"""
import cx_Oracle

def connect_to_db():
    #note: function to retrieve connection string
    #return cx_Oracle.connect('demki/demd1892@demd')
    return cx_Oracle.connect('demki/dem18ki92@demp')
    #return cx_Oracle.connect('demki/dem18ki92@demq')
