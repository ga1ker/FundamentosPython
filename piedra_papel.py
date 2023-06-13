#elección aleatoria Maq
import random

#function randint(max,min)
rand_int= random.randint(1,3)
if rand_int==1:
    choice_maq='Piedra'
elif rand_int==2:
    choice_maq='Papel'
else:
    choice_maq='Tijeras'

#elección usuario
choice_text='''
Escriba una de las siguientes opciones:
    Piedra
    Papel
    Tijeras
'''
choice_user=input(choice_text)
#Impresion de opciones
print('Usuario elegigió->', choice_user)
print('Maquina elegigió->', choice_maq)

#ganador!
if choice_maq == choice_user:
    print("Es un empate")
else:
    if choice_maq=='Piedra' and choice_user=='Papel':
        print('Gana Usuario')
    elif choice_maq=='Piedra' and choice_user=='Tijeras':
        print('Gana maquina')
    elif choice_maq=='Papel' and choice_user=='Tijeras':
        print('Gana usuario')
    elif choice_maq=='Papel' and choice_user=='Piedra':
        print('Gana maquina')
    elif choice_maq=='Tijeras' and choice_user=='Piedra':
        print('gana Usuario')
    else:
        print('gana usuario')