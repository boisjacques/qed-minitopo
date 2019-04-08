import os
import threading
import time


class SafeguardThread(threading.Thread):

    def __init__(self, name='SafeguardThread'):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event()
        self._sleepperiod = 1.0

        threading.Thread.__init__(self, name=name)

    def run(self):
        """ main control loop """
        print "%s starts at %s" % (self.getName(), time.strftime('%X'))
        count = 0
        while not self._stopevent.isSet():
            count += 1
            if count == 120:
                break
            self._stopevent.wait(self._sleepperiod)
        os.system("killall qed")
        print "Safeguard thread terminated qed instances"

    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set()
        threading.Thread.join(self, timeout)
