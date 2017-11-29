import re
import datetime
from stackrecord import StackRecord

#ignore = ['LDAPConnThread','Timer','MTUTimer','ClientNotifForwarder','DoSManager']

def parsetimestamprec(rec):

    pattern = r'^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})'

    match = re.search(pattern, rec)
    if match:
        yr = int(match.group(1))
        mo = int(match.group(2))
        dy = int(match.group(3))
        h = int(match.group(4))
        m = int(match.group(5))
        s = int(match.group(6))

        return datetime.datetime(yr, mo, dy, h, m, s)

    return None


def parsemetarec(rec):

    pattern = r'^Full thread dump'

    match = re.search(pattern, rec)
    if match:
        return rec

    return None


def parseheaderrec(rec):

    # prepare dictionary object for header elements
    attrib = {}

    # thread name
    match = re.search(r'\"(.+?)\"', rec)
    if match:
        name = match.group(1)
        attrib['name'] = name

    else:
        attrib['name'] = ''

    # #number
    match = re.search(r'\#(\d+)\s', rec)
    if match:
        num = int(match.group(1))
        attrib['num'] = num

    else:
        attrib['num'] = ''

    # daemon
    match = re.search(r'daemon', rec)
    if match:
        daemon = True
    else:
        daemon = False

    attrib['daemon'] = daemon

    # priority
    match = re.search(r'prio=(\d+)', rec)
    if match:
        prio = int(match.group(1))
        attrib['prio'] = prio

    else:
        attrib['prio'] = ''

    # OS priority
    match = re.search(r'os_prio=(\d+)', rec)
    if match:
        os_prio = int(match.group(1))
        attrib['os_prio'] = os_prio

    else:
        attrib['os_prio'] = ''

    # tid
    match = re.search(r'tid=([0-9a-z]+)', rec)
    if match:
        tid = match.group(1)
        attrib['tid'] = tid

    else:
        attrib['tid'] = ''

    # nid, state, mem
    match = re.search(r'nid=([0-9a-z]+)\s([0-9a-z ]+)\s\[([0-9a-z]+)\]', rec)
    if match:
        nid = match.group(1)
        state = match.group(2)
        mem = match.group(3)

        attrib['nid'] = nid
        attrib['state'] = state
        attrib['mem'] = mem

    else:
        attrib['nid'] = ''
        attrib['state'] = ''
        attrib['mem'] = ''

    return attrib


def parsestatusrec(rec):

    pattern = r'java.lang.Thread.State\:\s(.+)'

    match = re.search(pattern, rec)
    if match:
        return match.group(1)

    return None


def parsestackrec(rec):

    pattern = r'at\s([0-9a-zA-z.$]+)\((.+?)\)'

    match = re.search(pattern, rec)
    if match:
        method = match.group(1)
        methodsrc = match.group(2)

        splitmethod = method.split('.')

        s = StackRecord()
        s.stackrec = method
        s.source = methodsrc
        s.elements = splitmethod
        s.rec_type = 'METHOD'

        #print(s)
        return s

    return None


def parseactionrec(rec):

    pattern = r'^-\s([a-zA-Z0-9 ]+)\<(.+?)\>\s\((.+?)\)'

    match = re.search(pattern, rec)
    if match:

        s = StackRecord()
        action = match.group(1).strip()
        if action == 'locked':
            s.locked = True

        elif action == 'parking to wait for':
            s.parking = True

        elif action == 'waiting on':
            s.waiting = True

        else:
            return None

        s.monitor_addr = match.group(2)
        s.monitor_type = match.group(3)[2:]
        s.rec_type = 'MONITOR'

        #print(s)
        return s

    return None



