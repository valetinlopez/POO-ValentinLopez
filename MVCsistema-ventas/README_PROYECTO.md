# MVCsistema-ventas

API REST hecha con Node.js y Express para gestionar productos, clientes y ventas usando arquitectura MVC con capas `routes`, `controllers`, `services`, `dao` y `domain`.

Este README es complementario y no reemplaza al `README.md` original del proyecto.

## Objetivo

El sistema permite:

- Administrar productos con operaciones CRUD.
- Administrar clientes con operaciones CRUD.
- Registrar ventas aplicando reglas de negocio.
- Cancelar ventas y restaurar stock automaticamente.
- Persistir la informacion en archivos JSON dentro de `src/data`.

## Arquitectura

La app esta separada en capas para que cada una tenga una responsabilidad clara:

- `routes`: define endpoints y delega al controller.
- `controllers`: traduce la request HTTP y arma la response.
- `services`: aplica reglas de negocio.
- `dao`: lee y escribe datos en JSON.
- `domain`: modela entidades como `Producto`, `Cliente` y `Venta`.
- `utils`: helpers de archivos e IDs.

## Estructura del proyecto

```text
MVCsistema-ventas/
|-- src/
|   |-- app.js
|   |-- server.js
|   |-- controllers/
|   |-- services/
|   |-- dao/
|   |-- domain/
|   |-- routes/
|   |-- middlewares/
|   `-- data/
|-- Dockerfile
|-- docker-compose.yml
|-- package.json
|-- package-lock.json
|-- README.md
`-- README_PROYECTO.md
```

## Tecnologias

- Node.js
- Express
- Nodemon para desarrollo
- Docker
- Docker Compose

## Requisitos

Para ejecutar localmente:

- Node.js 18 o superior
- npm

Para ejecutar con contenedores:

- Docker Desktop

## Instalacion local

```bash
npm install
```

## Ejecucion local

Modo desarrollo:

```bash
npm run dev
```

Modo normal:

```bash
npm start
```

La API queda disponible en:

```text
http://localhost:3000
```

## Endpoints principales

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

## Reglas de negocio de ventas

Al registrar una venta, la capa `services` valida:

- Que la cantidad sea mayor a cero.
- Que el cliente exista.
- Que el cliente no este bloqueado.
- Que el producto exista.
- Que haya stock suficiente.
- Que se descuente el stock al crear la venta.

Al cancelar una venta:

- Se elimina la venta.
- Se restaura el stock del producto vendido.

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

## Dockerizacion

Se agregaron estos archivos:

- `Dockerfile`
- `docker-compose.yml`
- `.dockerignore`

### Que hace el Dockerfile

- Usa una imagen liviana de Node.js 20 sobre Alpine.
- Copia `package.json` y `package-lock.json`.
- Instala dependencias de produccion con `npm ci --omit=dev`.
- Copia el codigo fuente.
- Expone el puerto `3000`.
- Inicia la app con `npm start`.

### Que hace docker-compose

- Construye la imagen del proyecto.
- Publica el puerto `3000` del contenedor en el `3000` de tu maquina.
- Define variables de entorno.
- Crea un volumen llamado `ventas_data` para persistir `src/data`.
- Reinicia el contenedor automaticamente salvo detencion manual.

## Ejecutar con Docker Compose

Construir y levantar:

```bash
docker compose up --build
```

Levantar en segundo plano:

```bash
docker compose up -d --build
```

Detener:

```bash
docker compose down
```

Detener y eliminar tambien el volumen de datos:

```bash
docker compose down -v
```

## Persistencia de datos

Los archivos JSON de `src/data` se montan en un volumen llamado `ventas_data`.

Eso significa que:

- Si reinicias el contenedor, los datos siguen existiendo.
- Si eliminas el contenedor sin borrar el volumen, los datos se conservan.
- Si ejecutas `docker compose down -v`, se elimina tambien la persistencia.

## Pruebas rapidas

Ruta inicial:

```bash
curl http://localhost:3000/
```

Listar productos:

```bash
curl http://localhost:3000/api/productos
```

## Posibles mejoras futuras

- Agregar variables de entorno mediante archivo `.env`.
- Incorporar validaciones mas estrictas de payload.
- Agregar tests automatizados.
- Migrar la persistencia a una base de datos relacional o NoSQL.
- Incorporar logs y healthchecks para despliegue productivo.
