const Cliente = require("../domain/Cliente");
const { getDatabase } = require("../database/database");

const mapCliente = (row) =>
  new Cliente({
    ...row,
    bloqueado: Boolean(row.bloqueado),
  });

const getAll = () => {
  const db = getDatabase();
  const rows = db
    .prepare("SELECT id, nombre, email, bloqueado FROM clientes ORDER BY id")
    .all();

  return rows.map(mapCliente);
};

const getById = (id) => {
  const db = getDatabase();
  const row = db
    .prepare("SELECT id, nombre, email, bloqueado FROM clientes WHERE id = ?")
    .get(id);

  return row ? mapCliente(row) : null;
};

const getByEmail = (email) => {
  const db = getDatabase();
  const row = db
    .prepare("SELECT id, nombre, email, bloqueado FROM clientes WHERE lower(email) = lower(?)")
    .get(email);

  return row ? mapCliente(row) : null;
};

const create = (clienteData) => {
  const db = getDatabase();
  const result = db
    .prepare("INSERT INTO clientes (nombre, email, bloqueado) VALUES (?, ?, ?)")
    .run(clienteData.nombre, clienteData.email, clienteData.bloqueado ? 1 : 0);

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
    UPDATE clientes
    SET nombre = ?, email = ?, bloqueado = ?
    WHERE id = ?
  `).run(siguiente.nombre, siguiente.email, siguiente.bloqueado ? 1 : 0, id);

  return getById(id);
};

const remove = (id) => {
  const cliente = getById(id);
  if (!cliente) {
    return null;
  }

  const db = getDatabase();
  db.prepare("DELETE FROM clientes WHERE id = ?").run(id);
  return cliente;
};

module.exports = { getAll, getById, getByEmail, create, update, remove };
