import random
while True :
    print('Play rock-paper-scissors 0--rock , 1--paper , 2--scissors ')
    player = int(input('Please show your answer : '))
    computer = random.randint(0,2)
    print(computer)
    
    if (player == 0) and (computer == 2) or (player == 2) and (computer == 1) or (player == 1) and (computer == 0):
        print('Player Win!!!\n')
    elif(computer == 2) and (player == 1) or (computer == 1) and (player == 0) or (computer == 0) and (player == 2):
        print('Player Lose\n')
    else:
        print('Draw\n')
