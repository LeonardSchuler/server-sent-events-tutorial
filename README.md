# Server-Sent Events Tutorials

This project demonstrates **Server-Sent Events (SSE)** in Python using multiple approaches, covering both **synchronous** and **asynchronous** patterns. It includes low-level implementations with **raw sockets** and **Flask** (synchronous), as well as modern async frameworks like **FastAPI** and **Starlette**. Live client examples are provided in Python and the browser to showcase real-time event streaming.

---

## Table of Contents

- [Overview](#overview)  
- [Usage](#usage)  
- [Browser Client](#browser-client)  
- [Implementations](#implementations)  
- [Requirements](#requirements)  

---

## Overview

Server-Sent Events (SSE) allow a server to push real-time updates to clients over HTTP. This PoC demonstrates:

- Low-level SSE using **sockets**  
- Framework-based SSE using **Flask**  
- Async SSE using **FastAPI** and **Starlette**  
- Python client using **httpx/requests**  
- Browser-based client using **EventSource API**  

The project also includes live console dashboards using **Rich** to visualize server and client output side-by-side.

---
## Usage
Run any implementation’s main launcher:
```sh
cd <implementation folder>
python main.py

╭──────────────────── SERVER ────────────────────╮ ╭──────────── CLIENT ─────────────╮
│ SSE Socket server running at 127.0.0.1:9000... │ │                                 │
│                                                │ │ Client connecting to server...  │
│ Connected by ('127.0.0.1', 55575)              │ │                                 │
│                                                │ │ Sending:                        │
│ Responding:                                    │ │ GET / HTTP/1.1                  │
│ HTTP/1.1 200 OK                                │ │ Host: 127.0.0.1                 │
│ Content-Type: text/event-stream                │ │ Accept: text/event-stream       │
│ Cache-Control: no-cache                        │ │                                 │
│ Connection: keep-alive                         │ │                                 │
│                                                │ │ Received:                       │
│                                                │ │ HTTP/1.1 200 OK                 │
│ Sending:                                       │ │ Content-Type: text/event-stream │
│ id: 1                                          │ │ Cache-Control: no-cache         │
│ data: Hello! This is event 1                   │ │ Connection: keep-alive          │
│                                                │ │                                 │
│                                                │ │ id: 1                           │
│ Sending:                                       │ │ data: Hello! This is event 1    │
│ id: 2                                          │ │                                 │
│ data: Hello! This is event 2                   │ │                                 │
│                                                │ │ Received:                       │
│                                                │ │ id: 2                           │
│ Sending:                                       │ │ data: Hello! This is event 2    │
│ id: 3                                          │ │                                 │
│ data: Hello! This is event 3                   │ │                                 │
│                                                │ │ Received:                       │
│                                                │ │ id: 3                           │
│ Sending:                                       │ │ data: Hello! This is event 3    │
│ id: 4                                          │ │                                 │
│ data: Hello! This is event 4                   │ │                                 │
│                                                │ │ Received:                       │
│                                                │ │ id: 4                           │
╰────────────────────────────────────────────────╯ │ data: Hello! This is event 4    │
                                                   │                                 │
                                                   │                                 │
                                                   ╰─────────────────────────────────╯
```

### Browser Client
Open the browser client for SSE testing:

```sh
cd 5_sse_via_browser
python server.py
```
Then open `index.html` in your browser. Events are displayed in the page and console logs.

## Implementations

### 1. SSE via raw sockets
- **Server:** 1_sse_via_sockets/server.py  
- **Client:** 1_sse_via_sockets/client.py  
- **Main launcher:** 1_sse_via_sockets/main.py  

Demonstrates the SSE protocol from scratch using Python sockets and manual HTTP headers.

---

### 2. SSE via Flask
- **Server:** 2_sse_via_flask/server.py  
- **Client:** 2_sse_via_flask/client.py  
- **Main launcher:** 2_sse_via_flask/main.py  

Uses Flask's streaming response to push events to clients.

---

### 3. SSE via Starlette
- **Server:** 3_sse_via_starlette/server.py  
- **Client:** 3_sse_via_starlette/client.py  
- **Main launcher:** 3_sse_via_starlette/main.py  

Async SSE example using Starlette with a StreamingResponse and httpx with an AsyncClient.

---

### 4. SSE via FastAPI
- **Server:** 4_sse_via_fastapi/server.py  
- **Client:** 4_sse_via_fastapi/client.py  
- **Main launcher:** 4_sse_via_fastapi/main.py  

Extends the Starlette example with FastAPI.

---

### 5. SSE via Browser
- **Server:** 5_sse_via_browser/server.py  
- **Browser Client:** 5_sse_via_browser/index.html  
- **Node.js Client:** 5_sse_via_browser/browser.js  
- **Main launcher:** 5_sse_via_browser/main.py  

Demonstrates SSE consumption from the browser using EventSource API and a Node.js client simulating the browser EventSource API.

---

## Requirements

- Python >= 3.13  
- Node.js (for browser.js client)  
- Dependencies (as specified in pyproject.toml and package.json) managed with uv and npm

Install dependencies
```
uv sync
```