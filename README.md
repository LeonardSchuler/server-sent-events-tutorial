```sh
$ python main.py
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