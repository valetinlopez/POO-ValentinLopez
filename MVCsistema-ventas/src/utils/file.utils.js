const fs = require("fs/promises");

// Lee un archivo JSON y devuelve su contenido como objeto JS
const readJsonFile = async (path) => {
  const data = await fs.readFile(path, "utf-8");
  return JSON.parse(data);
};

// Escribe un objeto JS como JSON en el archivo indicado
const writeJsonFile = async (path, data) => {
  await fs.writeFile(path, JSON.stringify(data, null, 2), "utf-8");
};

module.exports = { readJsonFile, writeJsonFile };
