'''
Name....: .py
Date....:
Author..: Gregg Midon
Desc....:
Usage...:

Version History:
---------------

Example Records...
2017-07-20 11:38:09
Full thread dump Java HotSpot(TM) 64-Bit Server VM (25.121-b13 mixed mode):
"Query_Execution_4898" #15779 daemon prio=5 os_prio=0 tid=0x00007f3a886ce800 nid=0x20a7 waiting on condition [0x00007f3a69baa000]
java.lang.Thread.State: TIMED_WAITING (parking)
at sun.misc.Unsafe.park(Native Method)
- parking to wait for  <0x00000006d8262040> (a java.util.concurrent.locks.AbstractQueuedSynchronizer$ConditionObject)
at java.util.concurrent.locks.LockSupport.parkNanos(LockSupport.java:215)

'''
import re
import sys
import props
from time import strftime
from threadobj import ThreadObj
from threadparser import parsetimestamprec,parsemetarec,parseheaderrec,parsestatusrec,parsestackrec,parseactionrec
from export import exporttofile

def main():

    # initialize
    log_entry('Thread Dump Parser/Analyzer [v' + props.appversion + ']')
    threadtime = None
    metadata = None
    threads = []

    # open the source file
    log_entry('-> opening source file.')

    try:
        fin = open(props.sourcefilename, "r")
        ferr = open(props.errfilename, "a")

    except FileNotFoundError:
        to_console('Source file not found. Exiting!')
        exit(-1)

    # read the contents of the file
    log_entry('-> looping thru data file.')

    lcount = 0
    newobj = False

    for line in fin:

        # remove extra carriage return
        line = line[:-1]

        # remove leading spaces
        line = re.sub(r'^\s+', '', line)

        lcount += 1

        # determine type of record...
        if line[0:4] == '2017':

            threadtime = parsetimestamprec(line)

        elif line[0:4] == 'Full':

            metadata = parsemetarec(line[:-1])

        elif line[0:1] == '"':

            if newobj:
                threads.append(t)

            # create new thread object
            t = ThreadObj(threadtime, metadata)
            t.lineno = lcount
            newobj = True

            # parse the header record
            headerdict = parseheaderrec(line)
            t.addheader(headerdict)

        elif line[0:4] == 'java':

            t.status = parsestatusrec(line)

        elif line[0:3] == 'at ':

            t.addtostack(parsestackrec(line))

        elif line[0:2] == '- ':

            mon_rec = parseactionrec(line)
            if mon_rec:
                t.addtostack(parseactionrec(line))
            else:
                write_to_file(line, ferr)

        else:
            if len(line) > 0:
                write_to_file("[" + str(lcount) + "]", ferr)
                write_to_file(line, ferr)

    # add final thread obj
    if t:
        threads.append(t)

    log_entry('-> exporting to file.')
    exporttofile(threads, props.counterstart)

    # shut down
    log_entry('-> shutting down.')
    fin.close()
    ferr.close()

    log_entry('-> end.')


def log_entry(s):
    date_str = strftime('%x %X') + ': '
    print(date_str + s)


def to_console(s):
    print(s)


def write_to_file(s, fil):
    fil.write(s + '\n')


def to_float(s):
    if s == '':
        return 0.0

    return float(s)


if __name__ == '__main__':
    main()

