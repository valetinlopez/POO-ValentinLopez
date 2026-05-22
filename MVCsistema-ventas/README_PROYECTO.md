# MVCsistema-ventas

Proyecto backend MVC para gestionar productos, clientes y ventas con persistencia en SQLite.

## Que quedo mejorado

- Persistencia real en base de datos SQLite.
- Inicializacion automatica de tablas al arrancar.
- `schema.sql` para estructura de base.
- `seed.sql` para datos iniciales.
- Validaciones mas estrictas en altas y actualizaciones.
- Emails de clientes unicos.
- IDs invalidos responden `400`.
- Transacciones para crear y cancelar ventas.
- Proteccion contra eliminacion de clientes o productos con ventas asociadas.
- Docker actualizado para persistir la base correcta.

## Base de datos

Archivo por defecto:

```text
src/database/data/sistema-ventas.db
```

Podes cambiarlo con:

```text
DB_PATH
```

## Capas

- `routes`: mapea URL y metodo HTTP.
- `controllers`: recibe `req`, responde `res`.
- `services`: concentra reglas de negocio.
- `dao`: ejecuta consultas SQL.
- `database`: conexion, esquema, seeds y transacciones.
- `domain`: clases `Producto`, `Cliente`, `Venta`.

## Ejecucion

```bash
npm install
npm start
```

Desarrollo:

```bash
npm run dev
```

## Pruebas manuales sugeridas

1. `GET /api/productos`
2. `POST /api/ventas` con un producto con stock disponible
3. `GET /api/productos/:id` para verificar descuento de stock
4. `DELETE /api/ventas/:id` para verificar restauracion
5. `POST /api/clientes` repitiendo un email existente para validar error `400`

## Docker

```bash
docker compose up --build
```

La persistencia se guarda en un volumen montado sobre:

```text
/app/src/database/data
```
