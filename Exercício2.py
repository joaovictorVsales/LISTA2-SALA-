prova1= float(input('Nota da prova 1: '))
prova2= float(input('Nota da prova 2: '))
prova3= float(input('Nota da prova 3: '))


Nota= (prova1 + prova2 + prova3)/3


if (Nota < 6):

    print('REPROVADO! faça recuperação {:.2f} ' .format(Nota))

else:
    print( 'APROVADO! {:.2f} ' .format(Nota) )

rec= float(input('Nota da rec: '))

if (rec >=5):
    print('APROVADO!', rec)

else:
    print('REPROVADO!', rec)
