const productosService = require("../services/productos.service");

// CONTROLLER: recibe la request HTTP, llama al service, y devuelve la response
// No tiene lógica de negocio: solo traduce HTTP → Service → HTTP

const getAll = async (req, res, next) => {
  try {
    const productos = await productosService.obtenerTodos();
    res.status(200).json(productos);
  } catch (error) {
    next(error); // pasa el error al middleware global
  }
};

const getById = async (req, res, next) => {
  try {
    const id = parseInt(req.params.id);
    const producto = await productosService.obtenerPorId(id);
    res.status(200).json(producto);
  } catch (error) {
    next(error);
  }
};

const create = async (req, res, next) => {
  try {
    const producto = await productosService.crear(req.body);
    res.status(201).json(producto);
  } catch (error) {
    next(error);
  }
};

const update = async (req, res, next) => {
  try {
    const id = parseInt(req.params.id);
    const producto = await productosService.actualizar(id, req.body);
    res.status(200).json(producto);
  } catch (error) {
    next(error);
  }
};

const remove = async (req, res, next) => {
  try {
    const id = parseInt(req.params.id);
    const producto = await productosService.eliminar(id);
    res.status(200).json({ mensaje: "Producto eliminado", producto });
  } catch (error) {
    next(error);
  }
};

module.exports = { getAll, getById, create, update, remove };
