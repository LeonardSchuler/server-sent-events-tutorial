import socket
import time

HOST = "127.0.0.1"
PORT = 9000


def sse_format(message, event_id=None, event=None):
    """Format a message according to SSE protocol"""
    lines = []
    if event_id:
        lines.append(f"id: {event_id}")
    if event:
        lines.append(f"event: {event}")
    for line in message.splitlines():
        lines.append(f"data: {line}")
    lines.append("")  # Blank line indicates end of event
    return "\n".join(lines) + "\n"


# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
    )  # allows instant reuse of the socket
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"SSE Socket server running at {HOST}:{PORT}...\n")

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}\n")
        # Send HTTP response headers for SSE
        sse_response = "HTTP/1.1 200 OK\r\nContent-Type: text/event-stream\r\nCache-Control: no-cache\r\nConnection: keep-alive\r\n\r\n"
        print("Responding:", sse_response, sep="\n")
        conn.sendall(sse_response.encode("utf-8"))

        # Send events every 2 seconds
        event_id = 1
        try:
            while True:
                msg = f"Hello! This is event {event_id}"
                data = sse_format(msg, event_id=event_id)
                print("Sending:", data, sep="\n")
                conn.sendall(data.encode("utf-8"))
                event_id += 1
                time.sleep(2)
        except BrokenPipeError:
            print("Client disconnected.")
