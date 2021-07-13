import Redis from 'redis';
const cli = Redis.createClient();

cli.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})

cli.on('connect', () => {
    console.log('Redis client connected to the server')
})

const setNewSchool = (schoolName, value) => {
    cli.set(schoolName, value, (err, r) => {
        Redis.print(`Reply: ${r}`);
    });
}

async function displaySchoolValue(schoolName) {
    await cli.get(schoolName, (err, r) => {
        console.log(r);
    });
}

(async function main() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100')
    await displaySchoolValue('HolbertonSanFrancisco');
})()
