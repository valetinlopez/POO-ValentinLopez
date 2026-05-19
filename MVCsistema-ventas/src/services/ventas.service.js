const ventasDao = require("../dao/ventas.dao");
const productosDao = require("../dao/productos.dao");
const clientesDao = require("../dao/clientes.dao");
const { withTransaction } = require("../database/database");
const {
  createHttpError,
  ensurePositiveInteger,
} = require("../utils/validation.utils");

const obtenerTodas = () => ventasDao.getAll();

const obtenerPorId = (id) => {
  const venta = ventasDao.getById(id);
  if (!venta) {
    throw createHttpError("Venta no encontrada", 404);
  }

  return venta;
};

const crear = ({ clienteId, productoId, cantidad }) => {
  const clienteIdNormalizado = ensurePositiveInteger(clienteId, "clienteId");
  const productoIdNormalizado = ensurePositiveInteger(productoId, "productoId");
  const cantidadNormalizada = ensurePositiveInteger(cantidad, "cantidad");

  return withTransaction(() => {
    const cliente = clientesDao.getById(clienteIdNormalizado);
    if (!cliente) {
      throw createHttpError("Cliente no encontrado", 404);
    }

    if (cliente.bloqueado) {
      throw createHttpError("Cliente bloqueado", 400);
    }

    const producto = productosDao.getById(productoIdNormalizado);
    if (!producto) {
      throw createHttpError("Producto no encontrado", 404);
    }

    if (producto.stock < cantidadNormalizada) {
      throw createHttpError("Stock insuficiente", 400);
    }

    productosDao.update(productoIdNormalizado, {
      stock: producto.stock - cantidadNormalizada,
    });

    const total = producto.precio * cantidadNormalizada;
    const fecha = new Date().toISOString().split("T")[0];

    return ventasDao.create({
      clienteId: clienteIdNormalizado,
      productoId: productoIdNormalizado,
      cantidad: cantidadNormalizada,
      total,
      fecha,
    });
  });
};

const cancelar = (id) =>
  withTransaction(() => {
    const venta = ventasDao.getById(id);
    if (!venta) {
      throw createHttpError("Venta no encontrada", 404);
    }

    const producto = productosDao.getById(venta.productoId);
    if (producto) {
      productosDao.update(venta.productoId, {
        stock: producto.stock + venta.cantidad,
      });
    }

    return ventasDao.remove(id);
  });

module.exports = { obtenerTodas, obtenerPorId, crear, cancelar };
