import uvicorn
import asyncio
from starlette.applications import Starlette
from starlette.responses import StreamingResponse
from starlette.routing import Route


HOST = "127.0.0.1"
PORT = 9000


async def sse_event_stream():
    """SSE generator with cooperative yielding."""
    for i in range(1, 6):
        yield f"data: Hello event {i}\n\n"
        await asyncio.sleep(2)  # yield control to event loop


async def sse_endpoint(request):
    print()
    return StreamingResponse(sse_event_stream(), media_type="text/event-stream")


app = Starlette(debug=False, routes=[Route("/", sse_endpoint)])


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
        log_level="info",
        loop="asyncio",
    )
