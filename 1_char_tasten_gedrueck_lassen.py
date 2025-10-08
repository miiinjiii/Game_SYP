import pygame

pygame.init()

# Fenster erstellen und größe festlegen
window_width = 1280
window_height = 700
window = pygame.display.set_mode((window_width, window_height))

#einfügen von character
player = pygame.image.load('Exolon_Ast_Right.png')

# Position von Spieler festlegen
x = 32
y = 32

def add_player_location (x, y):
    window.blit (player, (x, y))

# Damit mein Fenster immer offen bleibt bis ich es mit x schließen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Spieler bewegt sich mit W, A, S, D 
        # Änderung hier da wir die Tasten nun gedrückt lassen können
        userinput = pygame.key.get_pressed ()

        if userinput[pygame.K_d]:
            x += 25
        if userinput[pygame.K_a]:
            x -= 25
        if userinput[pygame.K_w]:
            y -= 25
        if userinput[pygame.K_s]:
            y += 25

    window.fill((25, 25, 25))

    add_player_location (x, y)
    pygame.display.update()

pygame.quit()