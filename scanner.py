import socket

# Function to scan a TCP port
def scan_tcp_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"TCP Port {port} is open")
    sock.close()

# Function to scan a UDP port
def scan_udp_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(1)
    
    try:
        # Sending a dummy packet to check if the port is open
        sock.sendto(b'', (host, port))
        data, addr = sock.recvfrom(1024)  # Try to receive a response
        print(f"UDP Port {port} is open")
    except socket.timeout:
        print(f"UDP Port {port} might be open or filtered (no response)")
    except socket.error:
        print(f"UDP Port {port} is closed")
    finally:
        sock.close()

# Main function to choose TCP or UDP scan
def port_scanner(host, port_range, protocol):
    for port in range(port_range[0], port_range[1] + 1):
        if protocol == "TCP":
            scan_tcp_port(host, port)
        elif protocol == "UDP":
            scan_udp_port(host, port)
        else:
            print("Unsupported protocol. Choose TCP or UDP.")

# Input for IP address, port range, and protocol
host = input("Enter host IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
protocol = input("Enter protocol (TCP/UDP): ").upper()

# Start scanning
port_scanner(host, (start_port, end_port), protocol)
