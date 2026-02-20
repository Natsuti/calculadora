def tokenizar(s):
    buffer = ""
    tokens = []
    for i in s:
        if i >= "0" and i <= "9":
            buffer += i
        elif i in "+-*/()":
            if buffer:
                tokens.append(("num", int(buffer)))
                buffer = ""
            if i in "+-*/":
                tokens.append(("op", i))
            else:
                tokens.append(("paren", i))
    if buffer:
        tokens.append(("num", int(buffer)))
    return tokens
