const clientesDao = require("../dao/clientes.dao");

// SERVICE: contiene la lógica de negocio de clientes

const obtenerTodos = async () => {
  return await clientesDao.getAll();
};

const obtenerPorId = async (id) => {
  const cliente = await clientesDao.getById(id);
  if (!cliente) {
    const error = new Error("Cliente no encontrado");
    error.status = 404;
    throw error;
  }
  return cliente;
};

const crear = async ({ nombre, email, bloqueado = false }) => {
  if (!nombre || nombre.trim() === "") {
    const error = new Error("El nombre del cliente es obligatorio");
    error.status = 400;
    throw error;
  }
  if (!email || !email.includes("@")) {
    const error = new Error("El email es inválido");
    error.status = 400;
    throw error;
  }
  return await clientesDao.create({ nombre, email, bloqueado });
};

const actualizar = async (id, cambios) => {
  await obtenerPorId(id);
  return await clientesDao.update(id, cambios);
};

const eliminar = async (id) => {
  await obtenerPorId(id);
  return await clientesDao.remove(id);
};

module.exports = { obtenerTodos, obtenerPorId, crear, actualizar, eliminar };
