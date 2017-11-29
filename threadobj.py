'''
Name....: .py
Date....:
Author..: Gregg Midon
Desc....: Represents a single thread read from the dump
Usage...:

Version History:
---------------

'''

class ThreadObj:

    def __init__(self, ts, meta):
        self.name = ""
        self.num = 0
        self.threadtime = ts
        self.metadata = meta
        self.status = ""
        self.prio = 0
        self.os_prio = 0
        self.tid = ""
        self.nid = ""
        self.state = ""
        self.mem = ""
        self.status = ""
        self.stack = []
        self.filename = ""
        self.lineno = 0

    def addheader(self, d):
        self.name = d['name']
        self.num = d['num']
        self.prio = d['prio']
        self.os_prio = d['os_prio']
        self.tid = d['tid']
        self.nid = d['nid']
        self.state = d['state']
        self.mem = d['mem']

    def addtostack(self,s):
        self.stack.append(s)

    def tostring(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(self.threadtime, self.name, self.num, self.prio, self.os_prio, self.tid, self.nid, self.mem, self.state, self.status)
