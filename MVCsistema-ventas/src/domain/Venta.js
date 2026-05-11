// Domain Model: representa la entidad Venta tal como existe en el sistema
class Venta {
  constructor({ id, clienteId, productoId, cantidad, total, fecha }) {
    this.id = id;
    this.clienteId = clienteId;
    this.productoId = productoId;
    this.cantidad = cantidad;
    this.total = total;
    this.fecha = fecha;
  }
}

module.exports = Venta;
