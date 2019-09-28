'''
for tests
'''

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, object):
        self.log(object)
        super().append(object)

ll = LoggableList()
ll.append([1, 2])
ll.append(4)
print(ll)

