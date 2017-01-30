'''
Created on Jan 29, 2017

@author: saldivar
'''
import os
from itertools import cycle

board = list(map(lambda x: '-', list(range(9))))
player = ['X', 'O']
player_next = cycle(player)

# Uncomment for console
clear = lambda: os.system("clear")

def print_board():
    for p in reversed(range(0,9,3)):
        print(board[p] + ' ' + board[p + 1] + ' ' + board[p + 2])
        
def draw_player_option(player_option, number):
    if check_free_space(number):
        board[number - 1] = player_option
        return True
    else:
        return False 

def reset_board():
    global board
    board = list(map(lambda x: '-', list(range(9))))
   
def is_full():
    for i in board:
        if i == '-':
            return False
    else:
        return True   

def check_free_space(number):
    if board[number - 1] == '-':
        return True
    else:
        return False

def check_win():
    
    # Horizontal Check
    for p in range(0,9,3):
        if board[p] == board[p + 1] == board[p + 2] and board[p] != '-':
            return True
    
    # Vertical Check    
    for p in range(3):
        if board[p] == board[p + 3] == board[p + 6] and board[p] != '-':
            return True
    
    # Horizontal Check
    if (board[0] == board[4] == board[8] and board[0] != '-') or (board[2] == board[4] == board[6] and board[2] != '-'):
        return True

    return False

def input_number():
    
    while True:
        try:
            number = int(input("Input a number between 1 and 9 on the key pad: "))
            if number in range(1,10):
                break
            else:
                print('Number not in range')
        except:
            print ('Not a number')
    return number

def play_again():
    restart = input('Play again? Y or N: ')
    if restart in ('Y','y'):
        return True
    elif restart in ('N','n'):
        return False
    else:
        play_again()
            
def display_turn(player):
    print('Player ' + player)
            

def start_game():
    
    reset_board()
    while not check_win() and not is_full():
        clear()
        print_board()
        player = next(player_next)
        display_turn(player)
        number = input_number()
        while not draw_player_option(player, number):
            number = input_number()
    else:
        print_board()
        if check_win():
            print('Player ' + player + ' win')
        elif is_full():
            print('Board is Full')
        if play_again():
            start_game()

start_game()