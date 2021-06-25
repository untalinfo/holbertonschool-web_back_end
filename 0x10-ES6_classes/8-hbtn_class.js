export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  [Symbol.toPrimitive](h) {
    if (h === 'string') {
      return this._location;
    }
    if (h === 'number') {
      return this._size;
    }
    return null;
  }
}
