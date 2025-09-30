import pygame
from pygame import K_w, K_a, K_s, K_d


pygame.init()

window_width = 1000
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
player_x = 32
player_y = 32

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[K_d]:
            player_x += 32
        elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[K_a]:
            player_x -= 32
        elif event.type == pygame.KEYDOWN and pygame.key.get_pressed() [K_w]:
            player_y -= 32
        elif event.type == pygame.KEYDOWN  and pygame.key.get_pressed()[K_s]:
            player_y += 32
    window.fill((25, 25, 25))

    pygame.draw.circle(window, color = "blue", center=(player_x, player_y), radius=32, width=64)
    pygame.display.update()

pygame.quit()