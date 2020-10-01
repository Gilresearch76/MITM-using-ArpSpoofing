# MITM-using-ArpSpoofing
Man in the middle attack using Arp Spoofing.

## Requirements
* Linux OS
* Python 3.7 
```
pip3 install -r requirements.txt 
```

## Getting Started
Syntax:
```
Gil@kali:/root/Desktop$ python MITM.py <interface> <TargetIP> <RouterIP> <pcap file path>
```
For Example:
```
Gil@kali:/root/Desktop$ python MITM.py eth0 192.168.1.52 192.168.1.100 /root/Desktop/Gil
```
Output:
```
The pcap file was created in the path : /root/Desktop/Gil

Arp Spoofing is Running... 156 packets of ARP have been sent So far.
---------------------------------------------------------------------------

Sniffer is Running... 768 packets From the Target have been collected so far.
-----------------------------------------------------------------------------
```
## Authors
Gil Matitiyahu
