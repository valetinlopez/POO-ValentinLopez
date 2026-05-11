// MIDDLEWARE DE ERRORES GLOBAL
// Express lo identifica por tener 4 parámetros: (err, req, res, next)
// Centraliza el manejo de errores: en vez de responder en cada controller,
// todos los errores se pasan con next(error) y llegan aquí

const errorMiddleware = (err, req, res, next) => {
  const status = err.status || 500;
  const message = err.message || "Error interno del servidor";

  console.error(`[ERROR ${status}] ${message}`);

  res.status(status).json({ error: message });
};

module.exports = errorMiddleware;
