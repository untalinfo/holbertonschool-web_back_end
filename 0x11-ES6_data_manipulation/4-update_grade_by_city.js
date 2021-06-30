export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const grades = newGrades.filter(
        (grade) => grade.studentId === student.id,
      );
      const grade = grades.length ? grades[0].grade : 'N/A';

      return {
        ...student,
        grade,
      };
    });
}
