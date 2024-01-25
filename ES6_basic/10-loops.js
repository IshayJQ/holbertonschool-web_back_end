export default function appendToEachArrayValue(array, appendString) {
  let pos = 0;
  for (let idx of array) {
    let value = appendString + idx;
    array[pos] = value;
    pos += 1;
  }

  return array;
}
