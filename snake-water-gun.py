# Creating a snake water gun
import random
games=5
points=0
draw=0
for i in range(0,25):
    print('**',end='')
print('')
print('Welcome to Snake,Water,Gun Game\n')
for i in range(0,25):
    print('**',end='')
print('')
# creating functions to print choice of comp
def cChoice():
    if(compChoice==1):
        print('Computer chose Snake\n')
    elif(compChoice==2):
        print('Computer chose Water\n')
    else:
        print('Computer chose Gun\n')
while(games>0):
    compChoice=random.randint(1, 3)
    print('Choose any one of the following:')
    print('1.Snake\n2.Water\n3.Gun')
    choice=int(input())
    # draw conditions
    if(choice==1 and compChoice==1):
        print("It's a draw")
        cChoice()
        draw=draw+1
    elif(choice==2 and compChoice==2):
        print("It's a draw")
        cChoice()
        draw=draw+1
    elif(choice==3 and compChoice==3):
        print("It's a draw")
        cChoice()
        draw=draw+1
    # winning conditions
    elif(choice==1 and compChoice==2):
        print("You won")
        cChoice()
        points=points+1
    elif(choice==2 and compChoice==3):
        print("You won")
        cChoice()
        points=points+1
    elif(choice==3 and compChoice==1):
        print("You won")
        cChoice()
        points=points+1
    # losing conditions
    else:
        print('Sorry You lost')
        cChoice()
    games=games-1

print('The scores are as follows')
for i in range(0,25):
    print('-',end='')
print('')
print('You won:',points)
print('Computer won',5-points-draw)
print('Draw Matches',draw)
for i in range(0,25):
    print('-',end='')