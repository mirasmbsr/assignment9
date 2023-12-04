import pygame
import os
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Mickey's clock")
FPS = 200
clock = pygame.time.Clock()
running = True
right_hand = pygame.image.load('right-hand.png')
left_hand = pygame.image.load('left-hand.png')
main_image = pygame.image.load('main-clock.png')
rec_r = right_hand.get_rect()
rec_l = left_hand.get_rect()
rec_main = main_image.get_rect()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(main_image, rec_main)
    
    currenttime = datetime.now()
    seconds = currenttime.second
    minutes = currenttime.minute

    pos1 = pygame.transform.rotate(right_hand, -(minutes*6-90))
    pos2 = pygame.transform.rotate(left_hand, -(seconds*6-90))
    rec_pos1 = pos1.get_rect(center=(400,400))
    rec_pos2 = pos2.get_rect(center=(400,400))

    screen.blit(pos1, rec_pos1)
    screen.blit(pos2,rec_pos2)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()