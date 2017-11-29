'''
Name....: .py
Date....:
Author..: Gregg Midon
Desc....: Represents a single thread read from the dump
Usage...:
'''

class StackRecord:

    def __init__(self):
        self.stackrec = ""
        self.source = ""
        self.locked = False
        self.parking = False
        self.waiting = False
        self.elements = []
        self.monitor_addr = ""
        self.monitor_type = ""
        self.rec_type = ""

    def tostring(self):

        num_elements = len(self.elements)

        if num_elements > 0:
            class_nam = self.elements[num_elements - 2]
            method_nam = self.elements[num_elements - 1]
        else:
            class_nam = ""
            method_nam = ""

        monitor_state = ""
        if self.locked:
            monitor_state = 'L'

        elif self.parking:
            monitor_state = 'P'

        elif self.waiting:
            monitor_state = 'W'

        return "{},{},{},{},{},{},{},{}".format(self.rec_type[0:2], self.stackrec, self.source, self.monitor_addr, self.monitor_type, monitor_state, class_nam, method_nam)
