#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel


class SingleSwitchTopo(Topo):
    """Two routers in a 2-path client server setup"""

    def build(self):
        switch = self.addSwitch('switch')
        client = self.addHost('client', cpu=0.5)
        client.setIP('10.0.0.10',24, intf='client-eth0')
        client.setIP('10.0.0.10',24, intf='client-eth0')
        server = self.addHost('server', cpu=0.5)

        

        self.addLink(client, switch, bw=10, delay='5ms', loss=0, max_queue_size=1000)
        self.addLink(client, switch, bw=10, delay='5ms', loss=0, max_queue_size=1000)
        self.addLink(server, switch, bw=10, delay='5ms', loss=0, max_queue_size=1000)
        self.addLink(server, switch, bw=10, delay='5ms', loss=0, max_queue_size=1000)



def perfTest():
    """Create network and run simple performance test"""
    topo = SingleSwitchTopo()
    net = Mininet(topo=topo,
                  host=CPULimitedHost, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    print "Testing bandwidth between h1 and h4"
    h1, h4 = net.get('h1', 'h4')
    net.iperf((h1, h4))
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    perfTest()
