import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(1, 50):
    client.sendto(bytes(65430), ("ein32.cloud", 9999))