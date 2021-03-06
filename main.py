import pygame
import math
import time
pygame.init()
window = pygame.display.set_mode((700, 700))

displayMode = 0
renderDistance = 350
run = True
keyDown = [False,False,False,False,False,False]
angle = 45
startX = 80
startY = 80
handImg = pygame.image.load('hands.png')
redImg = pygame.image.load('red.png')
handImg = pygame.transform.scale(handImg, (700, 700))
redImg = pygame.transform.scale(redImg, (400, 400))
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
    rectRed = [0,0,0,0,200,200,255,230,230,230,230,200,200,255,255,50]
    rectRedToDraw = []
    rectGreen = [230,230,230,230,200,200,255,0,0,0,0,200,200,255,0,0]
    rectGreenToDraw = []
    rectBlue = [0,0,0,0,15,15,69,0,0,0,0,15,15,70,0,255]
    rectBlueToDraw = []
    #rects.append(pygame.Rect(70,70,50,50))
    rects.append(pygame.Rect(0, 330, 350, 20))
    rects.append(pygame.Rect(0, 0, 350, 20))
    rects.append(pygame.Rect(0, 0, 20, 350))
    rects.append(pygame.Rect(330, 0, 20, 350)) #outer green (0,230,0)


    #rects.append(pygame.Rect(30+100, 20, 20, 30))
    #rects.append(pygame.Rect(110+100, 20, 20, 30))
    rects.append(pygame.Rect(0, 0, 0, 0))
    rects.append(pygame.Rect(0, 0, 0, 0))


    rects.append(pygame.Rect(0, 20, 350, 10))


    rects.append(pygame.Rect(350, 330, 350, 20))
    rects.append(pygame.Rect(350, 0, 350, 20))
    rects.append(pygame.Rect(350, 0, 20, 350))
    rects.append(pygame.Rect(680, 0, 20, 350))
    #rects.append(pygame.Rect(180, 180, 30 , 30))


    rects.append(pygame.Rect(30+100+350, 20+80, 20, 30))
    rects.append(pygame.Rect(110+100+350, 20+80, 20, 30))

    rects.append(pygame.Rect(50+100+350, 30+80, 60, 10))

    rects.append(pygame.Rect(100, 160, 50, 50))
    rects.append(pygame.Rect(230, 160, 50, 50))


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
        if displayMode == 0:
            displayMode = 1
        else:
            displayMode = 0
        time.sleep(0.2)

    newStartX = startX + playerSpeed * math.cos(angle * 3.1 / 180)
    newStartY = startY + playerSpeed * math.sin(angle * 3.1 / 180)
    dumbStupid2 = -1
    moveHere = True
    for rectNum2 in rects:
        dumbStupid2 += 1
        if (newStartX > rects[dumbStupid2].left and newStartX < rects[dumbStupid2].right and newStartY > rects[dumbStupid2].top and newStartY < rects[dumbStupid2].bottom):
            moveHere = False
            if(rectRed[dumbStupid2] == 255 and rectGreen[dumbStupid2] == 255 and rectBlue[dumbStupid2] == 69):
                moveHere = True
                newStartX += 0
                newStartY += 290
            break
    if moveHere:
        startX = newStartX
        startY = newStartY







    window.fill((100, 100, 130))
    dumbStupid = -1
    for rectNum in rects:
        dumbStupid += 1
        if displayMode == 1:
            pygame.draw.rect(window,(rectRed[dumbStupid],rectGreen[dumbStupid],rectBlue[dumbStupid]),rects[dumbStupid])
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
        myStartX = startX
        myStartY = startY
        for i in range(renderDistance):
            breakMe = False
            myX = int(myStartX + i * math.cos(angleScanning * 3.1 / 180))
            myY = int(myStartY + i * math.sin(angleScanning * 3.1 / 180))
            dumbStupid = -1
            for rectNum in rects:
                dumbStupid +=1
                if(myX>rects[dumbStupid].left and myX < rects[dumbStupid].right and myY > rects[dumbStupid].top and myY < rects[dumbStupid].bottom):
                    if (rectRed[dumbStupid] == 255 and rectGreen[dumbStupid] == 255 and rectBlue[dumbStupid] == 69):
                        myStartX += 0
                        myStartY += 290
                        break
                    if (rectRed[dumbStupid] == 255 and rectGreen[dumbStupid] == 255 and rectBlue[dumbStupid] == 70):
                        myStartX += -350
                        break
                    height = 350-i
                    over = angleScanning-angle
                    renderRects.append(pygame.Rect(350-lineOn*5.8,180-height/2,6,height))
                    lightLevels.append(i/350*250)
                    rectRedToDraw.append(rectRed[dumbStupid])
                    rectGreenToDraw.append(rectGreen[dumbStupid])
                    rectBlueToDraw.append(rectBlue[dumbStupid])
                    breakMe = True
                    break
            if(breakMe):
                breakMe=False
                break
            if displayMode == 1:
                window.set_at((myX, myY), (255, 0, 0))
    iterationB = -1
    scaledRects = [];
    handBlitted = False
    for rectNum in renderRects:
        iterationB +=1
        thisRed = rectRedToDraw[iterationB] - 1*lightLevels[iterationB]
        thisGreen = rectGreenToDraw[iterationB] - 1*lightLevels[iterationB]
        thisBlue = rectBlueToDraw[iterationB] - 1*lightLevels[iterationB]
        if thisRed < 0:
            thisRed = 0
        if thisBlue < 0:
            thisBlue = 0
        if thisGreen < 0:
            thisGreen = 0
        scaleMultiplier = window.get_width()/350
        scaledRects.append(pygame.Rect(renderRects[iterationB].x*scaleMultiplier, renderRects[iterationB].y*scaleMultiplier, renderRects[iterationB].width*scaleMultiplier, renderRects[iterationB].height*scaleMultiplier))
        if displayMode == 0:
            if(rectRedToDraw[iterationB] == 68 and rectGreenToDraw[iterationB] == 69 and rectBlueToDraw[iterationB] == 70 and handBlitted == False):
                window.blit(redImg,scaledRects[iterationB])
                handBlitted = True
            else:
                pygame.draw.rect(window,(thisRed,thisGreen,thisBlue),scaledRects[iterationB])
    #if displayMode == 0:
        #window.blit(handImg, (0,0))
    pygame.display.flip()

pygame.quit()
exit()