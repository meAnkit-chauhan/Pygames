import pygame
from warrior import Warrior

pygame.init()
#create game windows
screen_width=980
screen_height=640
screen =pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Warrior")

#set framerate
clock=pygame.time.Clock()
FPS=60

#load background image
bg_image=pygame.image.load("C:\Users\PC\Documents\Ankit folders\ak.jpg").convert_alpha()

 #function for drawing background
def draw_bg():
    scale_bg=pygame.transform.scale(bg_image,(screen_width,screen_height))
    screen.blit(scale_bg,(0,0))


#create two instances of fighters
w1= Warrior(200,300)
w2= Warrior(500,300)

draw_bg()
#game loop
pygame.display.flip()
run=True
while run:

    clock.tick(FPS)

    #draw background
    draw_bg()


    #move warriors
    w1.move()
    #w2.move()

    w1.draw(screen)
    w2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #update display
            pygame.display.update()

#exit pygame
pygame.quit()
