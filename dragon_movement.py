import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600], pygame.RESIZABLE)
image = pygame.image.load("C:\\Users\\user\\Desktop\\D10\\config\\dragon.png")
image = pygame.transform.scale(image, (100, 100))

# kordinatarini olamiz
image_rect = image.get_rect()

# kordinatalarini sozlimiz
image_rect.x = 20
image_rect.y = 40

user_event = pygame.USEREVENT + 1
user_event_ = pygame.event.Event(user_event, newmessage="hello world")
pygame.event.post(user_event_)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                image_rect.x += 10
            elif event.key == pygame.K_a:
                image_rect.x -= 10
            elif event.key == pygame.K_w:
                image_rect.y -= 10
            elif event.key == pygame.K_s:
                image_rect.y += 10
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button bosildi", event.pos)
        elif event.type == user_event:
            print(f"{event.newmessage} >>>>>>>>>>>>>>>")
        elif event.type == pygame.MOUSEMOTION:

            # mishka bir nuqtadan boshqa nuqtaga haraktlangan oraqliq masofasi
            print(event.rel)

            # mishka turgan kordinatasini qaytaradi
            print(event.pos)

            if event.rel[0] > 0:
                print("Sichqoncha o'nga harakatlanmoqda")
            elif event.rel[0] < 0:
                print("Sichqoncha chapga harakatlanmoqda")
            elif event.rel[1] > 0:
                print("Sichqoncha pastga harakatlanmoqda")
            elif event.rel[1] < 0:
                print("Sichqoncha tepaga harakatlanmoqda")

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pygame.display.update()
