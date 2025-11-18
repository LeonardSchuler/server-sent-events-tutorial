import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware


HOST = "127.0.0.1"
PORT = 9000

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def event_stream():
    """
    Async generator for SSE.
    FastAPI will stream this without chunk headers visible to the client.
    """
    event_id = 1
    while event_id <= 5:
        yield f"id: {event_id}\ndata: Hello! Event {event_id}\n\n"
        event_id += 1
        await asyncio.sleep(2)


@app.get("/")
async def sse():
    print()
    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
    )


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=HOST,
        port=PORT,
        log_level="info",
        loop="asyncio",
    )
