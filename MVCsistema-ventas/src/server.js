const app = require("./app");
const { getDatabase, DB_PATH } = require("./database/database");

const PORT = process.env.PORT || 3000;

getDatabase();

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
  console.log(`Base de datos SQLite lista en: ${DB_PATH}`);
});
