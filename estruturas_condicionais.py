
maior_idade = 18
idade = int(input("digite sua idade: "))
if idade >= maior_idade: 
    print("Parabéns, você pode tirar sua CNH!")
else:
    print(f"Infelizmente você ainda pode tirar sua CNH! Você precisa esperar {18 - idade} anos para tirar sua CNH!")
