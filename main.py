import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

# window
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))


def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Game Main Method
def main():
    run = True
    while run:
        # Quit
        quit_game()

        # Reset the window
        window.fill((0, 0, 0))

        clock.tick(60)
        pygame.display.update()


main()
