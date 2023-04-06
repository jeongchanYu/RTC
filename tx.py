import argparse
import socket
import pyaudio


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='metric_synth.py arguments')
    parser.add_argument('-p', '-P', '--port', type=int, help='UDP port', default=15888)

    # config setup
    args = parser.parse_args()
    port = args.port
    fb_port = port + 1
    host_ip = socket.gethostbyname(socket.gethostname())

    print(f"Host IP : {host_ip}")
    print("Enter the remote IP : ")
    # remote_ip = input()
    remote_ip = '223.194.33.81'

    audio = pyaudio.PyAudio()

    for index in range(audio.get_device_count()):
        desc = audio.get_device_info_by_index(index)
        print("DEVICE: {device}, INDEX: {index}, RATE: {rate} ".format(
            device=desc["name"], index=index, rate=int(desc["defaultSampleRate"])))

    stream = audio.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024,
                    input_device_index=3)

    # socket open
    tx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rx_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    rx_sock.bind((host_ip, fb_port))
    rx_sock.setblocking(False)

    while True:
        tx_sock.sendto(stream.read(1024), (remote_ip, port))

        try:
            rx_data, addr = rx_sock.recvfrom(1024)
        except BlockingIOError:
            continue
        print(rx_data.decode())