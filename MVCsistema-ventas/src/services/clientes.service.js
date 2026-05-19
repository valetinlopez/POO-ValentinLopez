const clientesDao = require("../dao/clientes.dao");
const ventasDao = require("../dao/ventas.dao");
const {
  createHttpError,
  ensureNonEmptyString,
  ensureOptionalBoolean,
  ensureValidEmail,
} = require("../utils/validation.utils");

const validarPayloadCliente = (payload, { parcial = false } = {}) => {
  const cambios = {};

  if (!parcial || payload.nombre !== undefined) {
    cambios.nombre = ensureNonEmptyString(payload.nombre, "nombre");
  }

  if (!parcial || payload.email !== undefined) {
    cambios.email = ensureValidEmail(payload.email);
  }

  if (!parcial || payload.bloqueado !== undefined) {
    cambios.bloqueado = ensureOptionalBoolean(payload.bloqueado, "bloqueado") ?? false;
  }

  return cambios;
};

const validarEmailUnico = (email, clienteIdActual = null) => {
  const existente = clientesDao.getByEmail(email);
  if (existente && existente.id !== clienteIdActual) {
    throw createHttpError("Ya existe un cliente con ese email", 400);
  }
};

const obtenerTodos = () => clientesDao.getAll();

const obtenerPorId = (id) => {
  const cliente = clientesDao.getById(id);
  if (!cliente) {
    throw createHttpError("Cliente no encontrado", 404);
  }

  return cliente;
};

const crear = (payload) => {
  const cliente = validarPayloadCliente(payload);
  validarEmailUnico(cliente.email);
  return clientesDao.create(cliente);
};

const actualizar = (id, cambios) => {
  const actual = obtenerPorId(id);

  if (!cambios || Object.keys(cambios).length === 0) {
    throw createHttpError("Debe enviar al menos un campo para actualizar", 400);
  }

  const cambiosValidados = validarPayloadCliente(cambios, { parcial: true });

  if (cambiosValidados.email) {
    validarEmailUnico(cambiosValidados.email, actual.id);
  }

  return clientesDao.update(id, cambiosValidados);
};

const eliminar = (id) => {
  obtenerPorId(id);

  if (ventasDao.existsByClienteId(id)) {
    throw createHttpError(
      "No se puede eliminar el cliente porque tiene ventas asociadas",
      400
    );
  }

  return clientesDao.remove(id);
};

module.exports = { obtenerTodos, obtenerPorId, crear, actualizar, eliminar };
