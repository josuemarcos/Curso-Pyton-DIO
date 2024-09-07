
maior_idade = 18
idade_especial = 12

idade = int(input("digite sua idade: "))
if idade >= maior_idade: 
    print("Parabéns, você pode tirar sua CNH!")

elif idade == 12:
    print(f"Você pode fazer as aulas teóricas da CNH! mas só poderá tirar sua CNH em {maior_idade - idade}" )
else:
    print(f"Infelizmente você ainda pode tirar sua CNH! Você precisa esperar {18 - idade} anos para tirar sua CNH!")


maior_de_idade = "é maior de idade" if idade >= 18 else "É menor de idade"

print(maior_de_idade)