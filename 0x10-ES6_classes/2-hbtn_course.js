export default class HolbertonCourse {
  constructor(name, lenght, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof lenght !== 'number') throw TypeError('Length must be a number');
    if (Array.isArray(students) !== true) throw TypeError('students must be a array');
    this.name = name;
    this.lenght = lenght;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name must be a string');
    this._name = newName;
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(newLenght) {
    if (typeof lenght !== 'number') throw TypeError('Length must be a number');
    this._lenght = newLenght;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (Array.isArray(newStudents) !== true) throw TypeError('students must be a array');
    this._students = newStudents;
  }
}
