const { spawn } = require('child_process');

/*
 * genero un nuevo proceso hijo con el comando dado.
 * ese nuevo proceso será una instancia de la clase
 * ChildProcess. ChildProcess hereda de EventEmitter.
 */
const child = spawn('cat');

/*
 * asociando la entrada de la terminal
 * a la entrada del subrpoceso
 * la entrada del subproceso
 * es un "stream.Writable".
 */
process.stdin.pipe(child.stdin);

console.log('Welcome to Holberton School, what is your name?');

child.stdout.on('data', (data) => {
  process.stdout.write(`Your name is: ${data}`);
});

child.on('exit', () => {
  console.log('This important software is now closing');
});
