const productosDao = require("../dao/productos.dao");

// SERVICE: contiene la lógica de negocio de productos
// Coordina operaciones y aplica validaciones antes de tocar el DAO

const obtenerTodos = async () => {
  return await productosDao.getAll();
};

const obtenerPorId = async (id) => {
  const producto = await productosDao.getById(id);
  if (!producto) {
    const error = new Error("Producto no encontrado");
    error.status = 404;
    throw error;
  }
  return producto;
};

const crear = async ({ nombre, precio, stock }) => {
  if (!nombre || nombre.trim() === "") {
    const error = new Error("El nombre del producto es obligatorio");
    error.status = 400;
    throw error;
  }
  if (precio === undefined || precio <= 0) {
    const error = new Error("El precio debe ser mayor a cero");
    error.status = 400;
    throw error;
  }
  if (stock === undefined || stock < 0) {
    const error = new Error("El stock no puede ser negativo");
    error.status = 400;
    throw error;
  }
  return await productosDao.create({ nombre, precio, stock });
};

const actualizar = async (id, cambios) => {
  await obtenerPorId(id); // Valida que exista antes de actualizar
  return await productosDao.update(id, cambios);
};

const eliminar = async (id) => {
  await obtenerPorId(id); // Valida que exista antes de eliminar
  return await productosDao.remove(id);
};

module.exports = { obtenerTodos, obtenerPorId, crear, actualizar, eliminar };
