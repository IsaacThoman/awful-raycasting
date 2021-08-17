import pygame

pygame.init()
window = pygame.display.set_mode((350, 350))
window2 = pygame.display.set_mode((350, 350))

run = True
color = 100
colorChange = 10
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect = pygame.Rect(window.get_rect().center, (0, 0)).inflate(*([min(window.get_size()) // 2] * 2))

    if (color >= 240):
        colorChange = -10
    if (color <= 0):
        colorChange = 10
    color += colorChange
    for x in range(350):
        for y in range(350):
            window.set_at((x, y), (color,color/5,color/5))

    pygame.display.flip()

pygame.quit()
exit()