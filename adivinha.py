# jogo adaptado por mim do site
#https://pt.wikibooks.org/wiki/Matem%C3%A1tica_divertida/Um_truque_de_adivinha%C3%A7%C3%A3o

def resp():
    resp = input(f'Resposta esta nesta tabela? [S/N] ').upper()
    if resp == 'S':
        return 'S'
    elif resp == 'N':            
        return 'N'   
    else:
        print(f'Resposta inválida, tente de novo...')

'----------------------------------------------------------------------'    
from time import sleep

t1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
t2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27 ,30, 31]
t3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
t4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
t5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
while True:
    print(50*'-')
    print(10*'=','Jogo de adivinhação !!!!!',10*'=')
    print(50*'-')
    print(10*'=','Escolha um número de 1 a 31',10*'=')
    print(50*'-')
    print(f'..............Te dou alguns segundos...........')
    sleep(2)
    print()
    print('Veja as tabelas a seguir:')
    print()
    adv = 0
    print(t1)
    r =resp()
    if r == 'S':
        adv += 1
        print(t2)
        r = resp()
        if r == 'S':
            adv += 2 
            print(t3)
            r = resp()
        else:
            r == 'N'
            print(t3)
            r = resp()
        if r == 'S':
            adv += 4
            print(t4)
            r = resp()
        else:
            r == 'N'    
            print(t4)
            r = resp()
        if r == 'S':
            adv += 8
            print(t5)
            r = resp()
        else:
            r == 'N'    
            print(t5)
            r = resp()
        if r == 'S':
            adv += 16
            print(f'Seu numero:',adv)
        else:
            r == 'N'
            print(f'Seu numero:',adv)
            
            
    else:
        r == 'N'
        print(t2)
        r = resp()
        if r == 'S':
            adv += 2 
            print(t3)
            r = resp()
        else:
            r == 'N'
            print(t3)
            r = resp()
        if r == 'S':
            adv += 4
            print(t4)
            r = resp()
        else:
            r == 'N'    
            adv += 0
            print(t4)
            r = resp()
        if r == 'S':
            adv += 8
            print(t5)
            r = resp()
        else:
            r == 'N'    
            print(t5)
            r = resp()
        if r == 'S':
            adv += 16
            print(f'Seu numero:',adv)
        else:
            r == 'N'
            print(f'Seu numero:',adv)
    
    C = str(input('Deseja tentar de novo? [S/N]: ')).upper()
                       
    if C == 'S':
           True
    elif C != 'S' and C != 'N':
        print('Opção invalida!!!!')
        sleep(1)
        print(' Mas vamos de novo...')
        Exception
    else:
        C == 'N'
        print()
        print(3*'*','Obrigado por jogar, foi divertido!!!!',3*'*')
        print()
        break
    
