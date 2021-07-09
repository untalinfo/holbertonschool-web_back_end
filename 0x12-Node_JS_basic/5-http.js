const http = require('http');
const fs = require('fs');

const args = process.argv;

const PORT = 1245;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      try {
        if (err) reject(Error('Cannot load the database'));
        const totalData = data.split('\n').filter((line) => line).slice(1);

        let csCount = 0;
        let csStudents = '';

        let sweCount = 0;
        let sweStudents = '';

        totalData.forEach((student) => {
          const info = student.split(',');
          if (info[3] === 'CS') {
            csCount += 1;
            csStudents += csStudents ? `, ${info[0]}` : info[0];
          } else if (info[3] === 'SWE') {
            sweCount += 1;
            sweStudents += sweStudents ? `, ${info[0]}` : info[0];
          }
        });

        return resolve({
          total: totalData.length,
          csCount,
          csStudents,
          sweCount,
          sweStudents,
        });
      } catch (err) { return reject(Error('Cannot load the database')); }
    });
  });
}

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/' && req.method === 'GET') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students' && req.method === 'GET') {
    countStudents(args[2]).then(
      ({
        total, csCount, csStudents, sweCount, sweStudents,
      }) => {
        res.statusCode = 200;
        res.write('This is the list of our students\n');
        res.write(`Number of students: ${total}\n`);
        res.write(
          `Number of students in CS: ${csCount}. List: ${csStudents}\n`,
        );
        res.write(
          `Number of students in SWE: ${sweCount}. List: ${sweStudents}`,
        );
        res.end();
      },
    ).catch((err) => {
      res.end(`This is the list of our students
${err.message}`);
    });
  } else { res.end(); }
}).listen(PORT);

module.exports = app;
