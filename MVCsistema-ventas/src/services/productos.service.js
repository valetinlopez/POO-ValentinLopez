const productosDao = require("../dao/productos.dao");
const ventasDao = require("../dao/ventas.dao");
const {
  createHttpError,
  ensureNonEmptyString,
  ensureNonNegativeInteger,
  ensurePositiveNumber,
} = require("../utils/validation.utils");

const validarPayloadProducto = (payload, { parcial = false } = {}) => {
  const cambios = {};

  if (!parcial || payload.nombre !== undefined) {
    cambios.nombre = ensureNonEmptyString(payload.nombre, "nombre");
  }

  if (!parcial || payload.precio !== undefined) {
    cambios.precio = ensurePositiveNumber(payload.precio, "precio");
  }

  if (!parcial || payload.stock !== undefined) {
    cambios.stock = ensureNonNegativeInteger(payload.stock, "stock");
  }

  return cambios;
};

const obtenerTodos = () => productosDao.getAll();

const obtenerPorId = (id) => {
  const producto = productosDao.getById(id);
  if (!producto) {
    throw createHttpError("Producto no encontrado", 404);
  }

  return producto;
};

const crear = (payload) => productosDao.create(validarPayloadProducto(payload));

const actualizar = (id, cambios) => {
  obtenerPorId(id);

  if (!cambios || Object.keys(cambios).length === 0) {
    throw createHttpError("Debe enviar al menos un campo para actualizar", 400);
  }

  return productosDao.update(id, validarPayloadProducto(cambios, { parcial: true }));
};

const eliminar = (id) => {
  obtenerPorId(id);

  if (ventasDao.existsByProductoId(id)) {
    throw createHttpError(
      "No se puede eliminar el producto porque tiene ventas asociadas",
      400
    );
  }

  return productosDao.remove(id);
};

module.exports = { obtenerTodos, obtenerPorId, crear, actualizar, eliminar };
