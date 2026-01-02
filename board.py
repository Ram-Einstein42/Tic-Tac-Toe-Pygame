import pygame
from square import *

class Board:
    def __init__(self):
        self.board = [[Square((0,0)), Square((200,0)),Square((400,0))],
                      [Square((0,200)),Square((200,200)), Square((400,200))],
                      [Square((0,400)),Square((200,400)), Square((400,400))]]