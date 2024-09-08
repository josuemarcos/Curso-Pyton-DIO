#Exemplo utilizando iterável
vogais = "AEIOU"
palavra_do_usuario = input("Digite uma palavra para procurarmos vogais!")

for letra in palavra_do_usuario:
    if letra.upper() in vogais:
        print(letra, end = " ")
        

#Exemplo utilizando a função Range

for numero in range(0, 51, 5):
    print(numero, end = " ")

#Exemplo utilizando While
numero = 0

while numero != 10:
    numero = int(input("Digite um número "))
    if numero == 5:
        break
    print(numero)

