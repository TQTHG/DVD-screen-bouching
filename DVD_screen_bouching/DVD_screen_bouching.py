import pygame
import random
import os

file_path = os.path.dirname(os.path.abspath(__file__))

pygame.init()
pygame.mixer.init()

count = 0
font = pygame.font.SysFont(None,30)

# Screen
width = 1200
height = 800
size = 20

# Frame Per Second
fps = 60
clock = pygame.time.Clock()

# Physics
vy = 5
vx = 5
x = 10
y = 10

# Sounds
bounce_path = os.path.join(file_path,"assets","sounds","Bounce.mp3")
bounce_sound = pygame.mixer.Sound(bounce_path)

# Logo
dvd_width = 100
dvd_height = 50
dvd_path = os.path.join(file_path,"assets","image","DVD_Logo.png")
dvd_image = pygame.image.load(dvd_path)
dvd = pygame.transform.scale(dvd_image,(dvd_width,dvd_height))

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("DVD Screen Bouching")
running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    screen.blit(dvd,(x,y))

    if (y < height - dvd_height ) or (vy != 0):
        y += vy
    if y >= height - dvd_height:
        y = height - dvd_height
        vy *= -1
        bounce_sound.play()
        count += 1

    if (y > 0 ) or (vy != 0):
        y += vy
    if y <= 0 :
        y = 0
        vy *= -1
        bounce_sound.play()
        count += 1

    if (x  < width - dvd_width ) or (vx != 0):
        x += vx
    if x >= width - dvd_width:
        x = width -dvd_width
        vx *= -1
        bounce_sound.play()
        count += 1

    if (x > 0 ) or (vx != 0):
        x += vx
    if x <= 0 :
        x = 0 
        vx *= -1
        bounce_sound.play()
        count += 1

    text = font.render(f"Bounces: {count}" , True , (255,255,255))
    rect = text.get_rect(midtop = (width / 2 , 10))
    screen.blit(text,rect)
        
    clock.tick(fps)
    pygame.display.update()
pygame.quit()