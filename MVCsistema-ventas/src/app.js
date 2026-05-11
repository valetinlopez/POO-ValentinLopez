const express = require("express");
const productosRoutes = require("./routes/productos.routes");
const clientesRoutes = require("./routes/clientes.routes");
const ventasRoutes = require("./routes/ventas.routes");
const errorMiddleware = require("./middlewares/error.middleware");

const app = express();

// Middleware para parsear JSON en el body de las requests
app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    mensaje: "Bienvenido a la API del sistema de ventas",
    endpoints: [
      "/api/productos",
      "/api/clientes",
      "/api/ventas",
    ],
  });
});

// Registro de rutas con su prefijo base
app.use("/api/productos", productosRoutes);
app.use("/api/clientes", clientesRoutes);
app.use("/api/ventas", ventasRoutes);

// Middleware de errores: siempre al final, después de las rutas
app.use(errorMiddleware);

module.exports = app;
