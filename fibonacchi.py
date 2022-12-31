

# Serie de Fibonacci

fibonacci = [0, 1]


cont = 0
while cont < 20:

    varIndex1 = fibonacci[-1]
    varIndex2 = fibonacci[-2]
    add = varIndex1 + varIndex2
    fibonacci.append(add)

    cont += 1

print(fibonacci)



