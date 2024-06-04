def media (valores):
    return sum(valores)/len(valores)

def minimo(valores):
    res = valores[0]
    for i in valores:
        if i < res:
            res = i
    return res

def maximo(valores):
    res = valores[0]
    for i in valores:
        if i > res:
            res = i
    return res
