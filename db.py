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
    #return cx_Oracle.connect('*****/******@****')
    return cx_Oracle.connect('*****/******@****')
    #return cx_Oracle.connect('*****/*******@****')
