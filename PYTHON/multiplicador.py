
for numerador in range(10):
    print("tabuada do número", numerador+1)
    for multiplicador in range(10):
        print((numerador+1)*(multiplicador+1))

print("-"*100)

varA=3
varB=0
for num in range(varA):
    varB+=num**2
    print(varB)

cont=0
soma=0
while cont<=12:
    soma+=cont
    cont+=2
print('cont=', cont)
print('soma=', soma)
