import Redis from 'redis';
const cli = Redis.createClient();

cli.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})

cli.on('connect', () => {
    console.log('Redis client connected to the server')
})
