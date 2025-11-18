import requests

URL = "http://127.0.0.1:9000/"


def sse_client(url):
    print(f"Sending: GET {URL}\n")
    with requests.get(url, stream=True) as response:
        if response.status_code != 200:
            print("Failed to connect:", response.status_code)
            return

        buffer = ""
        for chunk in response.iter_content(chunk_size=1, decode_unicode=True):
            if chunk:
                buffer += chunk
                # SSE events end with double newline
                while "\n\n" in buffer:
                    event, buffer = buffer.split("\n\n", 1)
                    print("Received event:")
                    print(event)
                    print()
                    print()


if __name__ == "__main__":
    sse_client(URL)
