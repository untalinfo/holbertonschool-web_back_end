import redis from 'redis';
import { promisify } from 'util';

const cli = redis.createClient();

const hgetall = promisify(cli.hgetall).bind(cli);

(async function main() {
    const HolbertonSchools = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };

    for (const school in HolbertonSchools) {
        if (Object.prototype.hasOwnProperty.call(HolbertonSchools, school)) {
            cli.hset(
                'HolbertonSchools',
                school,
                HolbertonSchools[school],
                (err, reply) => {
                    redis.print(`Reply: ${reply}`);
                }
            )
        }
    }
    const hashVal = await hgetall('HolbertonSchools');
    console.log(hashVal);
}())
