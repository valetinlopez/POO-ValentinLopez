const ventasService = require("../services/ventas.service");
const { ensureId } = require("../utils/validation.utils");

const getAll = async (req, res, next) => {
  try {
    const ventas = await ventasService.obtenerTodas();
    res.status(200).json(ventas);
  } catch (error) {
    next(error);
  }
};

const getById = async (req, res, next) => {
  try {
    const id = ensureId(req.params.id);
    const venta = await ventasService.obtenerPorId(id);
    res.status(200).json(venta);
  } catch (error) {
    next(error);
  }
};

const create = async (req, res, next) => {
  try {
    const venta = await ventasService.crear(req.body);
    res.status(201).json(venta);
  } catch (error) {
    next(error);
  }
};

const cancel = async (req, res, next) => {
  try {
    const id = ensureId(req.params.id);
    const venta = await ventasService.cancelar(id);
    res.status(200).json({ mensaje: "Venta cancelada", venta });
  } catch (error) {
    next(error);
  }
};

module.exports = { getAll, getById, create, cancel };
