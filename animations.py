import pygame
import os

asset_folder = os.path.dirname(__file__);

explosion = []
for i in range(9):
	filename = "regularExplosion0{}.png".format(i)
	explosion.append(pygame.image.load(os.path.join(asset_folder,filename)))

#To add explosion at the specified 'position' of given 'size' 
class Explosion(pygame.sprite.Sprite) :
	def __init__(self,position,size):
		pygame.sprite.Sprite.__init__(self)
		self.pos = position
		self.size = size
		self.image = pygame.transform.scale(explosion[0],(size,size))
		self.rect = self.image.get_rect()
		self.rect.center = position
		self.current = pygame.time.get_ticks()
		self.time_bet_consec_frames = 50
		self.i = 0
		
	def update(self) : 
		if(pygame.time.get_ticks()-self.current>self.time_bet_consec_frames) : #Update the frame maintaining the frame_rate
			self.i+=1
			if self.i>=len(explosion) :
				self.kill() #Kill the instance after all the frames are over
				return
			self.current = pygame.time.get_ticks() 
			self.image = pygame.transform.scale(explosion[self.i],(self.size,self.size)) #Show next frame
			self.rect = self.image.get_rect()
			self.rect.center = self.pos
