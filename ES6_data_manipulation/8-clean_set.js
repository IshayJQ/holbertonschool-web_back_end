export default function cleanSet(set, startString) {
  // Return an empty string if the startString is not provided or is not a string
  if (typeof startString !== 'string') {
    return '';
  }

  // Filter values from the set that start with the specified startString
  const filteredValues = Array.from(set).filter((value) => value.startsWith(startString));

  // Append the rest of the string for values starting with startString
  const cleanedValues = filteredValues.map((value) => value.slice(startString.length));

  // Concatenate the cleaned values into a single string separated by '-'
  return cleanedValues.join('-');
}
