import pygame
import math
import time
pygame.init()
window = pygame.display.set_mode((350, 350))
window2 = pygame.display.set_mode((350, 350))

run = True
angle = 1;
while run:
    time.sleep(0.016)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rects = [pygame.Rect(70,70,50,50),pygame.Rect(150,250,130,20)]
    angle+=1
    startX = 175
    startY = 175
    window.fill((100, 100, 130))
    dumbStupid = -1
    for rectNum in rects:
        dumbStupid += 1
        pygame.draw.rect(window,(0,255,255),rects[dumbStupid])
    funnycolor = 0
    for angleScanning in range(angle-20,angle+20):
        angleScanning=angleScanning*2
        for i in range(350):
            breakMe = False
            myX = int(startX + i * math.cos(angleScanning * 3.1 / 180))
            myY = int(startY + i * math.sin(angleScanning * 3.1 / 180))
            dumbStupid = -1
            for rectNum in rects:
                dumbStupid +=1
                if(myX>rects[dumbStupid].left and myX < rects[dumbStupid].right and myY > rects[dumbStupid].top and myY < rects[dumbStupid].bottom):
                    breakMe = True
                    break
            if(breakMe):
                breakMe=False
                break

            window.set_at((myX, myY), (255, 0, 0))


    pygame.display.flip()

pygame.quit()
exit()