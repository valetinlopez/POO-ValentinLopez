const DEFAULT_SEED = {
  productos: [
    { id: 1, nombre: "Teclado Mecanico", precio: 15000, stock: 10 },
    { id: 2, nombre: "Mouse Gamer", precio: 8000, stock: 5 },
    { id: 3, nombre: 'Monitor 24"', precio: 60000, stock: 3 },
  ],
  clientes: [
    { id: 1, nombre: "Juan Perez", email: "juan@mail.com", bloqueado: false },
    { id: 2, nombre: "Maria Lopez", email: "maria@mail.com", bloqueado: false },
    { id: 3, nombre: "Carlos Ruiz", email: "carlos@mail.com", bloqueado: true },
  ],
  ventas: [],
};

const loadSeedData = () => DEFAULT_SEED;

module.exports = { loadSeedData };
