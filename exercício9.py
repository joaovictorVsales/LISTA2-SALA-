A= int(input())
B= int(input())


print('Números divisíveis por 4 e 5')

if(A % 4 == 0) or (A % 5 == 0):
    print(A)

elif(B % 4 == 0) or (B % 5 == 0):
    print(B)


else:
    print('Nenhum número é divisivel')