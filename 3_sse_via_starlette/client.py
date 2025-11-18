import asyncio
import httpx

URL = "http://127.0.0.1:9000/"


async def sse_client(url):
    print(f"Sending: GET {url}\n")
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("GET", url) as response:
            if response.status_code != 200:
                print("Failed to connect:", response.status_code)
                return

            buffer = ""
            async for chunk in response.aiter_bytes(chunk_size=1):
                if chunk:
                    buffer += chunk.decode("utf-8")
                    # SSE events end with double newline
                    while "\n\n" in buffer:
                        event, buffer = buffer.split("\n\n", 1)
                        print("Received event:")
                        print(event)
                        print()
                        print()


if __name__ == "__main__":
    asyncio.run(sse_client(URL))
