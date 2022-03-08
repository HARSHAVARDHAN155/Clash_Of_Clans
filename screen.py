
import struct
import numpy as np
from zmq import HEARTBEAT_IVL

from color import *


class Screen:
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._board = np.array([[''for j in range(self._width)]
                               for i in range(self._height)], dtype='object')
        print("\033[2J")  # CLAERING SCREEN

    def clean(self):
        self._board = np.array([[''for j in range(self._width)]
                               for i in range(self._height)], dtype='object')

        # set screen to begining
        print("\033[0;0H")
        for i in range(self._height):
            for j in range(self._width):
                print(self._board[i][j], end='')
            print(" ")

    def render_screen(self):
        # set cursor to beginning
        print("\033[0;0H")

        for i in range(self._height):
            for j in range(self._width):
                print(self._board[i][j], end='')
            print("")

    def place_object(self, obj):
        print("\033[0;0H")
        pos, size, height, width, maxsize,health_val = obj.get_dimension()
        structure = obj.get_structure()
        health = obj.get_health()
        # print(height,width,pos[0],pos[1],size[0],size[1],maxsize[0],maxsize[1])
        if(self._board[pos[1]][pos[0]+size[1]]!=' '):
            pos[0]=pos[0]-3
        if(self._board[pos[1]+size[0]][pos[0]]!=' '):
            pos[1]=pos[1]-1
        if(self._board[pos[1]][pos[0]-1]!=' '):
            pos[0]=pos[0]+2
        if(self._board[pos[1]-1][pos[0]]!=' '):
            pos[1]=pos[1]+1.5
        
        for i in range(pos[1], pos[1]+size[0]):
            for j in range(pos[0], pos[0]+size[1]):
                if(self._board[i][j] == ' '):
                    self._board[i][j] = structure[i-pos[1]][j-pos[0]]

        # pos[1]=pos[1]-2
        for i in range(pos[1], pos[1]+1):
            for j in range(pos[0], pos[0]+size[1]):
                    self._board[i][j] = health[i-pos[1]][j-pos[0]]
                    
                    
    def reset_screen(self):
        # Adjust and start a screen/.,
        self._board = np.array([[' ' for j in range(self._width)]
                               for i in range(self._height)], dtype='object')

        # Adjust the constant background
        # setup walls
        for i in range(self._height):
            for j in range(self._width):
                # Top wall and bottom
                if(i == 0 or i == self._height-1):
                    self._board[i][j] = bg.green+' '+reset
                # Left and Right Wall
                elif(j == 1 or j == self._width-1):
                    self._board[i][j] = bg.green+' '+reset
