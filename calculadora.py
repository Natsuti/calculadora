todo = input("calcula: ")
tokens = []
resultado = None
buffer = ""
# Se separa todo, la verdad es bien dificil separar los procesos, en esta caso primero la parte de la tokenizacion(lexer).
for i in range(len(todo)):
    if todo[i] >= "0" and todo[i] <= "9":
        buffer += todo[i]
        print(f"1. buffer: {buffer}")
    elif todo[i] in "+-*/":
        if buffer:
            tokens.append(buffer)
        tokens.append(todo[i])
        print(f"2. buffer: {buffer}, tokens: {tokens}")
        buffer = ""
tokens.append(buffer)
print(f"3. buffer: {buffer}, tokens: {tokens}")

# Si un algoritmo dependede de indices estables, la estructura no puede mutar, la estructura no puede mutar.
# Si la estructura muta, el indice debe estar bajo control explicito
# Ahora toca el parser(transforma los tokens en algo o eso creo, no importa la verdad, solo se que hace en codigo)
# Esto es un problema
for i in range(len(tokens)):
    if resultado:
        if tokens[i] in "+-*/":
            if tokens[i] == "+":
                resultado += int(tokens[i + 1])
            elif tokens[i] == "-":
                resultado -= int(tokens[i + 1])
            elif tokens[i] == "*":
                resultado *= int(tokens[i + 1])
            elif tokens[i] == "/":
                resultado /= int(tokens[i + 1])
    else:
        if tokens[i] in "+-*/":
            if tokens[i] == "+":
                resultado = int(tokens[i - 1]) + int(tokens[i + 1])
            elif tokens[i] == "-":
                resultado = int(tokens[i - 1]) - int(tokens[i + 1])
            elif tokens[i] == "*":
                resultado = int(tokens[i - 1]) * int(tokens[i + 1])
            elif tokens[i] == "/":
                resultado = int(tokens[i - 1]) / int(tokens[i + 1])
print(resultado)
