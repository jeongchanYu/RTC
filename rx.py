import argparse
import socket


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='metric_synth.py arguments')
    parser.add_argument('-p', '-P', '--port', type=int, help='UDP port', default=15888)

    # config setup
    args = parser.parse_args()
    port = args.port
    fb_port = port+1
    host_ip = socket.gethostbyname(socket.gethostname())

    print(f"Host IP : {host_ip}")
    print("Enter the remote IP : ")
    remote_ip = input()
    print(remote_ip)

    # socket open
    tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    rx_sock.bind((host_ip, port))

    while True:
        rx_data, addr = rx_sock.recvfrom(1024)
        tx_sock.sendto(rx_data.encode(), (remote_ip, fb_port))