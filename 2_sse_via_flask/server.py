from flask import Flask, Response
import time


HOST = "127.0.0.1"
PORT = 9000

app = Flask(__name__)


def event_stream():
    event_id = 1
    while True:
        message = f"Hello! Event {event_id}"
        yield f"id: {event_id}\ndata: {message}\n\n"
        event_id += 1
        time.sleep(2)


@app.route("/")
def sse():
    print()
    resp = Response(event_stream(), mimetype="text/event-stream")
    return resp


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False, threaded=True)
