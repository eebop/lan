import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.10", 1234))


def get_and_decrypt(clientsocket):
    num_bytes = (ord(clientsocket.recv(8).decode("utf-8")))
    data = []
    for _ in range(num_bytes):
        data.append(s.recv(1))
    return ''.join(data)


def incrypt_and_send():
    clientsocket.send(bytes(chr(len(value)), 'utf-8'))

while True:
    msg = get_and_decrypt(s)
    incrypt_and_send(s, input('send a reply...'))