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

# Color
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
random_number = random.randint(0,255)
random_color = (random_number,random_number,random_number)

# Ball
x = width / 2
y = height / 2 + 100

# Physics
vy = 5
vx = 5

# Sounds
bounce_path = os.path.join(file_path,"assets","sounds","Bounce.mp3")
bounce_sound = pygame.mixer.Sound(bounce_path)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("DVD Screen Bouching")

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    balls = pygame.draw.circle(screen , random_color , (x , y), size)

    if (y < height - size) or (vy != 0):
        y += vy
    if y >= height - size:
        y = height - size
        vy *= -1
        random_color = (random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255))
        bounce_sound.play()
        count += 1

    if (y > 0 + size) or (vy != 0):
        y += vy
    if y <= 0 + size:
        y = 0 + size
        vy *= -1
        random_color = (random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255))
        bounce_sound.play()
        count += 1

    if (x  < width - size) or (vx != 0):
        x += vx
    if x >= width - size :
        x = width - size
        vx *= -1
        random_color = (random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255))
        bounce_sound.play()
        count += 1

    if (x > 0 + size) or (vx != 0):
        x += vx
    if x <= 0 + size:
        x = 0 + size
        vx *= -1
        random_color = (random.randint(0,255),
                        random.randint(0,255),
                        random.randint(0,255))
        bounce_sound.play()
        count += 1

    text = font.render(f"Bounces: {count}" , True , white)
    rect = text.get_rect(midtop = (width / 2 , 10))
    screen.blit(text,rect)
        
    clock.tick(fps)
    pygame.display.update()
pygame.quit()