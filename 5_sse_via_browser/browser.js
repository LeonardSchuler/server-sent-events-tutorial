import { EventSource } from 'eventsource'

console.log("Connecting...")
const es = new EventSource('http://localhost:9000/')
console.log()

/*
 * This will listen for events with the field `event: notice`.
 */
es.addEventListener('notice', (event) => {
    console.log(event.data)
})

/*
 * This will listen for events with the field `event: update`.
 */
es.addEventListener('update', (event) => {
    console.log(event.data)
})

/*
 * The event "message" is a special case, as it will capture events _without_ an
 * event field, as well as events that have the specific type `event: message`.
 * It will not trigger on any other event type.
 */
es.addEventListener('message', (event) => {
    console.log("Received event:")
    console.log("id:", event.lastEventId)
    console.log("data:", event.data)
    console.log()
})

/**
 * To explicitly close the connection, call the `close` method.
 * This will prevent any reconnection from happening.
 */
setTimeout(() => {
    es.close()
}, 10_000)