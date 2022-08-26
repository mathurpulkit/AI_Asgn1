# defines the general class of a board with n*n tiles
# we will use 0 to denote empty tile
import copy
import random
from time import time
random.seed(time)

class ntile:
    def __init__(self, n: int, initial_state = None):
        self.n = n
        if initial_state is None: # if no initial state is provided, generate a solved board
            self.board = [[i for i in range(self.n)] for j in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    self.board[i][j] += i*self.n + 1
            self.board[self.n-1][self.n-1] = 0
        elif isinstance(initial_state, ntile):
            self.board = copy.deepcopy(initial_state.board)
        elif isinstance(initial_state, list):
            self.board = copy.deepcopy(initial_state)
        else: # generate a random board
            self.board = [[i for i in range(self.n)] for j in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    self.board[i][j] += i*self.n + 1
            self.board[self.n-1][self.n-1] = 0
            for i in range(self.n*self.n):
                rand_i = random.randint(0, self.n-1)
                rand_j = random.randint(0, self.n-1)
                self.board[rand_i][rand_j], self.board[self.n-1][self.n-1] = self.board[self.n-1][self.n-1], self.board[rand_i][rand_j]
        return

    def move(self, move: str):
        # convention is that we are moving the blank space
        # returns False if no valid move is performed, else returns True
        # find 0 in the board
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    zero_i = i
                    zero_j = j
                    break
        if move == 'U':
            if zero_i == 0:
                return False
            self.board[zero_i][zero_j], self.board[zero_i-1][zero_j] = self.board[zero_i-1][zero_j], self.board[zero_i][zero_j]
            return True
        elif move == 'D':
            if zero_i == self.n-1:
                return False
            self.board[zero_i][zero_j], self.board[zero_i+1][zero_j] = self.board[zero_i+1][zero_j], self.board[zero_i][zero_j]
            return True
        elif move == 'L':
            if zero_j == 0:
                return False
            self.board[zero_i][zero_j], self.board[zero_i][zero_j-1] = self.board[zero_i][zero_j-1], self.board[zero_i][zero_j]
            return True
        elif move == 'R':
            if zero_j == self.n-1:
                return False
            self.board[zero_i][zero_j], self.board[zero_i][zero_j+1] = self.board[zero_i][zero_j+1], self.board[zero_i][zero_j]
            return True
        return False

    def newBoardMove(self, move: str, prune: bool = False):
        # creates a duplicate of the board and performs the move on the duplicate, returns the duplicate
        new_board = ntile(self.n, self.board)
        new_board.move(move)
        if prune:
            if new_board.board == self.board:
                return None
        return new_board

    def is_solved(self):
        for i in range(self.n-1):
            for j in range(self.n):
                if self.board[i][j] != i*self.n + j + 1:
                    return False
        for j in range(self.n-1):
            if self.board[self.n-1][j] != (self.n-1)*self.n + j + 1:
                return False
        if self.board[self.n-1][self.n-1] != 0:
            return False
        return True

    