import pygame, sys


pygame.init()
screen = pygame.display.set_mode((800, 800))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # window
    screen.fill((255, 255, 255))

    # head
    pygame.draw.circle(screen, (240, 227, 43), (400, 275), radius=25)

    # eyes
    pygame.draw.rect(screen, (0, 0, 0), (390, 265, 5, 5))
    pygame.draw.rect(screen, (0, 0, 0), (405, 265, 5, 5))

    # mask
    pygame.draw.circle(
        screen, (0, 0, 0), (400, 275),
        radius=25, draw_bottom_left=True,
        draw_bottom_right=True
    )

    # body
    pygame.draw.line(screen, (12, 32, 245), [400, 300], [400, 450])

    # hands
    pygame.draw.line(screen, (240, 227, 43), [400, 320], [360, 360], width=2)
    pygame.draw.line(screen, (240, 227, 43), [400, 320], [440, 360], width=2)

    # foods
    pygame.draw.line(screen, (0, 0, 0), [400, 450], [350, 500])
    pygame.draw.line(screen, (0, 0, 0), [400, 450], [450, 500])

    # updating display
    pygame.display.update()

