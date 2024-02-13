export default function getListStudentIds(students) {
  // Check if students is an array
  if (!Array.isArray(students)) {
    return [];
  }

  // Use map function to extract ids from the array of objects
  return students.map((student) => student.id);
}
