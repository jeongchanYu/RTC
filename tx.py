import argparse
import socket
from requests import get
import re


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='metric_synth.py arguments')
    parser.add_argument('-i', '-I', '--ip', type=str, help='UDP ip address', required=True)
    parser.add_argument('-p', '-P', '--port', type=int, help='UDP port', default=15888)

    args = parser.parse_args()
    ip = args.ip
    port = args.port

    print(f"{ip}:{port}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data = input()
        sock.sendto(data.encode(), (ip, port))