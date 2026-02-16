todo = input("calcula: ")
tokens = []
resultado = 0
buffer = ""
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
