import argparse
import socket


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='metric_synth.py arguments')
    parser.add_argument('-l', '-L', '--local', type=bool, help='use local ip', default=False)
    parser.add_argument('-p', '-P', '--port', type=str, help='use local ip', default='12356')

    args = parser.parse_args()
    local = args.local

    ip = socket.gethostbyname(socket.gethostname()) if local else socket.gethostbyname(socket.getfqdn())
    port = args.port

    print(f"{ip}:{port}")