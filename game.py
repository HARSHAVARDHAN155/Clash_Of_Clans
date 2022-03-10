from cmath import sqrt
from mimetypes import init
from operator import ipow
import os
import sys
import numpy as np
from color import *
from objects import Cannon, Hut, Item, King, Wall
from objects import Town
from screen import Screen
from input import input_to
from input import Get

KEYS = ['a', 'd']


class Game:
    def __init__(self):
        rows, cols = os.popen('stty size', 'r').read().split()
        rows = int(rows)
        cols = int(cols)
        self.ran = 1
        self._kingval = 0
        # self._leftx =[int(self._width/2)-6,]
        # self._lefty=[int(self._height/2) - 4,int(self._height/2) - 3,int(self._height/2) - 2,int(self._height/2) - 1,int(self._height/2) ,int(self._height/2)+1,int(self._height/2)+2,int(self._height/2)+3,int(self._height/2)+4]
        # self._rightx=[int(self._height/2) - 4,int(self._height/2) - 3,int(self._height/2) - 2,int(self._height/2) - 1,int(self._height/2) ,int(self._height/2) +1,int(self._height/2) +2,int(self._height/2) +3,int(self._height/2) +4]
        self._kingattack = 0
        self._floor = int(0.1*(int(rows)))-4
        self._margin = int(0.4*(int(rows)))
        self._height = int(rows) - self._floor-4
        self._width = int(cols) - self._margin
        self._screen = Screen(self._height, self._width)
        if(rows < 32 or cols < 128):
            print("Increase Terminal Screen Size!!")
            sys.exit(0)
    
    def start(self):
        self._town = Town([int(self._width/2), (int(self._height/2))-2],
                          [3,4], int(1), 1, [self._width, self._height], int(100), 0)
        ##left wall
        self._wall_left = Wall([int(self._width/2)-3, int(self._height/2) - 5],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_left1 = Wall([int(self._width/2)-6, int(self._height/2) - 5+1],
                          [1,1], int(1), int(1), [self._width, self._height], int(100), 0)
        self._wall_left2 = Wall([int(self._width/2)-6, int(self._height/2) - 3],
                          [1,1], int(1), int(1), [self._width, self._height], int(100), 0)
        self._wall_left3 = Wall([int(self._width/2)-6, int(self._height/2) - 2],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_left4 = Wall([int(self._width/2)-6, int(self._height/2) - 1],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_left5 = Wall([int(self._width/2)-6, int(self._height/2) ],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_left6 = Wall([int(self._width/2)-6, int(self._height/2) + 1],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_left7 = Wall([int(self._width/2)-6, int(self._height/2) +2],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_left8 = Wall([int(self._width/2)-6, int(self._height/2) +3],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_left9 = Wall([int(self._width/2)-6, int(self._height/2) +4],
                          [1,1], int(1), int(1), [self._width, self._height], int(10), 0)

    
        
        self._wall_right = Wall([int(self._width/2)+6+6, int(self._height/2) - 5],
                          [1, 1], int(1), int(1), [self._width, self._height], int(10), 0)
        
        self._wall_right1 = Wall([int(self._width/2)+6+6, int(self._height/2) - 4],[1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        self._wall_right2 = Wall([int(self._width/2)+6+6, int(self._height/2) - 3],[1, 1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_right3 = Wall([int(self._width/2)+6+6, int(self._height/2) - 2],[1, 1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_right4 = Wall([int(self._width/2)+6+6, int(self._height/2) - 1],[1, 1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_right5 = Wall([int(self._width/2)+6+6, int(self._height/2) ],[1,1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_right6 = Wall([int(self._width/2)+6+6, int(self._height/2) +1],[1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        self._wall_right7 = Wall([int(self._width/2)+6+6, int(self._height/2) +2],[1, 1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_right8 = Wall([int(self._width/2)+6+6, int(self._height/2) +3],[1, 1], int(1), int(1), [self._width, self._height], int(10), 0)
        self._wall_right9 = Wall([int(self._width/2)+6+6, int(self._height/2) +4],[1, 1], int(1), int(1), [self._width, self._height], int(10), 0)
        

 
        
        
        self._wall_up = Wall([int(self._width/2)-6, int(self._height/2) - 5],  [1, 18], int(1), int(1), [self._width, self._height], int(100), 0)
        
        # self._wall_up1 = Wall([int(self._width/2)-6+2, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up2 = Wall([int(self._width/2)-6+1, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up3 = Wall([int(self._width/2)-6, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up4 = Wall([int(self._width/2)-5, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up5 = Wall([int(self._width/2)-4, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up6 = Wall([int(self._width/2)-3, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up7 = Wall([int(self._width/2)-2, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up8 = Wall([int(self._width/2)-1, int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        # self._wall_up9 = Wall([int(self._width/2), int(self._height/2) - 5], [1, 1], int(1), int(1), [self._width, self._height], int(100), 0)
        
        
        
        
        self._wall_down = Wall([int(self._width/2)-6, int(self._height/2) - 5+10],   [1, 18], int(1), int(1), [self._width, self._height], int(100), 0)
        self._king = King([int(6), int(self._height/2)], [1, 1],
                          2, 2, [self._width, self._height], int(100), 5)
        self._hut1 = Hut([int(12), int(3)], [1 , 1], 1, 1, [  self._width, self._height], int(100), 0)
        self._hut2 = Hut([int((self._width/2)), int(3)], [1 , 1],   1, 1, [self._width, self._height], int(100), 0)
        self._hut3 = Hut([int(28), int(20)],[1 , 1], 1, 1, [self._width, self._height], int(100), 0)
        self._hut4 = Hut([int((self._width-15)), int(3)], [1 , 1],    1, 1, [self._width, self._height], int(10), 0)
        self._hut5 = Hut([int((self._width-15)), int(20)],[1 , 1], 1, 1, [self._width, self._height], int(100), 0)
        self._cannon1 = Cannon([int(56), int(7)], [1 , 1], 1, 1, [ self._width, self._height], int(100), 15)
        self._cannon2 = Cannon([int(120), int(23)], [1 , 1], 1, 1, [ self._width, self._height], int(10), 15)

    def placing(self):
        self._screen.place_object(self._town)
    
        # self._screen.place_object(self._wall_left)
        self._screen.place_object(self._wall_left1)
        self._screen.place_object(self._wall_left2)
        self._screen.place_object(self._wall_left3)
        self._screen.place_object(self._wall_left4)
        self._screen.place_object(self._wall_left5)
        self._screen.place_object(self._wall_left6)
        self._screen.place_object(self._wall_left7)
        self._screen.place_object(self._wall_left8)
        self._screen.place_object(self._wall_left9)
        
        
        # self._screen.place_object(self._wall_right)
        self._screen.place_object(self._wall_right1)
        self._screen.place_object(self._wall_right2)
        self._screen.place_object(self._wall_right3)
        self._screen.place_object(self._wall_right4)
        self._screen.place_object(self._wall_right5)
        self._screen.place_object(self._wall_right6)
        self._screen.place_object(self._wall_right7)
        self._screen.place_object(self._wall_right8)
        self._screen.place_object(self._wall_right9)
        
        
        self._screen.place_object(self._wall_up)
        # self._screen.place_object(self._wall_up1)
        # self._screen.place_object(self._wall_up2)
        # self._screen.place_object(self._wall_up3)
        # self._screen.place_object(self._wall_up4)
        # self._screen.place_object(self._wall_up5)
        # self._screen.place_object(self._wall_up6)
        # self._screen.place_object(self._wall_up7)
        # self._screen.place_object(self._wall_up8)
        # self._screen.place_object(self._wall_up9)
        
        self._screen.place_object(self._wall_down)
        self._screen.place_object(self._hut1)
        self._screen.place_object(self._hut2)
        self._screen.place_object(self._hut4)
        self._screen.place_object(self._hut3)

        self._screen.place_object(self._hut5)
        self._screen.place_object(self._cannon1)
        self._screen.place_object(self._cannon2)

        if(self._kingval == 1):
            self._screen.place_object(self._king)

    def king_attack(self):
        pos, size, height, width, maxsize, health_val, damage = self._king.get_dimension()
        
        print(pos[0],pos[1],"width/2:",int(self._width/2),"height/2:",int(self._height/2),"kingattack:",self._kingattack)
        # print("waal1 :",self._wall_left1)
        if((self._kingattack==0)and(pos[0]+1== int(self._width/2)) and ((pos[1]== int(self._height/2 -2)) or (pos[1]==int(self._height/2 -1)) or (pos[1]==int(self._height/2 )) or  (pos[1]==int(self._height/2 +1))) ):
            self._town.update_health(damage)
        else:
            self._kingattack=0
        if((self._kingattack==0)and(pos[0]-1-3== int(self._width/2)) and ((pos[1]== int(self._height/2 -2)) or (pos[1]==int(self._height/2 -1)) or (pos[1]==int(self._height/2 )) or  (pos[1]==int(self._height/2 +1))) ):
            self._town.update_health(damage)
        else:
            self._kingattack=0
            
        if((self._kingattack==0)and(pos[1]+3== int(self._height/2 -2)) and ( (pos[0]==int(self._width/2)) or (pos[0]==int(self._width/2)) or (pos[0]+1==int(self._width/2))  or (pos[0]+2==int(self._width/2))  or (pos[0]+3==int(self._width/2)) ) ):
            self._town.update_health(damage)
        else:
            self._kingattack=0  
        if((self._kingattack==0)and(pos[1]-4== int(self._height/2 -2)) and ( (pos[0]==int(self._width/2)) or (pos[0]+3==int(self._width/2)) or (pos[0]+4==int(self._width/2))  or (pos[0]+2==int(self._width/2))  or (pos[0]+1==int(self._width/2)) ) ):
            self._town.update_health(damage)
        else:
            self._kingattack=0   
            
            
            #huts
        if((self._kingattack==0)and(((pos[0]+2== 12) and pos[1]==3) or (pos[0]-2==12  and pos[1] == 3) or (pos[1]+2==3  and pos[0] == 12)or (pos[1]-2==3  and pos[0] == 12))):
            self._hut1.update_health(damage)
        else:
            self._kingattack=0  
        if((self._kingattack==0)and(((pos[0]+2== int((self._width/2))) and pos[1]==3) or (pos[0]-2==int((self._width/2))  and pos[1] == 3) or (pos[1]+2==3  and pos[0] == int((self._width/2)))or (pos[1]-2==3  and pos[0] == int((self._width/2))))):
            self._hut2.update_health(damage)
        else:
            self._kingattack=0 
       
        if((self._kingattack==0)and(((pos[0]+2== 28) and pos[1]==20) or (pos[0]-2==28  and pos[1] == 20) or (pos[1]+2==20  and pos[0] == 28)or (pos[1]-2==20  and pos[0] == 28))):
            self._hut3.update_health(damage)
        else:
            self._kingattack=0 
       
        if((self._kingattack==0)and(((pos[0]+2== int((self._width-15))) and pos[1]==3) or (pos[0]-2==int((self._width-15))  and pos[1] == 3) or (pos[1]+2==3  and pos[0] == int((self._width-15)))or (pos[1]-2==3  and pos[0] == int((self._width-15))))):
            self._hut4.update_health(damage)
        else:
            self._kingattack=0 
        
        if((self._kingattack==0)and(((pos[0]+2== int((self._width-15))) and pos[1]==20) or (pos[0]-2==int((self._width-15))  and pos[1] == 20) or (pos[1]+2==20  and pos[0] == int((self._width-15)))or (pos[1]-2==20  and pos[0] == int((self._width-15))))):
            self._hut5.update_health(damage)
        else:
            self._kingattack=0 
        
          ## cannons
          
        if((self._kingattack==0)and(((pos[0]+2== 56) and pos[1]==7) or (pos[0]-2==56  and pos[1] == 7) or (pos[1]+2==7  and pos[0] == 56)or (pos[1]-2==7 and pos[0] == 56))):
            self._cannon1.update_health(damage)
        else:
            self._kingattack=0   
        if((self._kingattack==0)and(((pos[0]+2== 120) and pos[1]==23) or (pos[0]-2==120  and pos[1] == 23) or (pos[1]+2==23  and pos[0] == 120)or (pos[1]-2==23  and pos[0] == 120))):
            self._cannon2.update_health(damage)
        else:
            self._kingattack=0  

        ##Walls
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 5+1)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 5+1))):
            self._wall_left1.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 3)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 3))):
            self._wall_left2.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 2)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 2))):
            self._wall_left3.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 1)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) - 1))):
            self._wall_left4.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) )) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) ))):
            self._wall_left5.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +1)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +1))):
            self._wall_left6.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +2)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +2))):
            self._wall_left7.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +3)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +3))):
            self._wall_left8.update_health(damage)
        if((pos[0]+1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +4)) or (pos[0]-1==int(self._width/2)-6)and (pos[1]==(int(self._height/2) +4))):
            self._wall_left9.update_health(damage)
        
         ##right
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 5+1)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 5+1))):
            self._wall_right1.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 3)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 3))):
            self._wall_right2.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 2)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 2))):
            self._wall_right3.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 1)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) - 1))):
           self._wall_right4.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) )) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) ))):
            self._wall_right5.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +1)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +1))):
           self._wall_right6.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +2)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +2))):
            self._wall_right7.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +3)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +3))):
            self._wall_right8.update_health(damage)
        if((pos[0]+1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +4)) or (pos[0]-1==int(self._width/2)+12)and (pos[1]==(int(self._height/2) +4))):
            self._wall_right9.update_health(damage)
            
        ##up
        
        if(pos[0]<=(int(self._width/2)-6+18)and(pos[0]>=(int(self._width/2)-6))):
            if((pos[1]+1==(int(self._height/2) - 5))or(pos[1]-1==(int(self._height/2) - 5))):
                    self._wall_up.update_health(damage)
        ##down
        if(pos[0]<=(int(self._width/2)-6+18)and(pos[0]>=(int(self._width/2)-6))):
            if((pos[1]+1==(int(self._height/2) - 5+10))or (pos[1]-1==(int(self._height/2) - 5+10))):
                    self._wall_down.update_health(damage)
    def king_val(self):
        self._kingattack =1
    def key_board_interrupt(self):
        get = Get()
        ch = input_to(get.__call__)
        if(ch == 'q'):
            sys.exit()
        elif(ch == 'k'):
            self._kingval = 1
        elif ch == 'd':
            self._king.move(ch)
        elif ch == 'a':
            self._king.move(ch)
        elif ch == 'w':
            self._king.move(ch)
        elif ch == 's':
            self._king.move(ch)
        elif ch == 'z':
            self._kingattack =1
    def run(self):
        self.start()
        while True:
            self._screen.clean()
            self._screen.reset_screen()

            self.key_board_interrupt()
            self.king_attack()
            self.placing()

            self._screen.render_screen()


game = Game()
game.run()
