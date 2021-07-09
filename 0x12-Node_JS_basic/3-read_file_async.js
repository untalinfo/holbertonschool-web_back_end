const fs = require('fs');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      try {
        if (err) reject(Error('Cannot load the database'));
        const totalData = data.split('\n').filter((line) => line).slice(1);

        console.log(`Number of students: ${totalData.length}`);

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

        console.log(`Number of students in CS: ${csCount}. List: ${csStudents}`);
        console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents}`);
        return resolve();
      } catch (err) { return reject(Error('Cannot load the database')); }
    });
  });
};
