import pygame
import os
from maps import *

asset_folder = os.path.dirname(__file__);
blocked_dots = [] # List of dots that are blocked. These will be blocked in each screen frame
dots_left = 298 # To store the no of dots left

play = pygame.image.load(os.path.join(asset_folder,"playerShip1_orange.png"))
#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self,velx,vely):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(play,(25,25));
        self.x = 1 #Initial position of the player
        self.y = 1
        self.velocity = (0,0) #Initial velocity of the player ship
        self.rect = self.image.get_rect()
        self.rect.center = (25,23)
        self.curr_direction = 0
        self.count = 0
        self.bullets_left = 10
        self.life = 3
        self.direction = 0
        self.dots_left = dots_left

    def update(self):
        self.count += 1
        global dot_left
        if(self.count>16):
            if(dots_map[self.y][self.x]) :
                self.dots_left -=1
                blocked_dots.append((self.rect.centerx,self.rect.centery))
                dots_map[self.y][self.x] = 0
            self.count = 0
            self.curr_direction =  self.direction
        #Move the player according to its direction
        if(self.curr_direction==0) : self.velocity = (0,0)
        elif(self.curr_direction==1) :
            ol_rect = self.rect
            self.image = pygame.transform.rotate(pygame.transform.scale(play,(25,25)),90)
            self.rect.center = ol_rect.center
            self.velocity = (-1,0)
        elif(self.curr_direction==2) :
            ol_rect = self.rect
            self.image = pygame.transform.rotate(pygame.transform.scale(play,(25,25)),0)
            self.rect.center = ol_rect.center
            self.velocity = (0,-1)
        elif(self.curr_direction==3) :
            ol_rect = self.rect
            self.image = pygame.transform.rotate(pygame.transform.scale(play,(25,25)),-90)
            self.rect.center = ol_rect.center
            self.velocity = (1,0)
        elif(self.curr_direction==4) :
            ol_rect = self.rect
            self.image = pygame.transform.rotate(pygame.transform.scale(play,(25,25)),180)
            self.rect.center = ol_rect.center
            self.velocity = (0,1)
        if(self.count==0):
            if (map[self.y + self.velocity[1]][self.x + self.velocity[0]]) :
                self.rect.center  = (self.rect.centerx + self.velocity[0],self.rect.centery + self.velocity[1])
                self.x += self.velocity[0]
                self.y += self.velocity[1]
            else :
                self.count = 16
        else :
            self.rect.center  = (self.rect.centerx + self.velocity[0],self.rect.centery + self.velocity[1])