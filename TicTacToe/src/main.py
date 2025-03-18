
'''main.py'''

import pygame
import pygame.locals

import tictactoe

def main():
    '''
    ### TIC TAC TOE !! ###

    This is a simple game of Tic Tac Toe.
    The game is played on a 3x3 grid.

    The first player is X and the second player is O.
    The players take turns to place their mark on the grid.
    The first player to get 3 of their marks in a row is the winner.
    If the grid is full and no player has won, the game is a tie.
    '''

    pygame.init()
    screen = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("TIC TAC TOE")

    game_loop = tictactoe.GameLoop(screen)
    game_loop.run()


if __name__ == "__main__":
    main()
