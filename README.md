# Autómata Finito Determinista (AFD)

Este repositorio contiene una implementación básica de un Autómata Finito Determinista (AFD) en Python. Un AFD es un modelo matemático utilizado para simular un sistema con un número finito de estados, donde la transición de un estado a otro depende de una entrada específica.

## Descripción del Código

La clase `miAfd` define un AFD con las siguientes características:

- **Alfabeto:** Conjunto de símbolos permitidos en la cadena de entrada. En este caso, el alfabeto está compuesto por las letras `"A"`, `"B"`, `"C"`, `"D"`, `"E"`, `"F"`.
- **Estados:** Conjunto de estados en los que el autómata puede estar. Los estados definidos son `s0`, `s1` y `s2`.
- **Estado Inicial:** Estado en el que comienza el autómata. En este caso, el estado inicial es `s0`.
- **Estados Finales:** Conjunto de estados de aceptación. Si el autómata termina en alguno de estos estados, la cadena es aceptada. Aquí, el único estado final es `s2`.
- **Transiciones:** Diccionario que define cómo el autómata se mueve de un estado a otro basado en la entrada. Las transiciones están definidas para cada estado y cada símbolo del alfabeto.

### Funcionalidades

- **`reinicio()`:** Restablece el estado actual del autómata al estado inicial (`s0`).
- **`procesar(cadena)`:** Procesa una cadena de entrada y determina si es válida o no según las transiciones del AFD.

### Ejemplo de Uso

afd = miAfd()
valido, msg = afd.procesar("aab")
print(f"La cadena es {msg}")
