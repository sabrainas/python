#exemplo 1:
print("exemplo estrutura if")
numero=8
if numero>10:
    print("o numero é maior que 10")
else:
    print("o numero é menor que 10")


#exemplo 2:
nota1=float(input("digite sua nota: "))
nota2=float(input("digite sua nota: "))
media=(nota1+nota2)/2
print(f"sua média é: {media}")

if media>=6: 
    print("aprovado")
else:
    print("reprovado")

#exemplo 3:
idade1=int(input("digite sua idade1: "))
idade2=int(input("digite sua idade2: "))

if idade1>=18 and idade2>=18:
           print("entrada PERMITIDA")
else:
    print("entrada NEGADA")
