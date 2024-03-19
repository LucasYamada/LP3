compras = int(input("Digite o numero de compras:"))
valorf = 0

for i in range(0,compras):
    valori = float(input("Digite o valor da compra:"))
    if(valori >= 0.01 and valori < 10.0):
        valorf = valori - valori/25
    elif(valori >= 10 and valori < 100):
        valorf = valori - valori/20
    elif(valori >= 100 and valori < 500):
        valorf = valori - valori/10
    else:
        valorf = valori - valori*0.15

    print("O preco com desconto é:",valorf)

print("Obrigado, volte sempre!")
