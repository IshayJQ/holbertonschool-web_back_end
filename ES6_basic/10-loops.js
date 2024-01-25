export default function appendToEachArrayValue(array, appendString) {
  array.forEach((value, idx) => {
    array[idx] = appendString + value;
  });

  return array;
}
