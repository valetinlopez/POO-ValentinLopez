
# 📚 Sistema de Biblioteca (Versión Simple en Python)

## 🧾 Descripción del Proyecto

Este programa implementa un sistema básico de biblioteca utilizando **Programación Orientada a Objetos (POO)** en Python.
El objetivo es modelar entidades del mundo real y sus relaciones, permitiendo simular el préstamo de libros a usuarios.

El sistema funciona completamente en memoria (sin base de datos) y demuestra la interacción entre objetos mediante una ejecución por consola.

---

## 🎯 Objetivos del Sistema

* Representar entidades mediante clases
* Aplicar encapsulamiento
* Modelar relaciones entre objetos
* Simular operaciones reales (préstamos)
* Mostrar resultados por consola

---

## 🧱 Clases Implementadas

### 📚 Clase `Libro`

Representa un libro dentro de la biblioteca.

#### Atributos:

* `__titulo`: nombre del libro
* `__autor`: autor del libro
* `__disponible`: indica si el libro está disponible

#### Métodos:

* `prestar()`: cambia el estado a no disponible si puede prestarse
* `devolver()`: vuelve a marcar el libro como disponible
* `mostrar_info()`: devuelve información del libro
* `esta_disponible()`: indica disponibilidad

---

### 👤 Clase `Usuario`

Representa una persona que utiliza la biblioteca.

#### Atributos:

* `__nombre`: nombre del usuario
* `__id`: identificador único

#### Métodos:

* `mostrar_info()`: devuelve información del usuario

---

### 🔄 Clase `Prestamo`

Representa la relación entre un usuario y un libro.

#### Atributos:

* `__usuario`: objeto Usuario
* `__libro`: objeto Libro

#### Métodos:

* `realizar_prestamo()`: intenta prestar el libro
* `devolver_libro()`: devuelve el libro

---

### 🏛️ Clase `Biblioteca`

Administra el sistema completo.

#### Atributos:

* `__libros`: lista de libros
* `__usuarios`: lista de usuarios
* `__prestamos`: lista de préstamos

#### Métodos:

* `agregar_libro()`
* `agregar_usuario()`
* `registrar_prestamo()`
* `mostrar_libros()`

---

## 🔗 Relaciones entre Clases

* `Biblioteca` contiene múltiples `Libro`, `Usuario` y `Prestamo`
* `Prestamo` relaciona un `Usuario` con un `Libro`

Tipos de relación:

* **Composición** : Biblioteca → Libros / Usuarios
* **Asociación** : Prestamo → Usuario + Libro

---

## ▶️ Flujo de Ejecución

1. Se crea la biblioteca
2. Se crean libros y usuarios
3. Se agregan al sistema
4. Se realiza un préstamo
5. Se muestran resultados en consola

---

## 💻 Ejemplo de Uso

Salida esperada:

Usuario: Juan tomó prestado "El Principito"
Lista de libros actualizada con disponibilidad

---

## 🧠 Conceptos de POO Aplicados

* Encapsulamiento (`__atributos`)
* Clases y objetos
* Métodos
* Relaciones entre clases

---

## ✅ Conclusión

Este sistema demuestra cómo modelar entidades reales utilizando POO, destacando la interacción entre objetos y la organización del código de manera clara y mantenible.
