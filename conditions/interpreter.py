expression = input("Expression: ")
A,B,C = expression.split(" ")
A = float(A)
C = float(C)

if B == "+":
    result = A + C
elif B == "-":
    result = A - C
elif B == "*":
    result = A * C
elif B == "/":
    result = A / C
else:
    result = "Operador inválido."
print(f"{result:.1f}")





