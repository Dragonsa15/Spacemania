import pygame
from maps import *
from animations import *
from constants import *

# Initialization
asset_folder = os.path.dirname(__file__);
laser = pygame.image.load(os.path.join(asset_folder,"laserRed16.png"))
all_sprites = pygame.sprite.Group() 

#To add bullets to the game
class Bullets(pygame.sprite.Sprite) :
    def __init__(self,posx,posy,velox,veloy):
        pygame.sprite.Sprite.__init__(self)
        if velox>0 : #Set the direction of the bullet accordingly
            self.image = pygame.transform.rotate(pygame.transform.scale(laser,(10,20)),90)
        if velox<0 : 
            self.image = pygame.transform.rotate(pygame.transform.scale(laser,(10,20)),-90)
        if veloy>0 : 
            self.image = pygame.transform.rotate(pygame.transform.scale(laser,(10,20)),0)
        if veloy<0 : 
            self.image = pygame.transform.rotate(pygame.transform.scale(laser,(10,20)),180)
        self.rect = self.image.get_rect()
        self.count = 0
        self.rect.center = (posx,posy)
        self.velx = velox
        self.vely = veloy
    
    def update(self):
        self.count += 1
        if self.count>8 : #Update the position of the bullet on the map by one unit after every 16 iterations(this depends on the speed of the bullet)
            self.count = 0 
            
        if map[int((self.rect.centery+5-6)/17)][int((self.rect.centerx+5-8)/17)]==0 : #Explode the bullet when it hits the boundary
                explo = Explosion(self.rect.center,20)
                all_sprites.add(explo)
                self.kill()
        self.rect.centery += self.vely #To move the bullet forward in each frame
        self.rect.centerx += self.velx
        if self.rect.top < -20 or self.rect.left < 0 or self.rect.right > WIDTH-30 or self.rect.bottom > HEIGHT:
            explo = Explosion(self.rect.center,20) #Explode the bullet when the bullet reaches the boundary
            all_sprites.add(explo)
            self.kill()
