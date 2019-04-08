from mininet.topo import Topo


class BuildTopo(Topo):
    """One switch in a n-path client server setup"""

    def build(self, n=2):
        switch = self.addSwitch('s1')
        client = self.addHost('h1')  # Client
        server = self.addHost('h2')  # Server
        for i in range(0, n):
            self.addLink(client, switch, intfName1='h1-eth' + str(i), bw=10, delay='5ms', max_queue_size=1000)
            self.addLink(server, switch, intfName1='h2-eth' + str(i), bw=10, delay='5ms', max_queue_size=1000)