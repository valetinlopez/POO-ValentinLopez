# Sistema de Ventas API

API REST construida con Node.js y Express usando arquitectura MVC en capas:

- `routes`: define endpoints.
- `controllers`: traduce HTTP.
- `services`: aplica reglas de negocio.
- `dao`: encapsula acceso a datos.
- `domain`: modela entidades.
- `database`: inicializa y administra SQLite.

La persistencia se realiza en una base de datos SQLite local. Si la base esta vacia, se carga un seed inicial definido en codigo.

## Funcionalidades

- CRUD de productos.
- CRUD de clientes.
- Registro de ventas.
- Cancelacion de ventas con restauracion automatica de stock.
- Validaciones de negocio y de payload.
- Restricciones relacionales para evitar datos huerfanos.

## Reglas de negocio

- No se puede vender sin stock suficiente.
- No se puede vender a un cliente bloqueado.
- La cantidad debe ser un entero mayor a cero.
- El precio debe ser mayor a cero.
- El stock no puede ser negativo.
- El email de cliente debe ser valido y unico.
- No se puede eliminar un cliente o producto con ventas asociadas.
- Crear y cancelar ventas se ejecuta dentro de una transaccion.

## Estructura

```text
MVCsistema-ventas/
|-- src/
|   |-- app.js
|   |-- server.js
|   |-- controllers/
|   |-- dao/
|   |-- database/
|   |-- domain/
|   |-- middlewares/
|   |-- routes/
|   |-- services/
|   `-- utils/
|-- Dockerfile
|-- docker-compose.yml
|-- package.json
`-- README.md
```

## Requisitos

- Node.js 24 o superior.
- npm.

Opcional:

- Docker Desktop para correr en contenedores.

## Ejecutar localmente

```bash
npm install
npm start
```

Modo desarrollo:

```bash
npm run dev
```

Servidor:

```text
http://localhost:3000
```

La base queda en:

```text
src/database/data/sistema-ventas.db
```

Tambien podes personalizar la ruta con la variable `DB_PATH`.

## Endpoints

### Base

- `GET /`

### Productos

- `GET /api/productos`
- `GET /api/productos/:id`
- `POST /api/productos`
- `PUT /api/productos/:id`
- `DELETE /api/productos/:id`

### Clientes

- `GET /api/clientes`
- `GET /api/clientes/:id`
- `POST /api/clientes`
- `PUT /api/clientes/:id`
- `DELETE /api/clientes/:id`

### Ventas

- `GET /api/ventas`
- `GET /api/ventas/:id`
- `POST /api/ventas`
- `DELETE /api/ventas/:id`

## Ejemplos de payload

Crear producto:

```json
{
  "nombre": "Teclado mecanico",
  "precio": 45000,
  "stock": 10
}
```

Crear cliente:

```json
{
  "nombre": "Ana Lopez",
  "email": "ana@email.com",
  "bloqueado": false
}
```

Registrar venta:

```json
{
  "clienteId": 1,
  "productoId": 1,
  "cantidad": 2
}
```

## Docker

Construir y levantar:

```bash
docker compose up --build
```

La configuracion usa:

- imagen `node:24-alpine`;
- volumen persistente para `src/database/data`;
- variable `DB_PATH` apuntando al archivo SQLite dentro del contenedor.

## Notas

- El seed inicial vive en `src/database/seed-data.js`.
- El archivo SQLite generado se ignora en Git mediante `.gitignore`.
