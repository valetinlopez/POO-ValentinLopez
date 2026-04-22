# Trabajo Práctico: Uso de Memoria en Objetos e Instancias# 🧠 Trabajo Práctico: Uso de Memoria en Objetos e Instancias

## 🎯 Objetivo

Que los alumnos entiendan:

- Cómo se crean objetos en memoria
- Diferencia entre instancias vs valores primitivos
- Buenas prácticas para evitar uso innecesario de memoria

---

## 📝 Parte 1 – Análisis (sin código)

1. Explicar con sus palabras:

   - ¿Qué pasa en memoria cuando hago `new Dog('Rex')`?
   - ¿Por qué `dog1` y `dog2` ocupan espacios distintos en memoria?
   - ¿Qué diferencia hay entre:
     ```js
     const nombre = "fede";
     const nombre2 = new String("fede");
     ```
2. Dibujar (tipo esquema):

   - Stack vs Heap (simple)
   - Mostrar dónde viven:
     - variables
     - objetos
     - instancias

---

## 💻 Parte 2 – Código (detectar problemas)

Dado este código, identificar malas prácticas:

```js
const nombre = new String("Juan");
const apellido = new String("Perez");

const nombreCompleto = nombre + apellido;

const edad = new Number(30);
const activo = new Boolean(true);



🔧 Parte 3 – Refactor (mejorar uso de memoria)

class User {
  constructor(name) {
    this.name = new String(name);
  }
}

const user1 = new User("Ana");
const user2 = new User("Ana");



🚀 Parte 4 – Instancias y duplicación

const dog1 = new Dog("Rex");
const dog2 = new Dog("Rex");


Parte 5 – Desafío (nivel pro)

Crear una clase Config que:

Solo pueda tener una instancia (Singleton)
Guarde configuraciones como:
url
port
Todos los objetos deben usar la misma instancia


🔥 Bonus (opcional)

Investigar y probar en Node.js:
console.log(process.memoryUsage());
```
