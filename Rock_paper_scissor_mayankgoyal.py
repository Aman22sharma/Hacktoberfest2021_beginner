"""
Name : Rock Paper Scissor Game
Author : [Mayank Goyal) [https://github.com/mayankgoyal-13]
"""

import random

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

def judge(player, computer):
    # comparison of player and computer
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')
print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

if validate(player_hand):
    # the computer chooses a random value and each value is assigned to a hand
    computer_hand = random.randint(0, 2)
    print_hand(player_hand, player_name)
    print_hand(computer_hand, 'Computer')
    result = judge(player_hand, computer_hand)     # judge function is called
    print('Result: ' + result)
else:
    print('You entered an invalid option')
