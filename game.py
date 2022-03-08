from mimetypes import init
from operator import ipow
import os
import sys
import numpy as np
from color import *
from objects import Cannon, Hut, Item, King
from objects import Town
from screen import  Screen
from input import input_to
from input import Get

KEYS  = ['a','d']
class Game :
    def __init__(self):
        rows,cols = os.popen('stty size','r').read().split()
        rows = int(rows)
        cols = int(cols)
        self.ran = 1
        self._kingval = 0
        self._floor = int(0.1*(int(rows)))-4
        self._margin = int(0.4*(int(rows)))
        self._height = int(rows) - self._floor-4
        self._width = int(cols) - self._margin
        self._screen = Screen(self._height, self._width)

    def start(self):
        self._town = Town([int(self._width/2)-2,int(self._height/2) - 2],[6,8],int(1),int(3),[self._width,self._height],int(15))
        self._king = King([int(6),int(self._height/2)],[3,5],1,2,[self._width,self._height],int(100))
        self._hut1 = Hut([int(12),int(3)],[3,6],1,1,[self._width,self._height],int(100))
        self._hut2 = Hut([int((self._width/2)),int(3)],[3,6],1,1,[self._width,self._height],int(100))
        self._hut3 = Hut([int(28),int(20)],[3,6],1,1,[self._width,self._height],int(100))
        self._hut4 = Hut([int((self._width-15)),int(3)],[3,6],1,1,[self._width,self._height],int(100))
        self._hut5 = Hut([int((self._width-15)),int(20)],[3,6],1,1,[self._width,self._height],int(100))
        self._cannon1 = Cannon([int(56),int(7)],[3,5],1,1,[self._width,self._height],int(100))
        self._cannon2 = Cannon([int(120),int(23)],[3,5],1,1,[self._width,self._height],int(100))
    def placing(self):
        self._screen.place_object(self._town)
        self._screen.place_object(self._hut1)
        self._screen.place_object(self._hut2)
        self._screen.place_object(self._hut4)
        self._screen.place_object(self._hut3)
        
        self._screen.place_object(self._hut5)
        self._screen.place_object(self._cannon1)
        self._screen.place_object(self._cannon2)
        
        if(self._kingval==1):
            self._screen.place_object(self._king)
        
    
    def key_board_interrupt (self):
        get = Get()
        ch = input_to(get.__call__)
        if(ch=='q'):
            sys.exit()
        elif(ch=='k'):
            self._kingval =1
        elif ch =='d':
            self._king.move(ch)
        elif ch== 'a':
            self._king.move(ch)
        elif ch== 'w':
            self._king.move(ch)
        elif ch== 's':
            self._king.move(ch)
        
        
        
    def run(self):
        self.start()
        while True:
            self._screen.clean()
            self._screen.reset_screen()
            
            self.key_board_interrupt()
            self.placing()
            self._screen.render_screen()
        

game = Game()
game.run()