export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  cloneCar() {
  const Species = this.constructor[Symbol.species];
    return new Species();
  }
}
