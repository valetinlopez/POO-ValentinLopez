### Respuestas a las preguntas teóricas

**¿Qué imprime el objeto antes de sobrescribir `__str__()`?**

Algo como `<__main__.Persona object at 0x7fe0f5963fe0>`. Eso es el comportamiento por defecto heredado de `object`: como `Persona` no define `__str__`, Python cae en `object.__str__`, que a su vez delega en `__repr__`, y el `__repr__` por defecto solo muestra el módulo, la clase y la dirección de memoria del objeto.

**¿Qué cambia después de implementar `__str__()`?**

`print(p1)` y `str(p1)` muestran lo que vos definiste (`"Ana (30 años) - ana@mail.com"`) en lugar de la dirección de memoria. Importante: `__repr__` sigue siendo independiente — si solo sobrescribís `__str__`, `repr(p1)` seguirá mostrando la dirección, salvo que también sobrescribas `__repr__` (como hicimos acá, por buena práctica).

**¿Por qué `p1 == p2` primero da `False`?**

Porque `object.__eq__` por defecto compara  **identidad** , no contenido — es equivalente a `p1 is p2`. Como `p1` y `p2` son dos objetos distintos en memoria (aunque tengan los mismos datos), la comparación da `False`.

**¿Por qué después puede dar `True`?**

Porque al sobrescribir `__eq__` cambiamos el criterio: ahora comparamos **valor** (atributo por atributo: `nombre`, `edad`, `email`) en lugar de identidad. Si los datos coinciden, da `True` sin importar que sean objetos distintos en memoria.

**¿Qué relación tienen `__eq__()` y `__hash__()`?**

Python tiene un contrato implícito:  **si dos objetos son iguales (`==`), deben tener el mismo hash** . Por eso:

* Cuando sobrescribís `__eq__`, Python automáticamente pone `__hash__ = None` (la clase deja de ser "hasheable") salvo que también definas `__hash__` explícitamente.
* Por eso en la Parte 2 redefinimos `__hash__` usando **los mismos campos** que usa `__eq__` (`hash((nombre, edad, email))`). Esto es necesario para que la clase pueda usarse correctamente en `set` o como clave de `dict` — si no se respeta el contrato, podrías tener dos objetos "iguales" que no se detecten como duplicados en un set, lo cual rompe la estructura de datos.

**¿Cuál sería el equivalente de `getClass()` de Java en Python?**

`type(objeto)` (o `objeto.__class__`). Ambos devuelven la clase del objeto en tiempo de ejecución. La diferencia con Java es que en Python `type()` también sirve para crear clases dinámicamente, y `isinstance()` es preferible a comparar tipos directamente cuando querés chequear pertenencia a una jerarquía (incluye subclases), similar a `instanceof` en Java.
