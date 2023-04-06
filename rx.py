import argparse
import socket
from requests import get


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='metric_synth.py arguments')
    parser.add_argument('-p', '-P', '--port', type=int, help='use local ip', default=12356)

    args = parser.parse_args()

    ip = '127.0.0.1'
    port = args.port

    print(f"{ip}:{port}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    while True:
        data, addr = sock.recvfrom(1024)

        client_msg = "msg from client : {}".format(len(data))
        client_ip = "client IP Addr : {}".format(addr)

        print(client_msg)
        print(client_ip)
