export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this.name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this.name = value;
  }

  get length() {
    return this.lenght;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this.length = value;
  }

  get students() {
    return this.students;
  }

  set students(value) {
    if (!Array.isArray(value)) {
      throw new TypeError('Students must be a array of string');
    }
    if (value.some((number) => typeof number !== 'string')) {
      throw new TypeError('Students must be a array of string');
    }
    this.students = value;
  }
}
