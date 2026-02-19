def pedir():
    return input("calcula: ")


def tokenizar(s):
    buffer = ""
    tokens = []
    for i in s:
        if i >= "0" and i <= "9":
            buffer += i
        elif i in "+-*/":
            if buffer:
                tokens.append(("num", int(buffer)))
                buffer = ""
            tokens.append(("op", i))
    if buffer:
        tokens.append(("num", int(buffer)))
    return tokens


def parsear(li):
    pas = 0

    def expr(tokens):
        nonlocal pas
        left = term(tokens)
        while pas < len(tokens) and tokens[pas][0] == "op" and tokens[pas][1] in "+-":
            op = tokens[pas][1]
            pas += 1
            right = term(tokens)
            left = {"BinOp": {"left": left, "op": op, "right": right}}
        return left

    def term(tokens):
        nonlocal pas
        left = factor(tokens)
        while pas < len(tokens) and tokens[pas][0] == "op" and tokens[pas][1] in "*/":
            op = tokens[pas][1]
            pas += 1
            right = factor(tokens)
            left = {"BinOp": {"left": left, "op": op, "right": right}}
        return left

    def factor(tokens):
        nonlocal pas
        token = tokens[pas]
        pas += 1
        return {"Number": token[1]}

    return {"body": expr(li)}


import json

ast = parsear(tokenizar("2+3*4"))
print(json.dumps(ast, indent=4))
