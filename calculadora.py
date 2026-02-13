todo = input("calcula: ")
num1 = ""
operador = ""
num2 = ""
resultado = 0
buffer = ""
for i in range(len(todo)):
    print(f"todo[i]: {todo[i]}")
    if todo[i] != " ":
        buffer += todo[i]
        print(f"buffer: {buffer}")
    elif todo[i] == " " and num1 == "":
        num1 = buffer
        print(f"num1: {num1}, buffer: {buffer}")
        buffer = ""
    elif todo[i] == " " and operador == "":
        operador = buffer
        print(f"operador: {operador}, buffer: {buffer}")
        buffer = ""
num2 = buffer
print(f"buffer: {buffer}, num1: {num1}, operador: {operador}, num2: {num2}")
buffer = ""
if operador == "+":
    resultado = int(num1) + int(num2)
if operador == "-":
    resultado = int(num1) - int(num2)
if operador == "*":
    resultado = int(num1) * int(num2)
if operador == "/":
    resultado = int(num1) / int(num2)
print(resultado)
