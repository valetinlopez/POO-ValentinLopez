const Producto = require("../domain/Producto");
const { getDatabase } = require("../database/database");

const mapProducto = (row) => new Producto(row);

const getAll = () => {
  const db = getDatabase();
  const rows = db
    .prepare("SELECT id, nombre, precio, stock FROM productos ORDER BY id")
    .all();

  return rows.map(mapProducto);
};

const getById = (id) => {
  const db = getDatabase();
  const row = db
    .prepare("SELECT id, nombre, precio, stock FROM productos WHERE id = ?")
    .get(id);

  return row ? mapProducto(row) : null;
};

const create = (productoData) => {
  const db = getDatabase();
  const result = db
    .prepare("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)")
    .run(productoData.nombre, productoData.precio, productoData.stock);

  return getById(Number(result.lastInsertRowid));
};

const update = (id, cambios) => {
  const actual = getById(id);
  if (!actual) {
    return null;
  }

  const siguiente = { ...actual, ...cambios };
  const db = getDatabase();

  db.prepare(`
    UPDATE productos
    SET nombre = ?, precio = ?, stock = ?
    WHERE id = ?
  `).run(siguiente.nombre, siguiente.precio, siguiente.stock, id);

  return getById(id);
};

const remove = (id) => {
  const producto = getById(id);
  if (!producto) {
    return null;
  }

  const db = getDatabase();
  db.prepare("DELETE FROM productos WHERE id = ?").run(id);
  return producto;
};

module.exports = { getAll, getById, create, update, remove };
