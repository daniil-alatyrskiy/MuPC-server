import json
import socket

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

COMMANDS = ['/HW']
last_command = ''


def command_handler(cm):
    if cm in COMMANDS:
        if cm == "/HW":

            return cm


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, (client_host, client_port) = s.accept()
        with conn:
            conn.settimeout(1)
            print(f"Connected by {client_host,client_port}")
            try:
                data = conn.recv(1024)
            except TimeoutError:
                print('Timeout')
            except socket.timeout:
                print('Timeout')
            data_all = data.decode('utf-8')
            if len(data_all.split(' ')) > 1:
                command = data_all.split(' ')[1]
            else:
                command = data_all
            print(command)

            HDRS = 'HTTP/1.1 200\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode('utf-8')

            if command == '/HW':
                last_command = '/HW'

            if command == '/getit':
                conn.send(last_command.encode('utf-8'))  # Use triple-quote string.
                conn.shutdown(socket.SHUT_WR)
                last_command = ''
                continue


            content = data
            conn.send(HDRS + content)  # Use triple-quote string.
            conn.shutdown(socket.SHUT_WR)