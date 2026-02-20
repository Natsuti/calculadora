Calculadora(Se llama Pendeja, la llamé así por sus primeras versiones)

Pequeño intérprete de expresiones aritméticas escrito en Python desde cero.
El objetivo del proyecto era solo calcular resultados, pero me llevó a implementar manualmente las etapas básicas de un lenguaje: tokenización, parsing y evaluación. Al principio no sabía nada de nada solo quería ver como se hacía una calculadora para ver que tanto había avanzado en mi aprendizaje (Estaba practicando funciones antes de empezar con la calculadora, así de básico es mi nivel, por lo menos si tomo como referencia los libros que leo que son de nivel básico) y terminé descubriendo como en verdad funciona internamente una calculadora.

Qué hace

El programa recibe una expresión matemática escrita como texto y:

1. La tokeniza (lexer)
2. Construye un árbol sintáctico abstracto (parser recursivo)
3. Evalúa el árbol (evaluator)

Ejemplo:

2+3\*4

Primero se convierte en tokens:

[2, '+', 3, '*', 4]

Luego en un AST:

    +

/ \
 2 \*
/ \
 3 4

Finalmente produce:

14

Características actuales

- Suma, resta, multiplicación y división
- Precedencia de operadores
- Evaluación basada en AST
- Parser recursive descent

Objetivo del proyecto

Hacer una calculadora o también puede ser: Aprender cómo funcionan internamente los intérpretes y compiladores construyéndolos sin usar "eval()" ni librerías externas. Pero eso solo es secundario, yo solo empecé por una calculadora

Cada commit representa una etapa del desarrollo:

- evaluador binario (De ahí el nombre "Pendeja", porque sí le daban más de dos números se confundía)
- lexer
- parser incorrecto
- parser con precedencia
- parser recursivo
- evaluador recursivo->habilidad para calcular (atual)

Cómo ejecutar

python calculadora.py

Luego escribir una expresión:

calcula: 2+3\*4 o lo que sea, no pongan cosas que no sean números o se crasheará, todavia no sé manejar errores

Próximos pasos

- Operadores unarios
- Potencias
- Funciones matemáticas
- Variables
