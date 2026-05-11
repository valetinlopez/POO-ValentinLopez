const path = require("path");
const { readJsonFile, writeJsonFile } = require("../utils/file.utils");
const { generateId } = require("../utils/id.utils");
const Producto = require("../domain/Producto");

// Ruta al archivo JSON donde se persisten los productos
const DATA_PATH = path.join(__dirname, "../data/productos.json");

// DAO (Data Access Object): única capa que habla con el archivo JSON
// No tiene lógica de negocio, solo operaciones CRUD puras

const getAll = async () => {
  const data = await readJsonFile(DATA_PATH);
  return data.map((item) => new Producto(item));
};

const getById = async (id) => {
  const productos = await getAll();
  return productos.find((p) => p.id === id) || null;
};

const create = async (productoData) => {
  const productos = await getAll();
  const nuevoProducto = new Producto({
    id: generateId(productos),
    ...productoData,
  });
  productos.push(nuevoProducto);
  await writeJsonFile(DATA_PATH, productos);
  return nuevoProducto;
};

const update = async (id, cambios) => {
  const productos = await getAll();
  const index = productos.findIndex((p) => p.id === id);
  if (index === -1) return null;
  productos[index] = new Producto({ ...productos[index], ...cambios });
  await writeJsonFile(DATA_PATH, productos);
  return productos[index];
};

const remove = async (id) => {
  const productos = await getAll();
  const index = productos.findIndex((p) => p.id === id);
  if (index === -1) return null;
  const eliminado = productos.splice(index, 1)[0];
  await writeJsonFile(DATA_PATH, productos);
  return eliminado;
};

module.exports = { getAll, getById, create, update, remove };
