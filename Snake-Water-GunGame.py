from random import randint

while True:
    t = ['Snake', 'Water', 'Gun']
    computer_choice = randint(0, 2)
    
    print("Enter:")
    print("0 for Snake")
    print("1 for Water")
    print("2 for Gun")
    print("99 to quit")
    
    player_choice = int(input('Your choice: '))
    
    if player_choice == 99:
        break
    
    if player_choice == computer_choice:
        print('Tie!')
    elif player_choice == 0:
        if computer_choice == 1:
            print(f'You Win, Computer had {t[1]}')
        else:
            print(f'You Lose, Computer had {t[2]}')
    elif player_choice == 1:
        if computer_choice == 0:
            print(f'You Lose, Computer had {t[0]}')
        else:
            print(f'You Win, Computer had {t[2]}')
    elif player_choice == 2:
        if computer_choice == 0:
            print(f'You Win, Computer had {t[0]}')
        else:
            print(f'You Lose, Computer had {t[1]}')
    else:
        print("Invalid choice. Please choose 0, 1, 2, or 99 to quit.")
