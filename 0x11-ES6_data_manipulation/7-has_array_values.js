export default function hasValuesFromArray(set, array) {
  for (const item of array) if (!set.has(item)) return false;

  return true;
}
