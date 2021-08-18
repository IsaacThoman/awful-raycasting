import pygame
import math
import time
pygame.init()
window = pygame.display.set_mode((350, 350))
window2 = pygame.display.set_mode((350, 350))

run = True
keyDown = [False,False,False,False,False,False]
angle = 1;
startX = 175
startY = 175
while run:
    time.sleep(0.016)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:

            # checking if key "A" was pressed
            if event.key == pygame.K_w:
                keyDown[0] = True
            if event.key == pygame.K_a:
                keyDown[1] = True
            if event.key == pygame.K_s:
                keyDown[2] = True
            if event.key == pygame.K_d:
                keyDown[3] = True
            if event.key == pygame.K_q:
                keyDown[4] = True
            if event.key == pygame.K_e:
                keyDown[5] = True

        if event.type == pygame.KEYUP:

            # checking if key "A" was pressed
            if event.key == pygame.K_w:
                keyDown[0]= False
            if event.key == pygame.K_a:
                keyDown[1] = False
            if event.key == pygame.K_s:
                keyDown[2] = False
            if event.key == pygame.K_d:
                keyDown[3] = False
            if event.key == pygame.K_q:
                keyDown[4] = False
            if event.key == pygame.K_e:
                keyDown[5] = False

    rects = []
    lightLevels = []
    rects.append(pygame.Rect(70,70,50,50))
    rects.append(pygame.Rect(0,330,350,20))
    if keyDown[1]:
        angle += 2
    if keyDown[3]:
        angle += 0-2

    playerSpeed = 0
    if keyDown[0]:
        playerSpeed = 2
    if keyDown[2]:
        playerSpeed = 0-2
    playerSideSpeed = 0
    if keyDown[4]:
        playerSideSpeed = 2
    if keyDown[5]:
        playerSideSpeed = 0-2


    startX = int(startX + playerSpeed * math.cos(angle * 3.1 / 180))
    startY = int(startY + playerSpeed * math.sin(angle * 3.1 / 180))

    startX = int(startX + playerSideSpeed * math.cos(angle+90 * 3.1 / 180))
    startY = int(startY + playerSideSpeed * math.sin(angle+90 * 3.1 / 180))



    window.fill((100, 100, 130))
    dumbStupid = -1
    for rectNum in rects:
        dumbStupid += 1
        #pygame.draw.rect(window,(0,255,255),rects[dumbStupid])
    funnycolor = 0
    renderRects = []
    if angle >= 360:
        angle = (angle % 360)
    lineOn = 0
    for angleScanning in range(angle-30, angle + 30):
        lineOn +=1
        #if angleScanning > 360:
            #angleScanning = angleScanning % 360
        angleScanning=angleScanning
        for i in range(350):
            breakMe = False
            myX = int(startX + i * math.cos(angleScanning * 3.1 / 180))
            myY = int(startY + i * math.sin(angleScanning * 3.1 / 180))
            dumbStupid = -1
            for rectNum in rects:
                dumbStupid +=1
                if(myX>rects[dumbStupid].left and myX < rects[dumbStupid].right and myY > rects[dumbStupid].top and myY < rects[dumbStupid].bottom):
                    height = 350-i
                    over = angleScanning-angle
                    renderRects.append(pygame.Rect(300-lineOn*4,200-height/2,4,height))
                    lightLevels.append(i/350*250)
                    breakMe = True
                    break
            if(breakMe):
                breakMe=False
                break

            #window.set_at((myX, myY), (255, 0, 0))
    iterationB = -1
    for rectNum in renderRects:
        iterationB +=1
        pygame.draw.rect(window,(0,250-lightLevels[iterationB],0),renderRects[iterationB])

    pygame.display.flip()

pygame.quit()
exit()