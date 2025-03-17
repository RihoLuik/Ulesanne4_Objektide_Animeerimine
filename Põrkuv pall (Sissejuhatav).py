import pygame
from utils import lBlue

pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

# graafika laadimine
ball = pygame.image.load("images/Sissejuh/ball.png")

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4

running = True
while running:
    clock.tick(60) # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the window when clicking the "X"
            running = False

    screen.fill(lBlue)

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    posX += speedX
    posY += speedY

    # Põrkub servast serva ilma, et vajub akna äärdesse
    ball_width = ball.get_width()
    ball_height = ball.get_height()

    if posX + ball_width > screenX or posX < 0:
        speedX = -speedX

    if posY + ball_height > screenY or posY < 0:
        speedY = -speedY

    # graafika kuvamine ekraanil
    pygame.display.flip()

pygame.quit()