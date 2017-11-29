'''
Name....: thread_dump.py
Date....: 7/18/2017
Author..: Gregg Midon
Desc....: Retrieve a thread dump from prod. app. server
Usage...:

Version History:
---------------
0.0.1   07/18/2017  Original version

'''
import os,sys
import datetime

def main():

    d = datetime.datetime.now()

    # navigate to the script directory
    cwd = os.getcwd()
    if not cwd == "c:\\development\\scripts":
        os.chdir(r'c:\development\scripts')

    # retrieve thread dump for admin server
    os.system(r'C:\Development\oracle\wls12212\oracle_common\common\bin\wlst.cmd AdminTd.py')

    # move the output file to the correct directory
    adm_new = "c:\\development\\scripts\\data\\adm_td_{:%Y%m%d_%H%M%S}.td".format(d)
    os.rename("Thread_Dump_AdminServer.txt", adm_new)

    # retrieve thread dump for admin server
    os.system(r'C:\Development\oracle\wls12212\oracle_common\common\bin\wlst.cmd MSrvTd.py')

    # move the output file to the correct directory
    msrv_new = "c:\\development\\scripts\\data\\msrv_td_{:%Y%m%d_%H%M%S}.td".format(d)
    os.rename("Thread_Dump_AdminServer.txt", msrv_new)


if __name__ == '__main__':
    main()
