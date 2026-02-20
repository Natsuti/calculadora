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
        if token[0] == "num":
            pas += 1
            return {"Number": token[1]}
        if token[1] == "(":
            pas += 1
            node = expr(tokens)
            if tokens[pas][1] != ")":
                raise Exception("Parentesis no cerrado")
            pas += 1
            return node

    return {"body": expr(li)}
