from scapy.all import srp,Ether,ARP,conf
conf.verb = 0
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst='192.168.1.1-7'), timeout=1, inter = 0.1)
for snd,rcv in ans:
	print rcv.sprintf(r"%Ether.src% - %ARP.psrc%")
print (ans[0][0][1].pdst)
print (ans[1][0][1].pdst)
print (ans[2][0][1].pdst)
