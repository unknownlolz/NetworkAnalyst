import os
import sys
from config import *

# Function to check and install dependencies
def install_dependencies():
    print("Checking and installing dependencies...")
    try:
        import scapy
    except ImportError:
        os.system("pip install scapy")
    print("Dependencies installed.")

# Function to analyze network traffic
def analyze_traffic():
    from scapy.all import sniff

    # Callback function to process each packet
    def process_packet(packet):
        # Extract relevant information from the packet
        src_ip = packet[0][1].src if LOG_SOURCE_IP else ""
        dst_ip = packet[0][1].dst if LOG_DESTINATION_IP else ""
        protocol = packet[0][1].name if LOG_PROTOCOL else ""

        # Log the information if any of the logging options is enabled
        if src_ip or dst_ip or protocol:
            print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")

    # Start sniffing packets
    print("Starting network traffic analysis...")
    sniff(prn=process_packet, store=0)

if __name__ == "__main__":
    # Check and install dependencies
    install_dependencies()

    # Analyze network traffic
    analyze_traffic()
