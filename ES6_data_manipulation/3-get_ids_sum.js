export default function ngetStudentIdsSum(studentLists) {
  // Using the reduce function to calculate the sum of all student ids
  return studentLists.reduce((sum, student) => sum + student.id, 0);
}
