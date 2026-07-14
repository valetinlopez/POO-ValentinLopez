# TP - Métodos heredados de `object`

Este trabajo muestra cómo se comporta una clase en Python cuando usa los
métodos heredados de `object` y qué cambia cuando esos métodos se
sobrescriben.

## Estructura del proyecto

```text
Tp-metodosHeredados/
├── MetHeredados.py
├── MetSobreescritos.py
├── Readme.md
├── sources/
│   ├── __init__.py
│   ├── persona_heredada.py
│   └── persona_sobreescrita.py
└── tests/
    ├── __init__.py
    ├── test_persona_heredada.py
    └── test_persona_sobreescrita.py
```

## Clase utilizada

La clase `Persona` contiene tres atributos:

- `nombre`
- `edad`
- `email`

Se crean dos objetos con los mismos datos para comparar el comportamiento por
defecto contra el comportamiento sobrescrito.

## Archivos principales

- `sources/persona_heredada.py`: contiene la clase `Persona` sin sobrescribir
  métodos especiales.
- `sources/persona_sobreescrita.py`: contiene la clase `Persona` con
  `__str__`, `__repr__`, `__eq__` y `__hash__` sobrescritos.
- `MetHeredados.py`: script de demostración de los métodos heredados.
- `MetSobreescritos.py`: script de demostración de los métodos sobrescritos.
- `tests/`: contiene los tests unitarios hechos con `unittest`.

## Cómo ejecutar las demostraciones

Desde la carpeta raíz del repositorio:

```bash
python Tp-metodosHeredados/MetHeredados.py
python Tp-metodosHeredados/MetSobreescritos.py
```

También se pueden ejecutar desde adentro de la carpeta del TP:

```bash
cd Tp-metodosHeredados
python MetHeredados.py
python MetSobreescritos.py
```

## Cómo ejecutar los tests

Desde la carpeta `Tp-metodosHeredados`:

```bash
python -m unittest discover -s tests
```

Resultado esperado:

```text
Ran 10 tests

OK
```

## Parte 1: métodos heredados

En `sources/persona_heredada.py`, la clase `Persona` solo define `__init__`.
Por eso usa los métodos especiales que hereda de `object`.

Se comprueba:

- Imprimir el objeto directamente con `print(persona1)`.
- Convertirlo a texto con `str(persona1)`.
- Obtener su representación con `repr(persona1)`.
- Comparar dos objetos con `persona1 == persona2`.
- Obtener su hash con `hash(persona1)`.
- Mostrar su tipo con `type(persona1)`.
- Ver sus atributos y métodos con `dir(persona1)`.

Aunque `persona1` y `persona2` tienen los mismos datos, la comparación da
`False` porque `object.__eq__` compara identidad, es decir, si son exactamente
el mismo objeto en memoria.

También se ve una representación similar a:

```text
<sources.persona_heredada.Persona object at 0x...>
```

Esa salida corresponde al comportamiento por defecto heredado de `object`.

## Parte 2: métodos sobrescritos

En `sources/persona_sobreescrita.py` se redefinen métodos especiales para que
la clase tenga un comportamiento más claro y útil:

- `__str__`: devuelve una representación legible para el usuario.
- `__repr__`: devuelve una representación más precisa para depuración.
- `__eq__`: compara por valor, usando `nombre`, `edad` y `email`.
- `__hash__`: genera un hash consistente con la igualdad.

Ahora dos objetos con los mismos datos pueden considerarse iguales:

```python
p1 == p2
```

devuelve:

```text
True
```

Además, si dos objetos son iguales, sus hashes también deben ser iguales. Por
eso `__hash__` se calcula con los mismos atributos usados en `__eq__`.

## Tests unitarios

Los tests verifican:

- Que los atributos se guarden correctamente.
- Que `str()` y `repr()` heredados muestren la representación por defecto.
- Que dos objetos no sobrescritos comparen por identidad.
- Que `hash()` funcione en la clase heredada.
- Que `str()` y `repr()` sobrescritos devuelvan los textos esperados.
- Que `__eq__` sobrescrito compare por valor.
- Que `__hash__` sea consistente con `__eq__`.
- Que `type()` y `dir()` incluyan la información esperada.

## Respuestas teóricas

### Qué imprime el objeto antes de sobrescribir `__str__()`

Imprime algo parecido a:

```text
<sources.persona_heredada.Persona object at 0x...>
```

Esto ocurre porque Python usa la representación por defecto heredada de
`object`, que muestra el módulo, la clase y una dirección de memoria.

### Qué cambia después de implementar `__str__()`

`print(persona)` y `str(persona)` muestran el texto definido dentro de
`__str__`, por ejemplo:

```text
Ana (30 años) - ana@mail.com
```

Esto hace que el objeto sea más fácil de leer para una persona.

### Por qué `p1 == p2` primero da `False`

Porque, por defecto, `object.__eq__` compara identidad. Aunque los atributos
sean iguales, `p1` y `p2` son dos objetos distintos en memoria.

### Por qué después puede dar `True`

Porque al sobrescribir `__eq__` se cambia el criterio de comparación. En lugar
de comparar identidad, se comparan los valores de `nombre`, `edad` y `email`.

### Qué relación tienen `__eq__()` y `__hash__()`

Python mantiene una regla importante:

```text
Si dos objetos son iguales con ==, deben tener el mismo hash.
```

Por eso, si se sobrescribe `__eq__`, también conviene definir `__hash__` usando
los mismos atributos. Esto permite que los objetos funcionen correctamente en
estructuras como `set` y como claves de un `dict`.

### Cuál es el equivalente de `getClass()` de Java en Python

El equivalente más directo es:

```python
type(objeto)
```

También se puede usar:

```python
objeto.__class__
```

En general, `type()` es la forma más clara para mostrar la clase de un objeto.
