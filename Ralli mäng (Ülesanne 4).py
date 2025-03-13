import pygame
import random

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Load images
background = pygame.image.load("images/Ralli/bg_rally.jpg")
red_car = pygame.image.load("images/Ralli/f1_red.png")
blue_car = pygame.image.load("images/Ralli/f1_blue.png")

# Resize if needed
red_car = pygame.transform.scale(red_car, (50, 80))
blue_car = pygame.transform.scale(blue_car, (50, 80))

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

# Red Car Position
red_x = WIDTH // 2 - 25
red_y = HEIGHT - 120

# Blue Car Setup
blue_cars = []
num_blue_cars = 3 # Number of moving cars
for i in range(num_blue_cars):
    x_pos = random.choice([200, 300, 400]) # Lane positions
    y_pos = random.randint(-300, -100)
    blue_cars.append([x_pos, y_pos])

# Game Variables
score = 0
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(background, (0, 0))  # Draw background

    # Display Red Car
    screen.blit(red_car, (red_x, red_y))

    # Move and Draw Blue Cars
    for car in blue_cars:
        car[1] += 5  # Move down
        if car[1] > HEIGHT:  # If car goes off screen, reset
            car[1] = random.randint(-300, -100)
            car[0] = random.choice([200, 300, 400])
            score += 1  # Increase score
        screen.blit(blue_car, (car[0], car[1]))

    # Display Score
    score_text = FONT.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)  # 30 FPS

pygame.quit()