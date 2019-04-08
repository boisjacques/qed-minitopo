#!/usr/bin/python
import csv
import os
import sys
import time

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import dumpNodeConnections, pmonitor
from mininet.log import setLogLevel
from buildQED import BuildQED
from buildTopo import BuildTopo
from testCaseManager import TestCaseManager
from safeguardThread import SafeguardThread


def testHandler(net):
    """wrapper for tests"""
    tcm = TestCaseManager()
    client, server, switch = net.get('h1', 'h2', "s1")
    params = []
    diffs = []
    times = []
    bandwidth = []
    delay = []
    loss = []
    date = time.strftime('%y%m%j-%X')
    filename = "report-" + date + ".csv"

    for i in range(0, len(tcm.linkopts)):
        print "deleting links 1"
        net.delLinkBetween(client, switch)
        net.delLinkBetween(server, switch)

        print "deleting links 2"
        net.delLinkBetween(client, switch)
        net.delLinkBetween(server, switch)

        dumpNodeConnections(net.hosts)
        linkopts = tcm.getNextTest()
        for j in range(0, 2):
            net.addLink(client, switch, intfName1='h1-eth' + str(j), **linkopts[0])
            net.addLink(server, switch, intfName1='h2-eth' + str(j), **linkopts[1])
        setIPaddresses(net)
        for k in range(0, 25):
            param, diff, runtime = runTest(net, i)
            params.append(param)
            diffs.append(diff)
            times.append(runtime - 1.12)  # Fixed waiting overhead
            testEncoder(linkopts[0], bandwidth, delay, loss)
            csvWriter(params, diffs, times, bandwidth, delay, loss, filename)
        for k in range(0, 25):
            param, diff, runtime = runTest(net, i, "20MB")
            params.append(param)
            diffs.append(diff)
            times.append(runtime - 1.12)  # Fixed waiting overhead
            testEncoder(linkopts[0], bandwidth, delay, loss)
            csvWriter(params, diffs, times, bandwidth, delay, loss, filename)
        for k in range(0, 25):
            param, diff, runtime = runTest(net, i, "50MB")
            params.append(param)
            diffs.append(diff)
            times.append(runtime - 1.12)  # Fixed waiting overhead
            testEncoder(linkopts[0], bandwidth, delay, loss)
            csvWriter(params, diffs, times, bandwidth, delay, loss, filename)


def testEncoder(linkops, bw, dl, lo):
    bandwidth = ""
    delay = linkops["delay"]
    loss = ""
    if linkops["bw"] == 10:
        bandwidth = "low-bw"
    elif linkops["bw"] == 100:
        bandwidth = "mid-bw"
    elif linkops["bw"] == 1000:
        bandwidth = "hi-bw"
    if "loss" in linkops:
        if linkops["loss"] == 1:
            loss = "min-loss"
        elif linkops["loss"] == 3:
            loss = "hi-loss"
    else:
        loss = "no-loss"
    bw.append(bandwidth)
    dl.append(delay)
    lo.append(loss)


def setIPaddresses(net, n=2):
    """Sets the IP addresses"""
    for i in range(0, n):
        net.get('h1').setIP('10.0.0.1' + str(i), 24, intf='h1-eth' + str(i))
        net.get('h2').setIP('10.0.0.2' + str(i), 24, intf='h2-eth' + str(i))


def setupTestbed():
    """Create network and run simple performance test"""
    topo = BuildTopo()
    net = Mininet(topo=topo, link=TCLink)
    setIPaddresses(net)
    return net


def runTest(net, i=0, param="5MB"):
    thread = SafeguardThread()
    thread.start()
    print "Running test " + str(i)
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    loss = net.pingAll()
    if loss != 0:
        print "test network invalid"
        return param, -2, -2
    client, server = net.get('h1', 'h2')
    print "Starting QED server"
    popens = dict()
    starttime = time.time()
    popens[server] = server.popen("qed", "-s", "-file=" + param + ".zip", "-addr=10.0.0.20:4433")
    client.cmd("sleep .1")
    print "Starting QED client"
    popens[client] = client.popen("qed", "-c", "-addr=10.0.0.20:4433")
    for h, line in pmonitor(popens, timeoutms=500):
        if h:
            print '%s: %s' % (h.name, line),
    thread.join()
    finishtime = time.time()
    exectime = finishtime - starttime
    return param, os.system("diff " + param + ".zip recvd_" + param + ".zip"), exectime


def csvWriter(params, diffs, times, bandwidth, delay, loss, filename="testreport.csv"):
    with open(filename, mode='w') as results:
        result_writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(params)):
            result_writer.writerow([params[i], diffs[i], times[i], bandwidth[i], delay[i], loss[i]])


if __name__ == '__main__':
    BuildQED()
    setLogLevel('info')
    net = setupTestbed()
    net.start()
    if len(sys.argv == 2):
        if sys.argv[1] == 't':
            net.startTerms()
            runTest(net)
        else:
            print "invalid parameter, stopping..."
    else:
        testHandler(net)
    net.stop()
