// Genera un ID único tomando el máximo ID existente en el array y sumándole 1
// Si el array está vacío, comienza desde 1
const generateId = (array) => {
  if (array.length === 0) return 1;
  const maxId = Math.max(...array.map((item) => item.id));
  return maxId + 1;
};

module.exports = { generateId };
