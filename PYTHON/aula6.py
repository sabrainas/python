#estrutura if

idade=int(input("digite sua idade: "))

if idade>18:
    print("entrada liberada")
elif idade ==18:
        print("idade permitida")
else:
        print("entrada NEGADA")

#exercício

numero=int(input("digite um numero: "))

if numero>0:
    print("positivo")
elif numero==0:
    print("neutro")
else:
    print("negativo")

#exercicio 2

lado1=int(input("medida 1: "))
lado2=int(input("medida 2: "))
lado3=int(input("medida 3: "))

if lado1==lado2==lado3:
    print("triângulo equilátero")
elif lado1==lado2!=lado3 or lado1!=lado2==lado3 or lado1==lado3!=lado2:
    print("triângulo isósceles")
else:
    print("triângulo escaleno")
