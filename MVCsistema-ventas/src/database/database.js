const fs = require("fs");
const path = require("path");
const { DatabaseSync } = require("node:sqlite");

const DB_DIRECTORY = path.join(__dirname, "data");
const DB_PATH = process.env.DB_PATH || path.join(DB_DIRECTORY, "sistema-ventas.db");
const SCHEMA_PATH = path.join(__dirname, "schema.sql");
const SEED_PATH = path.join(__dirname, "seed.sql");

let databaseInstance = null;
let initialized = false;

const ensureDatabaseDirectory = () => {
  fs.mkdirSync(path.dirname(DB_PATH), { recursive: true });
};

const readSqlFile = (filePath) => fs.readFileSync(filePath, "utf8");

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

const reseedSequence = (db, tableName) => {
  const maxId = db.prepare(`SELECT COALESCE(MAX(id), 0) AS maxId FROM ${tableName}`).get().maxId;

  const updated = db
    .prepare("UPDATE sqlite_sequence SET seq = ? WHERE name = ?")
    .run(maxId, tableName);

  if (updated.changes === 0) {
    db.prepare("INSERT INTO sqlite_sequence(name, seq) VALUES (?, ?)").run(tableName, maxId);
  }
};

const createSchema = (db) => {
  const schemaSql = readSqlFile(SCHEMA_PATH);
  db.exec(schemaSql);
};

const shouldRunSeed = (db) => {
  const productos = db.prepare("SELECT COUNT(*) AS total FROM productos").get().total;
  const clientes = db.prepare("SELECT COUNT(*) AS total FROM clientes").get().total;
  const ventas = db.prepare("SELECT COUNT(*) AS total FROM ventas").get().total;

  return productos === 0 && clientes === 0 && ventas === 0;
};

const seedDatabase = (db) => {
  if (!shouldRunSeed(db)) {
    return;
  }

  const seedSql = readSqlFile(SEED_PATH);

  withDatabaseTransaction(db, () => {
    db.exec(seedSql);
  });

  reseedSequence(db, "productos");
  reseedSequence(db, "clientes");
  reseedSequence(db, "ventas");
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
