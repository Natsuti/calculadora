from tokens import *
from parser import *


def pedir():
    return input("calcula: ")


def evaluate(nodo):
    if "body" in nodo:
        nodo = nodo["body"]

    if "Number" in nodo:
        return nodo["Number"]
    elif "BinOp" in nodo:
        nodo = nodo["BinOp"]
        left = evaluate(nodo["left"])
        op = nodo["op"]
        right = evaluate(nodo["right"])
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right


print(
    "Esto es una calculadora integrada con lexer, parser y un evaluador(la calculadora), para quitar: quit"
)
while True:
    p = pedir()
    if p == "quit":
        break
    t = tokenizar(p)
    pa = parsear(t)
    print(evaluate(pa))
