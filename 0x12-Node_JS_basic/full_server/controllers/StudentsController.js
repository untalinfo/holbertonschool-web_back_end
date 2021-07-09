const utils = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    utils.readDatabase(process.argv[2])
      .then(({ studentsInfo }) => {
        let csCount = 0;
        let csStudents = '';

        let sweCount = 0;
        let sweStudents = '';

        studentsInfo.forEach((student) => {
          const info = student.split(',');
          if (info[3] === 'CS') {
            csCount += 1;
            csStudents += csStudents ? `, ${info[0]}` : info[0];
          } else if (info[3] === 'SWE') {
            sweCount += 1;
            sweStudents += sweStudents ? `, ${info[0]}` : info[0];
          }
        });
        response.setHeader('Content-Type', 'text/plain');
        response.statusCode = 200;
        response.write('This is the list of our students\n');
        response.write(
          `Number of students in CS: ${csCount}. List: ${csStudents}\n`,
        );
        response.write(
          `Number of students in SWE: ${sweCount}. List: ${sweStudents}`,
        );
        response.end();
      })
      .catch((err) => { response.send(err.message); });
  }

  static getAllStudentsByMajor(request, response) {
    if (!['SWE', 'CS'].includes(request.params.major)) response.status(500).send('Major parameter must be CS or SWE');
    utils.readDatabase(process.argv[2])
      .then(({ studentsInfo }) => {
        let csCount = 0;
        let csStudents = '';

        let sweCount = 0;
        let sweStudents = '';

        studentsInfo.forEach((student) => {
          const info = student.split(',');
          if (info[3] === 'CS') {
            csCount += 1;
            csStudents += csStudents ? `, ${info[0]}` : info[0];
          } else if (info[3] === 'SWE') {
            sweCount += 1;
            sweStudents += sweStudents ? `, ${info[0]}` : info[0];
          }
        });

        if (request.params.major === 'CS' && csCount > 0) {
          response.send(`List: ${csStudents}`);
        } else if (request.params.major === 'SWE' && sweCount > 0) {
          response.send(`List: ${sweStudents}`);
        } else {
          response.status(500).send('Cannot load the database');
        }
      })
      .catch((err) => { response.send(err.message); });
  }
}

module.exports = StudentsController;
