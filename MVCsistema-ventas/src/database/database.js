const fs = require("fs");
const path = require("path");
const { DatabaseSync } = require("node:sqlite");
const { loadSeedData } = require("./seed-data");

const DB_DIRECTORY = path.join(__dirname, "data");
const DB_PATH = process.env.DB_PATH || path.join(DB_DIRECTORY, "sistema-ventas.db");

let databaseInstance = null;
let initialized = false;

const ensureDatabaseDirectory = () => {
  fs.mkdirSync(path.dirname(DB_PATH), { recursive: true });
};

const withDatabaseTransaction = (db, callback) => {
  db.exec("BEGIN IMMEDIATE TRANSACTION;");

  try {
    const result = callback();
    db.exec("COMMIT;");
    return result;
  } catch (error) {
    db.exec("ROLLBACK;");
    throw error;
  }
};

const createSchema = (db) => {
  db.exec(`
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS productos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT NOT NULL,
      precio REAL NOT NULL CHECK (precio > 0),
      stock INTEGER NOT NULL CHECK (stock >= 0)
    );

    CREATE TABLE IF NOT EXISTS clientes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      bloqueado INTEGER NOT NULL DEFAULT 0 CHECK (bloqueado IN (0, 1))
    );

    CREATE TABLE IF NOT EXISTS ventas (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      cliente_id INTEGER NOT NULL,
      producto_id INTEGER NOT NULL,
      cantidad INTEGER NOT NULL CHECK (cantidad > 0),
      total REAL NOT NULL CHECK (total >= 0),
      fecha TEXT NOT NULL,
      FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT,
      FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE RESTRICT
    );
  `);
};

const reseedSequence = (db, tableName) => {
  const maxId = db.prepare(`SELECT COALESCE(MAX(id), 0) AS maxId FROM ${tableName}`).get().maxId;

  const updated = db
    .prepare("UPDATE sqlite_sequence SET seq = ? WHERE name = ?")
    .run(maxId, tableName);

  if (updated.changes === 0) {
    db.prepare("INSERT INTO sqlite_sequence(name, seq) VALUES (?, ?)").run(tableName, maxId);
  }
};

const seedTableIfEmpty = (db, tableName, items, insertItem) => {
  const count = db.prepare(`SELECT COUNT(*) AS total FROM ${tableName}`).get().total;
  if (count > 0 || items.length === 0) {
    return;
  }

  withDatabaseTransaction(db, () => {
    for (const row of items) {
      insertItem(row);
    }
  });

  reseedSequence(db, tableName);
};

const seedDatabase = (db) => {
  const seedData = loadSeedData();

  const insertProducto = db.prepare(`
    INSERT INTO productos (id, nombre, precio, stock)
    VALUES (?, ?, ?, ?)
  `);
  const insertCliente = db.prepare(`
    INSERT INTO clientes (id, nombre, email, bloqueado)
    VALUES (?, ?, ?, ?)
  `);
  const insertVenta = db.prepare(`
    INSERT INTO ventas (id, cliente_id, producto_id, cantidad, total, fecha)
    VALUES (?, ?, ?, ?, ?, ?)
  `);

  seedTableIfEmpty(db, "productos", seedData.productos, (producto) => {
    insertProducto.run(producto.id, producto.nombre, producto.precio, producto.stock);
  });

  seedTableIfEmpty(db, "clientes", seedData.clientes, (cliente) => {
    insertCliente.run(
      cliente.id,
      cliente.nombre,
      cliente.email,
      cliente.bloqueado ? 1 : 0
    );
  });

  seedTableIfEmpty(db, "ventas", seedData.ventas, (venta) => {
    insertVenta.run(
      venta.id,
      venta.clienteId,
      venta.productoId,
      venta.cantidad,
      venta.total,
      venta.fecha
    );
  });
};

const getDatabase = () => {
  if (!databaseInstance) {
    ensureDatabaseDirectory();
    databaseInstance = new DatabaseSync(DB_PATH);
    databaseInstance.exec("PRAGMA foreign_keys = ON;");
  }

  if (!initialized) {
    createSchema(databaseInstance);
    seedDatabase(databaseInstance);
    initialized = true;
  }

  return databaseInstance;
};

const withTransaction = (callback) => {
  const db = getDatabase();
  return withDatabaseTransaction(db, callback);
};

const closeDatabase = () => {
  if (databaseInstance) {
    databaseInstance.close();
    databaseInstance = null;
    initialized = false;
  }
};

module.exports = { getDatabase, withTransaction, closeDatabase, DB_PATH };
