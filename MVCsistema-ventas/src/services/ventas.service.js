const ventasDao = require("../dao/ventas.dao");
const productosDao = require("../dao/productos.dao");
const clientesDao = require("../dao/clientes.dao");

// SERVICE: aquí vive toda la lógica de negocio de las ventas
// Es la capa más importante del sistema: valida reglas, coordina DAOs y calcula datos

const obtenerTodas = async () => {
  return await ventasDao.getAll();
};

const obtenerPorId = async (id) => {
  const venta = await ventasDao.getById(id);
  if (!venta) {
    const error = new Error("Venta no encontrada");
    error.status = 404;
    throw error;
  }
  return venta;
};

const crear = async ({ clienteId, productoId, cantidad }) => {
  // --- REGLA 5: cantidad debe ser mayor a cero ---
  if (!cantidad || cantidad <= 0) {
    const error = new Error("La cantidad debe ser mayor a cero");
    error.status = 400;
    throw error;
  }

  // --- REGLA 7: el cliente debe existir ---
  const cliente = await clientesDao.getById(clienteId);
  if (!cliente) {
    const error = new Error("Cliente no encontrado");
    error.status = 404;
    throw error;
  }

  // --- REGLA 2: el cliente no puede estar bloqueado ---
  if (cliente.bloqueado) {
    const error = new Error("Cliente bloqueado");
    error.status = 400;
    throw error;
  }

  // --- REGLA 6: el producto debe existir ---
  const producto = await productosDao.getById(productoId);
  if (!producto) {
    const error = new Error("Producto no encontrado");
    error.status = 404;
    throw error;
  }

  // --- REGLA 1: debe haber stock suficiente ---
  if (producto.stock < cantidad) {
    const error = new Error("Stock insuficiente");
    error.status = 400;
    throw error;
  }

  // --- REGLA 3: descontar stock automáticamente ---
  await productosDao.update(productoId, { stock: producto.stock - cantidad });

  // Calcular total de la venta
  const total = producto.precio * cantidad;
  const fecha = new Date().toISOString().split("T")[0]; // formato YYYY-MM-DD

  return await ventasDao.create({ clienteId, productoId, cantidad, total, fecha });
};

const cancelar = async (id) => {
  const venta = await ventasDao.getById(id);
  if (!venta) {
    const error = new Error("Venta no encontrada");
    error.status = 404;
    throw error;
  }

  // --- REGLA 4: restaurar el stock al cancelar una venta ---
  const producto = await productosDao.getById(venta.productoId);
  if (producto) {
    await productosDao.update(venta.productoId, {
      stock: producto.stock + venta.cantidad,
    });
  }

  return await ventasDao.remove(id);
};

module.exports = { obtenerTodas, obtenerPorId, crear, cancelar };
