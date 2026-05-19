const Venta = require("../domain/Venta");
const { getDatabase } = require("../database/database");

const mapVenta = (row) =>
  new Venta({
    id: row.id,
    clienteId: row.cliente_id,
    productoId: row.producto_id,
    cantidad: row.cantidad,
    total: row.total,
    fecha: row.fecha,
  });

const getAll = () => {
  const db = getDatabase();
  const rows = db
    .prepare(`
      SELECT id, cliente_id, producto_id, cantidad, total, fecha
      FROM ventas
      ORDER BY id
    `)
    .all();

  return rows.map(mapVenta);
};

const getById = (id) => {
  const db = getDatabase();
  const row = db
    .prepare(`
      SELECT id, cliente_id, producto_id, cantidad, total, fecha
      FROM ventas
      WHERE id = ?
    `)
    .get(id);

  return row ? mapVenta(row) : null;
};

const create = (ventaData) => {
  const db = getDatabase();
  const result = db
    .prepare(`
      INSERT INTO ventas (cliente_id, producto_id, cantidad, total, fecha)
      VALUES (?, ?, ?, ?, ?)
    `)
    .run(
      ventaData.clienteId,
      ventaData.productoId,
      ventaData.cantidad,
      ventaData.total,
      ventaData.fecha
    );

  return getById(Number(result.lastInsertRowid));
};

const remove = (id) => {
  const venta = getById(id);
  if (!venta) {
    return null;
  }

  const db = getDatabase();
  db.prepare("DELETE FROM ventas WHERE id = ?").run(id);
  return venta;
};

const existsByClienteId = (clienteId) => {
  const db = getDatabase();
  const row = db
    .prepare("SELECT EXISTS(SELECT 1 FROM ventas WHERE cliente_id = ?) AS existe")
    .get(clienteId);

  return Boolean(row.existe);
};

const existsByProductoId = (productoId) => {
  const db = getDatabase();
  const row = db
    .prepare("SELECT EXISTS(SELECT 1 FROM ventas WHERE producto_id = ?) AS existe")
    .get(productoId);

  return Boolean(row.existe);
};

module.exports = {
  getAll,
  getById,
  create,
  remove,
  existsByClienteId,
  existsByProductoId,
};
