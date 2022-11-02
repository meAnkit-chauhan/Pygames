import pygame
class Warrior():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))

    def move(self):
        speed=10
        dx=0
        dy=0

        #get key presses
        key= pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx= -speed
        if key[pygame.K_d]:
            dx= speed

        #ensure player stays on screen
        if self.rect.left + dx<0:


        #update player postion
        self.rect.x +=dx
        self.rect.y +=dy
     
    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)
