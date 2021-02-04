import pygame
import pygame.camera
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("kanha's camera")
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    pygame.display.update()



