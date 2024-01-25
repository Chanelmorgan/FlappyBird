import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

# window
win_height = 720
win_width = 551
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Flappy Bird Game")

# Images
bird_images = [pygame.image.load("assets/bird_down.png"),
               pygame.image.load("assets/bird_mid.png"),
               pygame.image.load("assets/bird_up.png")]
skyline_image = pygame.image.load("assets/background.png")
ground_image = pygame.image.load("assets/ground.png")
top_pipe_image = pygame.image.load("assets/pipe_top.png")
bottom_pipe_image = pygame.image.load("assets/pipe_bottom.png")
game_over_image = pygame.image.load("assets/game_over.png")
start_image = pygame.image.load("assets/start.png")

# Game

# higher the number the faster the ground will be moving
scroll_speed = 1
bird_start_position = (100, 250)


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bird_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = bird_start_position
        # Number that loops through the bird images
        # to animate it
        self.image_index = 0
        self.vel = 0
        # Prevents the player from spamming the space bar
        self.flap = False

    def update(self, user_input):
        # Animate Bird
        self.image_index += 1
        # When the image index gets to 30 reset
        if self.image_index >= 30:
            self.image_index = 0
        self.image = bird_images[self.image_index // 10]

        # Gravity and Flap
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 500:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False
        # User input
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0:
            self.flap = True
            self.vel = -7


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()


def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Game Main Method
def main():
    # Instantiate Bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 520
    ground = pygame.sprite.Group()
    ground.add((Ground(x_pos_ground, y_pos_ground)))

    run = True
    while run:
        # Quit
        quit_game()

        # Reset the window
        window.fill((0, 0, 0))

        # User input
        user_input = pygame.key.get_pressed()

        # Draw background
        window.blit(skyline_image, (0, 0))

        # Spawn Ground -
        # because the images move off the screen we need to generate new ones
        if len(ground) <= 2:
            ground.add(Ground(win_width, y_pos_ground))

        # Draw - Pipes, Ground and Bird to start game
        ground.draw(window)
        bird.draw(window)

        # Update - Pipes, Ground and Bird
        # Need to update the ground so its moves
        ground.update()
        bird.update(user_input)

        # frames per second limited to 60
        clock.tick(60)
        pygame.display.update()


main()
