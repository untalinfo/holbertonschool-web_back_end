export default function groceriesList() {
  const gsArray = [
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ];
  const gsMap = new Map();
  gsArray.forEach((g) => gsMap.set(g[0], g[1]));
  return gsMap;
}
