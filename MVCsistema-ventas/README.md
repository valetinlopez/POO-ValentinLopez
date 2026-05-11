# Sistema de Ventas — API REST

> API backend profesional construida con Node.js + Express, usando arquitectura MVC desacoplada con capas Service, DAO y Domain Models. Persistencia en archivos JSON.

---

## Índice

1. [¿Qué construimos?](#qué-construimos)
2. [¿Por qué esta arquitectura?](#por-qué-esta-arquitectura)
3. [Estructura del proyecto](#estructura-del-proyecto)
4. [Explicación de cada capa](#explicación-de-cada-capa)
5. [Reglas de negocio](#reglas-de-negocio)
6. [Flujo completo de una request](#flujo-completo-de-una-request)
7. [Endpoints disponibles](#endpoints-disponibles)
8. [Cómo correr el proyecto](#cómo-correr-el-proyecto)
9. [Cómo probarlo con Postman](#cómo-probarlo-con-postman)
10. [Tecnologías y por qué las elegimos](#tecnologías-y-por-qué-las-elegimos)

---

## ¿Qué construimos?

Un **sistema de ventas** con tres entidades principales: **Productos**, **Clientes** y **Ventas**. La API permite:

- Crear, leer, actualizar y eliminar productos y clientes (CRUD completo).
- Registrar ventas aplicando reglas de negocio (stock, cliente bloqueado, etc.).
- Cancelar ventas y restaurar el stock automáticamente.

Pero más importante que el dominio del sistema, construimos una **arquitectura profesional y escalable** que separa responsabilidades en capas bien definidas.

---

## ¿Por qué esta arquitectura?

### El problema que resuelve

Imaginá que escribís todo en un solo archivo: las rutas, la validación del stock, la lectura del JSON y la respuesta HTTP. Eso funciona para proyectos pequeños, pero cuando el proyecto crece:

- Se vuelve imposible de leer.
- Un cambio en cómo guardás los datos rompe la lógica de negocio.
- No podés reutilizar código.
- Los errores son difíciles de rastrear.

### La solución: separación de responsabilidades

Dividimos el sistema en capas. Cada capa tiene **una sola responsabilidad** y solo habla con la capa que tiene justo debajo.

```
Request HTTP
     ↓
  ROUTES        → "¿A qué controller mando esto?"
     ↓
CONTROLLERS     → "¿Qué respuesta HTTP devuelvo?"
     ↓
 SERVICES       → "¿Qué reglas de negocio aplico?"
     ↓
   DAOs         → "¿Cómo leo/escribo los datos?"
     ↓
 JSON FILES     → Persistencia real en disco
```

Este patrón se llama **arquitectura en capas** y es la base de casi cualquier backend profesional, sin importar si usa Node.js, Java, Python o cualquier otro lenguaje.

---

## Estructura del proyecto

```
sistema-ventas/
│
├── src/
│   ├── controllers/          # Reciben HTTP, responden HTTP
│   │   ├── productos.controller.js
│   │   ├── clientes.controller.js
│   │   └── ventas.controller.js
│   │
│   ├── services/             # Lógica de negocio (el cerebro)
│   │   ├── productos.service.js
│   │   ├── clientes.service.js
│   │   └── ventas.service.js
│   │
│   ├── dao/                  # Acceso a datos (lee/escribe JSON)
│   │   ├── productos.dao.js
│   │   ├── clientes.dao.js
│   │   └── ventas.dao.js
│   │
│   ├── domain/               # Clases que representan las entidades
│   │   ├── Producto.js
│   │   ├── Cliente.js
│   │   └── Venta.js
│   │
│   ├── routes/               # Define los endpoints de la API
│   │   ├── productos.routes.js
│   │   ├── clientes.routes.js
│   │   └── ventas.routes.js
│   │
│   ├── data/                 # Base de datos (archivos JSON)
│   │   ├── productos.json
│   │   ├── clientes.json
│   │   └── ventas.json
│   │
│   ├── utils/                # Funciones reutilizables
│   │   ├── file.utils.js     # Leer/escribir JSON
│   │   └── id.utils.js       # Generar IDs automáticos
│   │
│   ├── middlewares/
│   │   └── error.middleware.js  # Manejo centralizado de errores
│   │
│   ├── app.js                # Configura Express (middlewares + rutas)
│   └── server.js             # Levanta el servidor en el puerto 3000
│
└── package.json
```

---

## Explicación de cada capa

### Domain Models (`/domain`)

**¿Qué son?**
Clases JavaScript simples que representan las entidades del sistema.

**¿Por qué los usamos?**
Sin ellos, los datos son objetos planos (`{}`) sin estructura garantizada. Con Domain Models, sabemos exactamente qué campos tiene cada entidad. Además, cuando el DAO devuelve un dato, lo instancia como clase, lo que da consistencia en toda la aplicación.

```js
// Ejemplo: domain/Producto.js
class Producto {
  constructor({ id, nombre, precio, stock }) {
    this.id = id;
    this.nombre = nombre;
    this.precio = precio;
    this.stock = stock;
  }
}
```

Cada vez que el DAO lee un producto del JSON, lo convierte en una instancia de `Producto`. Así, en cualquier parte del código, si tenés una variable `producto`, sabés que tiene `.id`, `.nombre`, `.precio` y `.stock`.

---

### Utils (`/utils`)

**¿Qué son?**
Funciones auxiliares reutilizables que no pertenecen a ninguna capa específica.

**¿Por qué las separamos?**
Si cada DAO escribiera su propia función para leer JSON, tendríamos código duplicado. Si en algún momento cambiamos la forma de leer archivos, habría que cambiar 3 archivos. Al centralizar en `file.utils.js`, cambiamos en un solo lugar.

```js
// utils/file.utils.js
const readJsonFile = async (path) => {
  const data = await fs.readFile(path, "utf-8");
  return JSON.parse(data);
};

const writeJsonFile = async (path, data) => {
  await fs.writeFile(path, JSON.stringify(data, null, 2), "utf-8");
};
```

`id.utils.js` resuelve cómo generar IDs únicos. La estrategia es simple: busca el ID más alto del array y suma 1. Si está vacío, arranca desde 1.

---

### DAO — Data Access Object (`/dao`)

**¿Qué es el patrón DAO?**
Es un patrón de diseño cuyo objetivo es **encapsular todo el acceso a los datos** en un solo lugar. El resto del sistema no sabe si los datos están en un JSON, en una base de datos SQL, o en una API externa. Solo llama al DAO.

**¿Por qué es importante?**
Si mañana cambiamos los archivos JSON por una base de datos PostgreSQL, solo tenemos que reescribir los DAOs. Los services, controllers y routes no cambian nada. Eso es lo que se llama **desacoplamiento**.

```js
// dao/productos.dao.js (fragmento)
const getAll = async () => {
  const data = await readJsonFile(DATA_PATH);
  return data.map((item) => new Producto(item)); // convierte a Domain Models
};

const getById = async (id) => {
  const productos = await getAll();
  return productos.find((p) => p.id === id) || null;
};
```

Cada DAO tiene las operaciones CRUD puras: `getAll`, `getById`, `create`, `update`, `remove`. Sin validaciones, sin lógica de negocio.

---

### Services (`/services`)

**¿Qué son?**
La capa más importante del backend. Aquí vive **toda la lógica de negocio**.

**¿Por qué separar la lógica de negocio?**
La lógica de negocio son las "reglas del juego" de tu sistema (no vendas si no hay stock, no atiendas a clientes bloqueados, etc.). Si esa lógica estuviera en el controller, estaría mezclada con código HTTP. Si estuviera en el DAO, mezclaría acceso a datos con reglas. El Service es el lugar correcto porque es puro JavaScript, testeable, y no depende de HTTP ni de cómo se guardan los datos.

```js
// services/ventas.service.js (fragmento)
const crear = async ({ clienteId, productoId, cantidad }) => {
  // Valida cantidad
  if (!cantidad || cantidad <= 0) { ... }

  // Valida que el cliente existe
  const cliente = await clientesDao.getById(clienteId);
  if (!cliente) { ... }

  // Valida que no está bloqueado
  if (cliente.bloqueado) { ... }

  // Valida que el producto existe
  const producto = await productosDao.getById(productoId);
  if (!producto) { ... }

  // Valida stock
  if (producto.stock < cantidad) { ... }

  // Descuenta stock
  await productosDao.update(productoId, { stock: producto.stock - cantidad });

  // Crea la venta
  const total = producto.precio * cantidad;
  return await ventasDao.create({ clienteId, productoId, cantidad, total, fecha });
};
```

Notá que el Service habla con **dos DAOs al mismo tiempo** (productos y ventas). Eso está bien: el Service coordina, los DAOs ejecutan.

---

### Controllers (`/controllers`)

**¿Qué son?**
El punto de contacto entre el mundo HTTP y el mundo JavaScript. Reciben el objeto `req`, llaman al service correspondiente, y devuelven un `res` con el status HTTP correcto.

**¿Qué NO hacen?**

- No leen ni escriben archivos.
- No validan reglas de negocio.
- No calculan totales.

```js
// controllers/ventas.controller.js (fragmento)
const create = async (req, res, next) => {
  try {
    const venta = await ventasService.crear(req.body); // delega al service
    res.status(201).json(venta);                        // responde HTTP
  } catch (error) {
    next(error); // si algo falla, pasa al middleware de errores
  }
};
```

El `try/catch` + `next(error)` es el patrón estándar de Express para manejo de errores asíncrono.

---

### Routes (`/routes`)

**¿Qué son?**
El mapa de tu API. Define qué URL + método HTTP corresponde a qué función del controller.

```js
// routes/ventas.routes.js
router.get("/", ventasController.getAll);         // GET  /api/ventas
router.get("/:id", ventasController.getById);     // GET  /api/ventas/1
router.post("/", ventasController.create);        // POST /api/ventas
router.delete("/:id", ventasController.cancel);   // DELETE /api/ventas/1
```

Son tan simples como esto. Sin lógica, solo mapeo.

---

### Middleware de errores (`/middlewares`)

**¿Qué es un middleware?**
En Express, un middleware es una función que se ejecuta en el medio de una request, antes de llegar al controller o después. El middleware de errores es especial: se activa cuando cualquier función llama `next(error)`.

**¿Por qué centralizarlo?**
Sin él, cada controller tendría que construir su propia respuesta de error. Con él, el formato de error es siempre consistente: `{ "error": "mensaje" }`.

```js
// middlewares/error.middleware.js
const errorMiddleware = (err, req, res, next) => {
  const status = err.status || 500;   // si el error tiene status, lo usa; si no, 500
  const message = err.message || "Error interno del servidor";
  res.status(status).json({ error: message });
};
```

Express reconoce este middleware porque tiene **4 parámetros** (`err, req, res, next`). Siempre debe estar registrado **después de las rutas** en `app.js`.

---

### app.js y server.js

**¿Por qué son dos archivos separados?**

`app.js` configura Express: middlewares, rutas, etc. `server.js` solo levanta el servidor en un puerto.

Esta separación es una buena práctica porque permite importar `app` en tests sin levantar el servidor real. Es una distinción que usan frameworks como NestJS y patrones como los que viste en FastAPI.

```js
// app.js: configura
app.use(express.json());
app.use("/api/productos", productosRoutes);
app.use(errorMiddleware);

// server.js: arranca
app.listen(3000, () => console.log("Servidor corriendo en puerto 3000"));
```

---

## Reglas de negocio

Todas viven en los **Services**, que es el lugar correcto.

| # | Regla                                        | Dónde se aplica      | Error que devuelve                          |
| - | -------------------------------------------- | --------------------- | ------------------------------------------- |
| 1 | No se puede vender sin stock suficiente      | `ventas.service.js` | `Stock insuficiente` (400)                |
| 2 | Un cliente bloqueado no puede comprar        | `ventas.service.js` | `Cliente bloqueado` (400)                 |
| 3 | Al registrar una venta se descuenta el stock | `ventas.service.js` | —                                          |
| 4 | Al cancelar una venta se restaura el stock   | `ventas.service.js` | —                                          |
| 5 | La cantidad debe ser mayor a cero            | `ventas.service.js` | `La cantidad debe ser mayor a cero` (400) |
| 6 | El producto debe existir antes de vender     | `ventas.service.js` | `Producto no encontrado` (404)            |
| 7 | El cliente debe existir antes de vender      | `ventas.service.js` | `Cliente no encontrado` (404)             |

---

## Flujo completo de una request

### Ejemplo: `POST /api/ventas` con body `{ clienteId: 1, productoId: 2, cantidad: 3 }`

```
1. Express recibe la request POST /api/ventas

2. ROUTE: ventas.routes.js
   router.post("/", ventasController.create)
   → Identifica que debe llamar a ventasController.create

3. CONTROLLER: ventas.controller.js → create()
   - Extrae req.body: { clienteId: 1, productoId: 2, cantidad: 3 }
   - Llama a ventasService.crear(req.body)

4. SERVICE: ventas.service.js → crear()
   - Valida que cantidad > 0 ✓
   - Consulta clientesDao.getById(1) → obtiene Juan Perez
   - Valida que no está bloqueado ✓
   - Consulta productosDao.getById(2) → obtiene Mouse Gamer (stock: 5)
   - Valida stock: 5 >= 3 ✓
   - Llama productosDao.update(2, { stock: 2 }) → descuenta stock
   - Calcula total: 8000 * 3 = 24000
   - Llama ventasDao.create({ clienteId: 1, productoId: 2, cantidad: 3, total: 24000, fecha: "2026-05-08" })

5. DAO: ventas.dao.js → create()
   - Lee ventas.json
   - Genera nuevo ID
   - Crea instancia Venta con los datos
   - Escribe ventas.json actualizado
   - Retorna la venta creada

6. Sube por las capas hasta el CONTROLLER
   - Controller recibe la venta
   - Responde: res.status(201).json(venta)

7. El cliente (Postman) recibe:
   HTTP 201 Created
   {
     "id": 1,
     "clienteId": 1,
     "productoId": 2,
     "cantidad": 3,
     "total": 24000,
     "fecha": "2026-05-08"
   }
```

---

## Endpoints disponibles

### Productos — `/api/productos`

| Método | URL                    | Descripción                |
| ------- | ---------------------- | --------------------------- |
| GET     | `/api/productos`     | Obtiene todos los productos |
| GET     | `/api/productos/:id` | Obtiene un producto por ID  |
| POST    | `/api/productos`     | Crea un nuevo producto      |
| PUT     | `/api/productos/:id` | Actualiza un producto       |
| DELETE  | `/api/productos/:id` | Elimina un producto         |

**Body para POST/PUT:**

```json
{
  "nombre": "Teclado Mecánico",
  "precio": 15000,
  "stock": 10
}
```

---

### Clientes — `/api/clientes`

| Método | URL                   | Descripción               |
| ------- | --------------------- | -------------------------- |
| GET     | `/api/clientes`     | Obtiene todos los clientes |
| GET     | `/api/clientes/:id` | Obtiene un cliente por ID  |
| POST    | `/api/clientes`     | Crea un nuevo cliente      |
| PUT     | `/api/clientes/:id` | Actualiza un cliente       |
| DELETE  | `/api/clientes/:id` | Elimina un cliente         |

**Body para POST/PUT:**

```json
{
  "nombre": "Juan Perez",
  "email": "juan@mail.com",
  "bloqueado": false
}
```

---

### Ventas — `/api/ventas`

| Método | URL                 | Descripción                       |
| ------- | ------------------- | ---------------------------------- |
| GET     | `/api/ventas`     | Obtiene todas las ventas           |
| GET     | `/api/ventas/:id` | Obtiene una venta por ID           |
| POST    | `/api/ventas`     | Registra una nueva venta           |
| DELETE  | `/api/ventas/:id` | Cancela una venta (restaura stock) |

**Body para POST:**

```json
{
  "clienteId": 1,
  "productoId": 2,
  "cantidad": 3
}
```

---

## Cómo correr el proyecto

### 1. Clonar o descargar el proyecto

```bash
cd sistema-ventas
```

### 2. Instalar dependencias

```bash
npm install
```

### 3. Correr en modo desarrollo (con auto-restart)

```bash
npm run dev
```

### 4. Correr en modo producción

```bash
npm start
```

El servidor queda disponible en `http://localhost:3000`.

---

## Cómo probarlo con Postman

### Crear un producto

- Método: `POST`
- URL: `http://localhost:3000/api/productos`
- Body (JSON): `{ "nombre": "Auriculares", "precio": 5000, "stock": 8 }`

### Registrar una venta

- Método: `POST`
- URL: `http://localhost:3000/api/ventas`
- Body (JSON): `{ "clienteId": 1, "productoId": 1, "cantidad": 2 }`

### Probar cliente bloqueado

- El cliente con ID 3 (Carlos Ruiz) está bloqueado por defecto.
- Intentar hacer una venta con `clienteId: 3` devuelve `{ "error": "Cliente bloqueado" }`.

### Probar stock insuficiente

- Mouse Gamer tiene stock 5. Intentar vender cantidad 10 devuelve `{ "error": "Stock insuficiente" }`.

### Cancelar una venta

- Método: `DELETE`
- URL: `http://localhost:3000/api/ventas/1`
- El stock del producto se restaura automáticamente.

---

## Tecnologías y por qué las elegimos

### Node.js

Es el entorno de ejecución de JavaScript en el servidor. Lo elegimos porque es el ecosistema natural para aprender backend junto con el JavaScript que ya conocemos del frontend.

### Express

Es el framework web más usado en Node.js. Muy minimalista: solo te da lo necesario (routing, middlewares, manejo de requests/responses) sin imponer estructura. Eso lo hace ideal para aprender, porque vos construís la arquitectura.

### fs/promises

El módulo nativo de Node.js para trabajar con el sistema de archivos de forma asíncrona. Lo elegimos para persistencia en lugar de una base de datos real porque el objetivo de este proyecto es aprender la arquitectura, no la integración con bases de datos. La lógica de negocio es exactamente igual con PostgreSQL o MongoDB; solo cambia el DAO.

### async/await

Toda la lógica asíncrona usa `async/await` en lugar de callbacks o `.then()`. Es la forma moderna y legible de manejar operaciones asíncronas en JavaScript, y es exactamente lo mismo que usás con Promises o con SQLAlchemy async en FastAPI.

### nodemon

Herramienta de desarrollo que reinicia automáticamente el servidor cuando modificás un archivo. Solo se instala como dependencia de desarrollo (`--save-dev`) porque en producción no se usa.

---

## Conceptos clave para recordar

| Concepto                        | Definición simple                                                                           |
| ------------------------------- | -------------------------------------------------------------------------------------------- |
| **Arquitectura en capas** | Dividir el sistema en zonas con responsabilidades únicas                                    |
| **Patrón DAO**           | Encapsular todo el acceso a datos en una sola clase/módulo                                  |
| **Service Layer**         | Capa donde vive la lógica de negocio, sin saber de HTTP ni de bases de datos                |
| **Domain Model**          | Clase que representa una entidad del sistema (Producto, Cliente, Venta)                      |
| **Middleware**            | Función que se ejecuta entre la request y la response                                       |
| **Desacoplamiento**       | Que las capas no dependan directamente entre sí para poder cambiarlas independientemente    |
| **REST**                  | Estilo de API donde cada recurso tiene su URL y se usan verbos HTTP (GET, POST, PUT, DELETE) |
| **async/await**           | Forma de escribir código asíncrono que parece sincrónico y es más legible                |
