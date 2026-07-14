# TP - Metodos heredados de `object`

Este trabajo muestra como se comporta una clase en Python cuando usa los
metodos heredados de `object` y que cambia cuando esos metodos se
sobrescriben.

## Clase utilizada

La clase `Persona` contiene tres atributos:

- `nombre`
- `edad`
- `email`

Se crean dos objetos con los mismos datos para comparar el comportamiento por
defecto y el comportamiento sobrescrito.

## Archivos

- `MetHeredados.py`: demuestra los metodos heredados de `object` sin
  sobrescribirlos.
- `MetSobreescritos.py`: demuestra la misma clase sobrescribiendo `__str__`,
  `__repr__`, `__eq__` y `__hash__`.

## Como ejecutar

Desde la carpeta del proyecto:

```bash
python Tp-metodosHeredados/MetHeredados.py
python Tp-metodosHeredados/MetSobreescritos.py
```

## Parte 1: metodos heredados

En `MetHeredados.py`, la clase `Persona` solo define `__init__`. Por eso usa
los metodos especiales que hereda de `object`.

Se comprueba:

- Imprimir el objeto directamente con `print(persona1)`.
- Convertirlo a texto con `str(persona1)`.
- Obtener su representacion con `repr(persona1)`.
- Comparar dos objetos con `persona1 == persona2`.
- Obtener su hash con `hash(persona1)`.
- Mostrar su tipo con `type(persona1)`.
- Ver sus atributos y metodos con `dir(persona1)`.

### Resultado esperado

Aunque `persona1` y `persona2` tienen los mismos datos, la comparacion da
`False` porque `object.__eq__` compara identidad, es decir, si son exactamente
el mismo objeto en memoria.

Tambien se ve una representacion similar a:

```text
<__main__.Persona object at 0x...>
```

Esa salida corresponde al comportamiento por defecto heredado de `object`.

## Parte 2: metodos sobrescritos

En `MetSobreescritos.py` se redefinen metodos especiales para que la clase
tenga un comportamiento mas claro y util:

- `__str__`: devuelve una representacion legible para el usuario.
- `__repr__`: devuelve una representacion mas precisa para depuracion.
- `__eq__`: compara por valor, usando `nombre`, `edad` y `email`.
- `__hash__`: genera un hash consistente con la igualdad.

### Resultado esperado

Ahora dos objetos con los mismos datos pueden considerarse iguales:

```python
p1 == p2
```

devuelve:

```text
True
```

Ademas, si dos objetos son iguales, sus hashes tambien deben ser iguales. Por
eso `__hash__` se calcula con los mismos atributos usados en `__eq__`.

## Respuestas teoricas

### Que imprime el objeto antes de sobrescribir `__str__()`

Imprime algo parecido a:

```text
<__main__.Persona object at 0x...>
```

Esto ocurre porque Python usa la representacion por defecto heredada de
`object`, que muestra el modulo, la clase y una direccion de memoria.

### Que cambia despues de implementar `__str__()`

`print(persona)` y `str(persona)` muestran el texto definido dentro de
`__str__`, por ejemplo:

```text
Ana (30 anos) - ana@mail.com
```

Esto hace que el objeto sea mas facil de leer para una persona.

### Por que `p1 == p2` primero da `False`

Porque, por defecto, `object.__eq__` compara identidad. Aunque los atributos
sean iguales, `p1` y `p2` son dos objetos distintos en memoria.

### Por que despues puede dar `True`

Porque al sobrescribir `__eq__` se cambia el criterio de comparacion. En lugar
de comparar identidad, se comparan los valores de `nombre`, `edad` y `email`.

### Que relacion tienen `__eq__()` y `__hash__()`

Python mantiene una regla importante:

```text
Si dos objetos son iguales con ==, deben tener el mismo hash.
```

Por eso, si se sobrescribe `__eq__`, tambien conviene definir `__hash__` usando
los mismos atributos. Esto permite que los objetos funcionen correctamente en
estructuras como `set` y como claves de un `dict`.

### Cual es el equivalente de `getClass()` de Java en Python

El equivalente mas directo es:

```python
type(objeto)
```

Tambien se puede usar:

```python
objeto.__class__
```

En general, `type()` es la forma mas clara para mostrar la clase de un objeto.
