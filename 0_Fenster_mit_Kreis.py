import pygame
from pygame import K_w, K_a, K_s, K_d


pygame.init()

# Fenster erstellen und größe festlegen
window_width = 1280
window_height = 700
window = pygame.display.set_mode((window_width, window_height))

# Position von Spieler festlegen
player_x = 32
player_y = 32

# Damit mein Fenster immer offen bleibt bis ich es mit x oder Escpae schließe
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # Spieler bewegt sich mit W, A, S, D 
        elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[K_d]:
            player_x += 32
        elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[K_a]:
            player_x -= 32
        elif event.type == pygame.KEYDOWN and pygame.key.get_pressed() [K_w]:
            player_y -= 32
        elif event.type == pygame.KEYDOWN  and pygame.key.get_pressed()[K_s]:
            player_y += 32

    window.fill((25, 25, 25))

    pygame.draw.circle(window, color = "white", center=(player_x, player_y), radius=32, width=64)
    pygame.display.update()

pygame.quit()