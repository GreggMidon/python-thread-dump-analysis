'''
Name....: .py
Date....:
Author..: Gregg Midon
Desc....:
Usage...:

Version History:
---------------


'''
import re

def main():

    #pattern = r'^"[a-zA-Z0-9-_]+'
    #pattern = r'\"(.+?)\"\s\#(\d+)'
    pattern = r'^-\s([a-zA-Z0-9 ]+)\<(.+?)\>\s\((.+?)\)'
    #pattern = r'^-\sparking\sto\swait\sfor\s\<(.+?)\>\s\((.+?)\)'
    p = re.compile(pattern)

    line = '- parking to wait for  <0x00000006d8262040> (a java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject)'
    #line = '- locked <0x0000000798fc2dc0> (a oracle.jdbc.driver.T4CConnection)'

    match = re.search(pattern, line)

    if match:
        print(match.group())
        for x in match.groups():
            print(x)

    else:
        print('No matchie matchie..!')

if __name__ == '__main__':
    main()

