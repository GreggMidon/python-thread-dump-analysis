'''
Name....: .py
Date....:
Author..: Gregg Midon
Desc....:
Usage...:

Version History:
---------------
self.stack = []

stackrec
source
locked
parking
elements = []
monitor_addr
monitor_type

'''
import props

def exporttofile(threads, lastgid):

    f_hdr = open(props.headerfilename, 'a')
    f_stk = open(props.stackfilename, 'a')
    f_mon = open(props.monitorfilename, 'a')
    f_err = open(props.experrfilename, 'a')

    counter = lastgid + 1

    for t in threads:
        hdr_str = "{},{}".format(counter, t.tostring())
        writetofile(hdr_str, f_hdr)

        ndx = 1
        for s in t.stack:

            try:
                stack_str = "{},{},{}".format(counter, ndx, s.tostring())
                writetofile(stack_str, f_stk)

            except AttributeError:
                writetofile('', f_err)

            if s.rec_type == 'MONITOR':

                monitor_state = ''
                if s.locked:
                    monitor_state = 'L'

                elif s.parking:
                    monitor_state = 'P'

                elif s.waiting:
                    monitor_state = 'W'

                monitor_str = "{},{},{},{},{}".format(counter, ndx, monitor_state, s.monitor_type, s.monitor_addr)
                writetofile(monitor_str, f_mon)

            ndx += 1

        counter += 1

    f_hdr.close()
    f_stk.close()
    f_mon.close()
    f_err.close()


def writetofile(s, fil):
    fil.write(s + '\n')