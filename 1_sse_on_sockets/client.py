import socket

HOST = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print()
    print("Client connecting to server...\n")
    s.connect((HOST, PORT))
    # Send a basic GET request for SSE
    sse_upgrade = (
        "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nAccept: text/event-stream\r\n\r\n"
    )
    print("Sending:", sse_upgrade, sep="\n")
    s.sendall(sse_upgrade.encode("utf-8"))

    buffer = ""
    try:
        while True:
            data = s.recv(1024).decode("utf-8")
            if not data:
                break
            buffer += data
            while "\n\n" in buffer:
                event, buffer = buffer.split("\n\n", 1)
                print("Received:")
                print(event)
                print()
                print()
    except KeyboardInterrupt:
        print("Client stopped.")
