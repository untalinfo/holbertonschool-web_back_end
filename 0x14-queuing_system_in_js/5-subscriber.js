import redis from 'redis';

const cli = redis.createClient();

cli.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})

cli.on('connect', () => {
    console.log('Redis client connected to the server')
})

cli.subscribe('holberton school channel');

cli.on('message', function(channel, message) {
    console.log(message);

    if (message === 'KILL_SERVER') {
        this.unsubscribe(channel);
        process.exit();
    }
})
