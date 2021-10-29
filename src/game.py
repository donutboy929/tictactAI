from player import *
from evaluator import *

class Game():
    def __init__(self, playerX=Player("X"), playerO=Player("O")):
        self.winner = None
        self.playerX = playerX
        self.playerO = playerO
        self.board = Board()
        self.__turn_counter = 0
        self.__current_player = playerX

    def get_turn(self) -> int:
        return self.__turn_counter

    def get_current_player(self) -> Player:
        return self.__current_player

    def player_turn(self, position_index) -> bool:
        self.__current_player = self.playerX if self.__turn_counter % 2 == 0 else self.playerO
        successfully_place_symbol = self.__current_player.place_symbol_on_board(position_index, self.board)
        self.__turn_counter += 1 if successfully_place_symbol else 0
        return successfully_place_symbol

    def check_row_win(self) -> str:
        return check_row_win(self.board.view_board())

    def check_col_win(self) -> str:
        return check_col_win(self.board.view_board())

    def check_diagonal_win(self) -> str:
        return check_diagonal_win(self.board.view_board())

    
    
