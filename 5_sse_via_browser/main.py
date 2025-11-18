import subprocess
import threading
import time
from rich.live import Live
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns

console = Console()

# Shared buffers for outputs
server_lines = []
client_lines = []


def stream_process(process, buffer):
    """Read process output line by line into buffer."""
    for line in process.stdout:  # text mode returns str
        buffer.append(line.rstrip())
    process.stdout.close()


def render_panels():
    """Create side-by-side panels for server and client."""
    server_text = "\n".join(server_lines[4:])
    client_text = "\n".join(client_lines)

    server_panel = Panel(
        server_text or "[grey]Waiting...[/grey]", title="SERVER", border_style="green"
    )
    client_panel = Panel(
        client_text or "[grey]Waiting...[/grey]", title="BROWSER", border_style="blue"
    )

    return Columns([server_panel, client_panel])


# Start server and client
server = subprocess.Popen(
    ["python", "-u", "server.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)
time.sleep(1)  # allow server to bind to the port

client = subprocess.Popen(
    ["node", "browser.js"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)

# Threads to read output
threading.Thread(
    target=stream_process, args=(server, server_lines), daemon=True
).start()
threading.Thread(
    target=stream_process, args=(client, client_lines), daemon=True
).start()

# Live display
with Live(render_panels(), refresh_per_second=5, console=console) as live:
    while server.poll() is None or client.poll() is None:
        live.update(render_panels())
