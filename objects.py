from wsgiref.handlers import read_environ
import numpy as np
import time
from color import *
import os


class Item:
    def __init__(self, pos, size, height, width, maxsize,health_val):
        self._pos = np.array(pos)
        self._size = np.array(size)
        self._height = height
        self._width = width
        self._maxsize = np.array(maxsize)
        self._structure = np.array([[]])
        self._health = np.array([[]])
        self._health_val = health_val

    def get_dimension(self):
        return [self._pos, self._size, self._height, self._width, self._maxsize,self._health_val]

    def get_structure(self):
        return self._structure
    def get_health(self):
        return self._health

class Town(Item):
    def __init__(self, pos, size, height, width, maxsize,health_val):
        super().__init__(pos, size, height, width, maxsize,health_val)
        # self._structure = np.array([[bg.yellow+' '+reset for j in range(self._size[1])]for i in range(size[0])],dtype='object')

        # var = []
        # for i in range(size[0]):
        #     temp=[]
        #     for j in range(self._size[1]):
        #         temp.append(bg.yellow+' '+reset)
        #     var.append(temp)

        # self._structure =np.array(var,dtype='object')

        self._structure = np.zeros(
            (self._size[0], self._size[1]), dtype='object')
        for i in range(size[0]):
            for j in range(size[1]):
                self._structure[i][j] = bg.blue +' '+reset
                if(j == 3 and i != 0 and i != size[0]-1):
                    self._structure[i][j] = bg.black+'  '+reset+bold
                    self._structure[i][j] = 'T'+reset+bold
        
        self._health = np.zeros(
            (int(2), self._size[1]), dtype='object')
        for i in range(2):
            for j in range(size[1]):
                if(self._health_val>50):
                    self._health[i][j] = bg.green+' '+reset
                elif (self._health_val>20):
                    self._health[i][j] = bg.yellow+' '+reset
                else:
                    self._health[i][j] =bg.red+' '+reset
                    
               


class King(Item):
    def __init__(self, pos, size, height, width, maxsize,health_val):
        super().__init__(pos, size, height, width, maxsize,health_val)

        self._structure = np.zeros(
            (self._size[0], self._size[1]), dtype='object')
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                self._structure[i][j] = bg.red+' '+reset
                if(j == 2 and i != 0 and i != size[0]-1):
                    self._structure[i][j] = bg.black+'  '+reset
                    self._structure[i][j] = 'K'+reset+bold
        self._health = np.zeros(
            (int(2), self._size[1]), dtype='object')
        for i in range(2):
            for j in range(size[1]):
                if(self._health_val>50):
                    self._health[i][j] = bg.green+' '+reset
                elif (self._health_val>20):
                    self._health[i][j] = bg.yellow+' '+reset
                else:
                    self._health[i][j] =bg.red+' '+reset

    def move(self, ch):
        if(ch == 'd'):
            self._pos[0] = self._pos[0]+2
            if(self._pos[0]+self._size[0] >= self._maxsize[0]-1):
                self._pos[0] = self._maxsize[0] - self._size[0] - 3
        elif(ch == 'a'):
            self._pos[0] = self._pos[0]-2
            if(self._pos[0] <= 4):
                self._pos[0] = 4
        elif(ch == 'w'):
            self._pos[1] = self._pos[1]-2
            if(self._pos[1] <= 4):
                self._pos[1] = 1
        elif(ch == 's'):
            self._pos[1] = self._pos[1]+2
            if(self._pos[1]+self._size[1] >= self._maxsize[1]-1):
                self._pos[1] = self._maxsize[1] - self._size[1] + 1
    def update_health(self):
        self._health_val = self._health_val - 20

class Hut(Item):
    def __init__(self, pos, size, height, width, maxsize,health_val):
        super().__init__(pos, size, height, width, maxsize,health_val)

        self._structure = np.zeros(
            (self._size[0], self._size[1]), dtype='object')
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                self._structure[i][j] = bg.cyan+' '+reset
                if(j == 2 and i != 0 and i != size[0]-1):
                    self._structure[i][j] = bg.black+'  '+reset
                    self._structure[i][j] = 'H'+reset+bold
        self._health = np.zeros(
            (int(2), self._size[1]), dtype='object')
        for i in range(2):
            for j in range(size[1]):
                if(self._health_val>50):
                    self._health[i][j] = bg.green+' '+reset
                elif (self._health_val>20):
                    self._health[i][j] = bg.yellow+' '+reset
                else:
                    self._health[i][j] =bg.red+' '+reset
    
class Cannon(Item):
    def __init__(self, pos, size, height, width, maxsize,health_val):
        super().__init__(pos, size, height, width, maxsize,health_val)

        self._structure = np.zeros(
            (self._size[0], self._size[1]), dtype='object')
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                self._structure[i][j] = bg.purple+' '+reset
                if(j == 2 and i != 0 and i != size[0]-1):
                    self._structure[i][j] = bg.black+'  '+reset
                    self._structure[i][j] = 'C'+reset+bold
        self._health = np.zeros(
            (int(2), self._size[1]), dtype='object')
        for i in range(2):
            for j in range(size[1]):
                if(self._health_val>50):
                    self._health[i][j] = bg.green+' '+reset
                elif (self._health_val>20):
                    self._health[i][j] = bg.yellow+' '+reset
                else:
                    self._health[i][j] =bg.red+' '+reset
