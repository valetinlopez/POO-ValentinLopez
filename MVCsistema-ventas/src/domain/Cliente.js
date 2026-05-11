// Domain Model: representa la entidad Cliente tal como existe en el sistema
class Cliente {
  constructor({ id, nombre, email, bloqueado }) {
    this.id = id;
    this.nombre = nombre;
    this.email = email;
    this.bloqueado = bloqueado;
  }
}

module.exports = Cliente;
