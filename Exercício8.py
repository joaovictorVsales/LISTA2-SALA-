A= int(input())
B= int(input())
C= int(input())

print('Números divisíveis por 2 e 3')

if(A % 2 == 0) and (A % 3 == 0):
    print(A)

elif(B % 2 == 0) and (B % 3 == 0):
    print(B)

elif(C % 2 == 0) and (C % 3 == 0):
    print(C)

else:
    print('Nenhum número é divisivel:(')