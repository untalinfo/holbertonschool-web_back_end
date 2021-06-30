export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) return [];

  return students.reduce((count, student) => count + student.id, 0);
}
