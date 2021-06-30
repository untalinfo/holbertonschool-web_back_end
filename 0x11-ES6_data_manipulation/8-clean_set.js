export default function cleanSet(set, startString) {
  if (!startString || !startString.length) return '';

  let r = '';
  set.forEach((i) => {
    if (i && i.startsWith(startString)) {
      r += `${i.slice(startString.length)}-`;
    }
  });

  return r.slice(0, -1);
}
