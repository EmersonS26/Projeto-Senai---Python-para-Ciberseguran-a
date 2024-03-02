
from pprint import pprint
from scapy.arch.windows import get_windows_if_list
from scapy.all import *


conf.verb = 0

def parse_packet(packet):
    """sniff callback function."""

    if packet and packet.haslayer('UDP'):
        udp = packet.getlayer('UDP')
        udp.show()


def udp_sniffer():
    """start a sniffer."""
    interfaces = get_windows_if_list()
    pprint(interfaces)

    print('\n[*] start udp sniffer')
    sniff(
        filter = "udp port 53",
        iface=r'Realtek PCIe GbE Family Controller', prn=parse_packet)


    
    
if __name__ ==  '__main__':
    udp_sniffer()