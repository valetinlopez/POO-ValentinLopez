const clientesService = require("../services/clientes.service");
const { ensureId } = require("../utils/validation.utils");

const getAll = async (req, res, next) => {
  try {
    const clientes = await clientesService.obtenerTodos();
    res.status(200).json(clientes);
  } catch (error) {
    next(error);
  }
};

const getById = async (req, res, next) => {
  try {
    const id = ensureId(req.params.id);
    const cliente = await clientesService.obtenerPorId(id);
    res.status(200).json(cliente);
  } catch (error) {
    next(error);
  }
};

const create = async (req, res, next) => {
  try {
    const cliente = await clientesService.crear(req.body);
    res.status(201).json(cliente);
  } catch (error) {
    next(error);
  }
};

const update = async (req, res, next) => {
  try {
    const id = ensureId(req.params.id);
    const cliente = await clientesService.actualizar(id, req.body);
    res.status(200).json(cliente);
  } catch (error) {
    next(error);
  }
};

const remove = async (req, res, next) => {
  try {
    const id = ensureId(req.params.id);
    const cliente = await clientesService.eliminar(id);
    res.status(200).json({ mensaje: "Cliente eliminado", cliente });
  } catch (error) {
    next(error);
  }
};

module.exports = { getAll, getById, create, update, remove };
