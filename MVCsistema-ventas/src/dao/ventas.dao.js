const path = require("path");
const { readJsonFile, writeJsonFile } = require("../utils/file.utils");
const { generateId } = require("../utils/id.utils");
const Venta = require("../domain/Venta");

const DATA_PATH = path.join(__dirname, "../data/ventas.json");

const getAll = async () => {
  const data = await readJsonFile(DATA_PATH);
  return data.map((item) => new Venta(item));
};

const getById = async (id) => {
  const ventas = await getAll();
  return ventas.find((v) => v.id === id) || null;
};

const create = async (ventaData) => {
  const ventas = await getAll();
  const nuevaVenta = new Venta({
    id: generateId(ventas),
    ...ventaData,
  });
  ventas.push(nuevaVenta);
  await writeJsonFile(DATA_PATH, ventas);
  return nuevaVenta;
};

const remove = async (id) => {
  const ventas = await getAll();
  const index = ventas.findIndex((v) => v.id === id);
  if (index === -1) return null;
  const eliminada = ventas.splice(index, 1)[0];
  await writeJsonFile(DATA_PATH, ventas);
  return eliminada;
};

module.exports = { getAll, getById, create, remove };
