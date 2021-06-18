export default function createIteratorObject(report) {
  const newArray = [];
  for (const item in report.allEmployees) {
    if (item) newArray.push(...report.allEmployees[item]);
  }
  return newArray;
}
