class TestCaseManager():
    """Runs the test cases"""
    linkopts = []
    lastused = 0

    def __init__(self):
        self.populateLinkopts()

    def getNextTest(self, selectedTests=255):
        returnList = []
        if selectedTests == 255:
            for i in range(0, 2):
                returnList.append(self.linkopts[self.lastused])
                self.lastused += 1
        else:
            returnList.append(self.linkopts[selectedTests])
            returnList.append(self.linkopts[selectedTests + 1])
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