import pygame
from pygame.locals import (
    K_DOWN,
    K_UP,
    K_LEFT,
    K_RIGHT,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,
)
pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("food game")
image = pygame.image.load("fries_game.png")
image_surface = pygame.Surface((image.get_width(), image.get_height()))
image_surface.blit(image, (0, 0))
image2 = pygame.image.load("Sauce_for_game_actually_FR.png")
image_surface2 = pygame.Surface((image2.get_width(), image2.get_height()))
image_surface2.blit(image2, (0, 0))
x = 100
y = 100
x2 = 200
y2 = 200
boundary_left = 0
boundary_right = screen.get_width() - image_surface.get_width()
boundary_top = 0
boundary_bottom = screen.get_height() - image_surface.get_height()
points = 0
font = pygame.font.Font(None, 36)
run = True
speed = 0.5
while run:
    screen.fill((0, 0, 0))
    screen.blit(image_surface, (x, y))
    screen.blit(image_surface2, (x2, y2))
    text = font.render("Points: " + str(points), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        y -= speed
    if keys[K_DOWN]:
        y += speed
    if keys[K_LEFT]:
        x -= speed
    if keys[K_RIGHT]:
        x += speed
    if keys[K_w]:
        y2 -= speed
    if keys[K_s]:
        y2 += speed
    if keys[K_a]:
        x2 -= speed
    if keys[K_d]:
        x2 += speed
    if x < boundary_left:
        x = boundary_left
    elif x > boundary_right:
        x = boundary_right
    if y < boundary_top:
        y = boundary_top
    elif y > boundary_bottom:
        y = boundary_bottom
    if x2 < boundary_left:
        x2 = boundary_left
    elif x2 > boundary_right:
        x2 = boundary_right
    if y2 < boundary_top:
        y2 = boundary_top
    elif y2 > boundary_bottom:
        y2 = boundary_bottom
    if (x < x2 + image_surface2.get_width() and
        x + image_surface.get_width() > x2 and
        y < y2 + image_surface2.get_height() and
        y + image_surface.get_height() > y2):
        points += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()
pygame.quit()
# full game with a glitch
