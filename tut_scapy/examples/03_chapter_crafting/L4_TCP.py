"""
"""

from scapy.sendrecv import sr1
from scapy.layers.inet import IP, TCP
from scapy.utils import hexdump

# Combine raw ethernet frame with the payload bytes
datagram = IP(dst='192.168.210.240') / TCP()

# Print raw bytes
hexdump(datagram)

# Send the frame
sr1(datagram, iface='Business Network')
