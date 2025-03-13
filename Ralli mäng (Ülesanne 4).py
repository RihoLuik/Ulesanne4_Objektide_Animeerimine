import pygame
import random
from utils import red

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)
GAME_OVER_FONT = pygame.font.Font(None, 72)
SPEED = 5  # Speed of blue cars
PLAYER_SPEED = 7  # Speed of red car movement

# Load images
background = pygame.image.load("images/Ralli/bg_rally.jpg")
red_car = pygame.image.load("images/Ralli/f1_red.png")
blue_car = pygame.image.load("images/Ralli/f1_blue.png")

# Resize images
red_car = pygame.transform.scale(red_car, (50, 80))
blue_car = pygame.transform.scale(blue_car, (50, 80))

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

clock = pygame.time.Clock()


# Function to reset game state
def reset_game():
    global red_x, red_y, blue_cars, score, game_over
    red_x = WIDTH // 2 - 25
    red_y = HEIGHT - 120
    blue_cars = [[random.choice([200, 300, 400]), random.randint(-300, -100)] for _ in range(3)]
    score = 0
    game_over = False


# Initialize game variables
reset_game()
running = True

while running:
    screen.blit(background, (0, 0))  # Draw background

    if not game_over:
        # Player Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and red_x > 150:
            red_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and red_x < WIDTH - 200:
            red_x += PLAYER_SPEED

        # Move and Draw Blue Cars
        for car in blue_cars:
            car[1] += SPEED  # Move down
            if car[1] > HEIGHT:  # Reset if off-screen
                car[1] = random.randint(-300, -100)
                car[0] = random.choice([200, 300, 400])
                score += 1  # Increase score

            # Collision Detection
            red_rect = pygame.Rect(red_x, red_y, 50, 80)
            blue_rect = pygame.Rect(car[0], car[1], 50, 80)
            if red_rect.colliderect(blue_rect):
                game_over = True

            screen.blit(blue_car, (car[0], car[1]))

        # Draw Red Car
        screen.blit(red_car, (red_x, red_y))

        # Display Score
        score_text = FONT.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

    else:
        # Game Over Screen
        game_over_text = GAME_OVER_FONT.render("GAME OVER", True, red)
        score_text = FONT.render(f"Final Score: {score}", True, WHITE)
        restart_text = FONT.render("Press SPACE to Restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 2 + 20))
        screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2 + 60))

        # Check for restart key
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            reset_game()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)  # 30 FPS

pygame.quit()