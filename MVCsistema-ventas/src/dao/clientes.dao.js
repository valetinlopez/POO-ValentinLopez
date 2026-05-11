const path = require("path");
const { readJsonFile, writeJsonFile } = require("../utils/file.utils");
const { generateId } = require("../utils/id.utils");
const Cliente = require("../domain/Cliente");

const DATA_PATH = path.join(__dirname, "../data/clientes.json");

const getAll = async () => {
  const data = await readJsonFile(DATA_PATH);
  return data.map((item) => new Cliente(item));
};

const getById = async (id) => {
  const clientes = await getAll();
  return clientes.find((c) => c.id === id) || null;
};

const create = async (clienteData) => {
  const clientes = await getAll();
  const nuevoCliente = new Cliente({
    id: generateId(clientes),
    ...clienteData,
  });
  clientes.push(nuevoCliente);
  await writeJsonFile(DATA_PATH, clientes);
  return nuevoCliente;
};

const update = async (id, cambios) => {
  const clientes = await getAll();
  const index = clientes.findIndex((c) => c.id === id);
  if (index === -1) return null;
  clientes[index] = new Cliente({ ...clientes[index], ...cambios });
  await writeJsonFile(DATA_PATH, clientes);
  return clientes[index];
};

const remove = async (id) => {
  const clientes = await getAll();
  const index = clientes.findIndex((c) => c.id === id);
  if (index === -1) return null;
  const eliminado = clientes.splice(index, 1)[0];
  await writeJsonFile(DATA_PATH, clientes);
  return eliminado;
};

module.exports = { getAll, getById, create, update, remove };
