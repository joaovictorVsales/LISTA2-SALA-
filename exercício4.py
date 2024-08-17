a= int(input('A= '))
b= int(input('B= '))
c= int(input('C= '))

if(a<b+c) and (b<a+c) and (c<b+a):
    print('Triangulo equilátero')


elif(a==b!=c) or (a==c!=b) or (b==c!=a):
    print('Triangulo isósceles')


elif(a!=b!=c):
    print('Triangulo escaleno')

else:
    print('Não é um triangulo')





    
