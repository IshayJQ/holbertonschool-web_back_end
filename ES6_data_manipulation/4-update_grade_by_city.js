export default function updateStudentGradeByCity(students, city, newGrades) {
  // Filter students based on the specified city
  const filteredStudents = students.filter((student) => student.location === city);

  return filteredStudents.map((student) => {
    // Find the grade object for the current student id
    const gradeObject = newGrades.find((grade) => grade.studentId === student.id);

    // If a grade object is found, use the grade value; otherwise, set grade to "N/A"
    const grade = gradeObject ? gradeObject.grade : 'N/A';

    return {
      ...student,
      grade,
    };
  });
}
