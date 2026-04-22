# 📚 Sistema de Biblioteca (Versión Estructurada con PostgreSQL)

## 🧾 Descripción del Proyecto

Este proyecto implementa un sistema de biblioteca utilizando  **Python + Programación Orientada a Objetos + PostgreSQL** .

A diferencia de la versión simple, este sistema está organizado en múltiples archivos y capas, separando responsabilidades y permitiendo una arquitectura más escalable.

---

## 🧱 Estructura del Proyecto

```
biblioteca/
│
├── models/        → Clases del dominio (POO)
├── services/      → Lógica del sistema
├── db/            → Acceso a base de datos
├── main.py        → Punto de entrada
```

---

## 🎯 Objetivos del Sistema

* Aplicar POO de forma modular
* Separar lógica de negocio y persistencia
* Utilizar base de datos PostgreSQL
* Mantener código limpio y escalable

---

## 📦 Capas del Sistema

### 1. 🧠 Models (Modelos)

Contienen las clases principales:

#### 📚 `Libro`

* Representa libros
* Contiene ID de base de datos
* Maneja información básica

#### 👤 `Usuario`

* Representa usuarios
* Incluye identificación persistente

#### 🔄 `Prestamo`

* Relaciona usuario y libro
* Representa una operación del sistema

---

### 2. ⚙️ Services

#### 🏛️ `Biblioteca`

* Administra colecciones
* Maneja lógica general del sistema
* Interactúa con modelos

---

### 3. 🗄️ DB (Base de Datos)

#### `connection.py`

* Maneja conexión a PostgreSQL

#### `queries.py`

Contiene funciones como:

* `insertar_usuario()`
* `insertar_libro()`
* `registrar_prestamo()`

Estas funciones ejecutan SQL directamente.

---

## 🗄️ Base de Datos

Se utiliza PostgreSQL con las siguientes tablas:

### Tabla `usuarios`

* id
* nombre

### Tabla `libros`

* id
* titulo
* autor
* disponible

### Tabla `prestamos`

* id
* usuario_id
* libro_id

---

## 🔗 Relaciones del Sistema

* Usuario → puede tener muchos préstamos
* Libro → puede estar en un préstamo
* Prestamo → conecta Usuario y Libro
* Biblioteca → contiene todo

Tipos:

* **Composición** (Biblioteca)
* **Asociación** (Prestamo)

---

## ▶️ Flujo del Programa

1. Se crean objetos en Python
2. Se guardan en PostgreSQL
3. Se asignan IDs desde la base
4. Se registra un préstamo
5. Se actualiza disponibilidad

---

## 💻 Ejecución

```bash
python main.py
```

Salida esperada:

* Usuario guardado en base
* Libro guardado
* Préstamo registrado

---

## 🧠 Conceptos Aplicados

### Programación Orientada a Objetos:

* Encapsulamiento
* Clases y objetos
* Relaciones entre entidades

### Base de Datos:

* Persistencia de datos
* Claves primarias y foráneas
* Uso de SQL

### Arquitectura:

* Separación en capas
* Modularidad
* Escalabilidad

---

## ⚠️ Decisiones de Diseño

* No se utilizó ORM para mantener simplicidad
* Se separó acceso a datos en módulo independiente
* Se priorizó claridad sobre complejidad

---

## 🚀 Posibles Mejoras

* Menú interactivo
* Consultas SELECT
* Validaciones desde base de datos
* Interfaz gráfica
* API con FastAPI

---

## ✅ Conclusión

Este sistema demuestra una implementación completa de un modelo orientado a objetos conectado a una base de datos real, aplicando buenas prácticas de desarrollo y organización del código.

Se logra una solución clara, escalable y fácilmente mantenible.
