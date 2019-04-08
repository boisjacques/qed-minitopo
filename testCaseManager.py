from mininet.topo import Topo
from mininet.net import Mininet


class TestCaseManager():
    """Runs the test cases"""
    linkopts = []
    lastused = 0

    def __init__(self):
        self.populateLinkopts()

    def getNextTest(self):
        returnList = []
        for i in range(0, 2):
            returnList.append(self.linkopts[self.lastused])
            self.lastused += 1
        return returnList

    def populateLinkopts(self):
        # 10Mbit
        self.linkopts.append(dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=10, delay='110ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=10, delay='100ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=10, delay='175ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=10, delay='200ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=10, delay='5ms', loss=3, max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=10, delay='110ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=10, delay='100ms', loss=3, max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=10, delay='175ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=10, delay='200ms', loss=3, max_queue_size=1000, use_htb=True))

        # 100Mbit
        self.linkopts.append(dict(bw=100, delay='5ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=100, delay='5ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=100, delay='110ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=100, delay='100ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=100, delay='175ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=100, delay='200ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=100, delay='5ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=100, delay='5ms', loss=3, max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=100, delay='110ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=100, delay='100ms', loss=3, max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=100, delay='175ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=100, delay='200ms', loss=3, max_queue_size=1000, use_htb=True))

        # 1000Mbit
        self.linkopts.append(dict(bw=1000, delay='5ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=1000, delay='5ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=1000, delay='110ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=1000, delay='100ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=1000, delay='175ms', max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=1000, delay='200ms', max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=1000, delay='5ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=1000, delay='5ms', loss=3, max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=1000, delay='110ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=1000, delay='100ms', loss=3, max_queue_size=1000, use_htb=True))

        self.linkopts.append(dict(bw=1000, delay='175ms', loss=1, max_queue_size=1000, use_htb=True))
        self.linkopts.append(dict(bw=1000, delay='200ms', loss=3, max_queue_size=1000, use_htb=True))
