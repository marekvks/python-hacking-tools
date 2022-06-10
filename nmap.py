import socket

for i in range(20, 30):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.settimeout(2)

    port = i

    try:
        client.connect(("ein32.cloud", port))
        print(f"port {port} je otevřený se službou {socket.getservbyport(port)}")
    except:
        print(f"port {port} je zavřený")