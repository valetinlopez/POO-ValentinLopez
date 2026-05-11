// Domain Model: representa la entidad Producto tal como existe en el sistema
// Es una clase simple que estructura y documenta qué campos tiene un Producto
class Producto {
  constructor({ id, nombre, precio, stock }) {
    this.id = id;
    this.nombre = nombre;
    this.precio = precio;
    this.stock = stock;
  }
}

module.exports = Producto;
