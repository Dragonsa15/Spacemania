import pygame
from constants import *

screen = pygame.display.set_mode((WIDTH,HEIGHT))
font_name = pygame.font.match_font('arial') #To find the closest possible match to the name 'arial' 

def DrawRect(x,y,w,h,c): #GUI
	pygame.draw.rect(screen,c,[x,y,w,h])	


def draw_text(surf,text,size,x,y): #GUI
	font = pygame.font.Font(font_name,int(size))
	text_surface = font.render(text,True,BLUE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surf.blit(text_surface,text_rect)

def Button(x,y,string,color,function,w,h): #GUI
	global mouse
	global click
	mouse =pygame.mouse.get_pos()
	click =pygame.mouse.get_pressed()
	DrawRect(x,y,w,h,color)
	if x<=mouse[0]<=x+w and y<=mouse[1]<=y+h :
			if (click[0] == 1):
				function()
	draw_text(screen,string,(w+h)/8,x+w/2,y)	