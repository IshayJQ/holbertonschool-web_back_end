export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  let pos = 0;
  for (const idx of array) {
    const value = appendString + idx;
    newArray[pos] = value;
    pos += 1;
  }

  return newArray;
}
