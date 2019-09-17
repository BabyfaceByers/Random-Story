import pygame, sys, random, os, inspect, time
from pygame.locals import *
pygame.init()
StorySurface=pygame.display.set_mode((600,600),pygame.RESIZABLE)
white=(255,255,255)
black=(0,0,0)
lightgrey=(236, 240, 241)
grey=(149, 165, 166)
darkgrey=(127, 140, 141)
greenbuttonregular=(46, 204, 113)
greenbuttonhover=(39, 174, 96)
redbuttonregular=(231, 76, 60)
redbuttonhover=(192, 57, 43)
OatmealCompanyLogo=pygame.image.load('Oatmeal_Company_Logo.png')
StorySurface.fill(white)
StorySurface.blit(pygame.transform.scale(OatmealCompanyLogo,(600,600)),((StorySurface.get_width()/2-300),(StorySurface.get_width()/2-300)))
pygame.display.update()
save1arraypre=[]
save1items=[]
save2arraypre=[]
save2items=[]
save3arraypre=[]
save3items=[]
savedebugarraypre=[]
savedebugitems=[]
click3=0
initemscreen=False
save1=False
save2=False
save3=False
try:
    file=open("save1.txt","r")
    
    for line in file:
        save1arraypre.append(line.rstrip("\n"))
    file.close()
    save1loc=save1arraypre[0]
    save1arraypre.remove(save1arraypre[0])
    for x in save1arraypre:
        save1items.append(x)
except:
    pass
try:
    file=open("save2.txt","r")
    
    for line in file:
        save2arraypre.append(line.rstrip("\n"))
    file.close()
    save2loc=save2arraypre[0]
    save2arraypre.remove(save2arraypre[0])
    for x in save2arraypre:
        save2items.append(x)
except:
    pass
try:
    file=open("save3.txt","r")
    
    for line in file:
        save3arraypre.append(line.rstrip("\n"))
    file.close()
    save3loc=save3arraypre[0]
    save3arraypre.remove(save3arraypre[0])
    for x in save3arraypre:
        save3items.append(x)
except:
    pass
try:
    file=open("debugsave.txt","r")
    
    for line in file:
        savedebugarraypre.append(line.rstrip("\n"))
    file.close()
    savedebugloc=save3arraypre[0]
    savedebugarraypre.remove(savedebugarraypre[0])
    for x in savedebugarraypre:
        savedebugitems.append(x)
except:
    pass
#Story
def gamestart():
    print(inspect.stack()[0][3])
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        smallText=pygame.font.SysFont("arial",int(StorySurface.get_height()/5/2))
        textSurf,textRect=text_objects("The Random Story",smallText,black)
        textRect.center=( (int(StorySurface.get_width()/2),(int(StorySurface.get_height()/4) ) ) )
        StorySurface.blit(textSurf,textRect)
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Start",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",redbuttonregular,redbuttonhover,white,None,None)
        pygame.display.update()

def startcave():
    print(inspect.stack()[0][3])
    inspect.stack()[0][3]
    global StorySurface
    youritems.clear()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LSHIFT and event.key==pygame.K_w and event.key==pygame.K_RSHIFT:
                    debugload()
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[0], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, "You have just woken up, you are floating face up in a one foot deep lake. A woman's voice wispers to you \"Pick up the golden book.\" you look around and see a golden book sitting an a pedestal. Take it?", (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, giveandtravel, "Yes",greenbuttonregular,greenbuttonhover,white,0,caveentrance)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, caveentrance, "No",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def caveentrance():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[1], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'When you leave the cave, there is a large rabbit outside. He introduces himself as Big Chungus. He goes on to ask you, with no explanation, "Do you prefer small, normal, or big?"', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/7, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, ChungusResponse, "Small",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/7*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, giveandtravel, "Normal",greenbuttonregular,greenbuttonhover,white,3,ChungusResponse)
        button(StorySurface.get_width()/7*5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, giveandtravel, "Big",greenbuttonregular,greenbuttonhover,white,1,ChungusResponse)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def ChungusResponse():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[1], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        if items[1] in youritems:
            blit_text(StorySurface, 'He says "'+"Thank you for your kindness! Here's a copy of my autobiography!"+'" Then he walks away.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        elif items[3] in youritems:
            blit_text(StorySurface, 'He says "'+"That's good enough! Here's a 50% off coupon for my autobiography!"+'" Then he walks away.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        else:
            blit_text(StorySurface, 'He says "'+"OK! Goodbye!"+'" Then he walks away.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, uphilldownhill, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def uphilldownhill():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[1], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You look around and realize that you can only walk uphill, or downhill.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, uphill, "Uphill",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, downhillgameover, "Downhill",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def uphill():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[3], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'When you reach the top of the hill, you see a large golden banana shaped structure. Enter it?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        if items[0] in youritems:
            button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, BananaTempleEntrance, "Yes",greenbuttonregular,greenbuttonhover,white,None,None)
        else:
            button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, nogoldbook, "Yes",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, DonkeyKongGameOver, "No",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def BananaTempleEntrance():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[4], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'When you enter you see Donkey Kong praying to a pile of bananas using a book like the one in the cave. Pray with him?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, giveandtravel, "Yes",greenbuttonregular,greenbuttonhover,white,4,BananaTempleThanks)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, nogoldbook, "No",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None) , pygame.display.update()

def BananaTempleThanks():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[4], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You pull out the golden book and pray with Donkey Kong. After you both finish praying, he thanks you for your kindness and gives you a banana.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, BananaTempleLeave, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()
        
def BananaTempleLeave():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[4], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'After talking to Donkey Kong for a little while, you decide that you have to go. Donkey kong mentioned something about a strange tunnel underneath the temple. Would you like to take the tunnel, or go back down the hill.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, TempleTunnelMain, "Tunnel",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, CaveEntranceAfterTemple, "Downhill",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def TempleTunnelMain():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[5], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You enter the tunnel and immediately find yourself at a fork in the road. You can go left, right, or straight.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/7, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, TempleTunnelLeft, "Left",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/7*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, TempleTunnelExitMain, "Straight",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/7*5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, TempleTunnelRight, "Right",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def TunnelMain():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[5], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You can go left, right, or straight.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/7, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, TempleTunnelLeft, "Left",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/7*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, TempleTunnelExitMain, "Straight",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/7*5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/7, StorySurface.get_height()/12, TempleTunnelRight, "Right",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def TempleTunnelLeft():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[6], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You enter a room that has only a pedestal with a gold key on it. Would you like to take the key or turn back?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, giveandtravel, "Take Key",greenbuttonregular,greenbuttonhover,white,5,TempleTunnelExitMain)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, TunnelMain, "Go Back",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def TempleTunnelRight():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[7], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You enter a room that has only a pedestal with a gold key on it. Would you like to take the key or turn back?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, BananaDeath, "Take Key",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, TunnelMain, "Go Back",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def TempleTunnelExitMain():
    global StorySurface
    if items[5] not in youritems:
        TempleTunnelGameOver()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[8], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You reach a starcase that leads to a hatch in the ceiling. As you reach the starcase, a wall closes behind you trapping you in the tunnel. You use your golden key to unlock the hatch and leave the tunnel.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, Field, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def Field():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[9], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'When you come out of the hatch, you see that you are in the middle of a field. You see a Walmart in one direction and a house in the other. Where would you like to go?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, Walmart, "Walmart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gotohouse, "House",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def Walmart():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[10], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, '"Hi, welcome to walmart!" What would you like to buy?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        if items[1] in youritems:
            button(0, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, walmartbuy, "Sword",greenbuttonregular,greenbuttonhover,white,"Sword",None)
            button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, walmartbuy, "Cereal",greenbuttonregular,greenbuttonhover,white,"Cereal",None)
            button(StorySurface.get_width()/3*2, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, walmartbuy, "2 Apples",greenbuttonregular,greenbuttonhover,white,"Apples",None)
        else:
            button(StorySurface.get_width()/4, StorySurface.get_height()/5*3.5, StorySurface.get_width()/4, StorySurface.get_height()/12, walmartbuy, "Sword",greenbuttonregular,greenbuttonhover,white,"Sword",None)
            button(StorySurface.get_width()/4*2, StorySurface.get_height()/5*3.5, StorySurface.get_width()/4, StorySurface.get_height()/12, walmartbuy, "Cereal",greenbuttonregular,greenbuttonhover,white,"Cereal",None)
            button(StorySurface.get_width()/4*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/4, StorySurface.get_height()/12, walmartbuy, "2 Apples",greenbuttonregular,greenbuttonhover,white,"Apples",None)
            if items[3] in youritems:
                button(0, StorySurface.get_height()/5*3.5, StorySurface.get_width()/4, StorySurface.get_height()/12, walmartbuy, "Apple + Autobiography",greenbuttonregular,greenbuttonhover,white,"Autobiography50",None)
            else:
                button(0, StorySurface.get_height()/5*3.5, StorySurface.get_width()/4, StorySurface.get_height()/12, walmartbuy, "Autobiography",greenbuttonregular,greenbuttonhover,white,"Autobiography",None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def CaveEntranceAfterTemple():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[1], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You have returned to the entrance of the cave where you woke up. Do you want to continue going down the hill, or do you want to enter the cave?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, returnToCave, "Cave",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, downhillgameover, "Downhill",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def returnToCave():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[0], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'When you enter the cave, the cave closes in on you. Would you like to go back to sleep in the lake, or bang on the area where the entrance was.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, ISleep, "Sleep",greenbuttonregular,greenbuttonhover,white,None,None)
        if items[1] in youritems:
            button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, BigChungusSavesYou, "Knock",greenbuttonregular,greenbuttonhover,white,None,None)
        else:
            button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, NobodySavesYou, "Knock",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def BigChungusSavesYou():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[0], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'Big Chungus reopens the cave and lets you out. He tells you that he was lucky to see you return to the cave. He brings you to his house.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, teaquestion, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def gotohouse():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[9], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You walk towards the house and see that it is Big Chungus\' house.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, houseentrance, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def houseentrance():
    if items[1] not in youritems:
        ChungusHouseDeath()
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[11], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'Big Chungus opens the door and asks you to show him your copy of his autobiography. You show him it and lets you in.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, teaquestion, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def teaquestion():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[12], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'When you walk inside, he asks if you want some tea.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, teaburn, "Yes",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, booksign, "No",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def teaburn():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[12], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You burn your tongue on the tea. Big chungus makes a medicine to help the burn, but you need to eat a fruit with the medicine or else you will pass out.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, teamedgood, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def teamedgood():
    global StorySurface
    if items[4] in youritems or items[8] in youritems:
        try:
            removeitem(4)
        except:
            removeitem(8)
    else:
        teaburnfaint()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[12], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You eat a fruit and take the medicine.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, booksign, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def booksign():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[12], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'Big Chungus asks you "Do you want me to sign your book?"', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, booksigning, "Yes",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, leaveportal, "No",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def leaveportal():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[11], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You leave Big Chungus\' house, and see a large red, silver, and blue portal. Enter it?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, portalyes, "Yes",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, portalno, "No",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def portalyes():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You walk through the portal and are immediately captured by what you guess to be soldiers. They are wearing strange black hats with a picture of a crab holding a blue kitchen knife on them.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, portalcastle, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def portalno():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'A group of strange people that you can only guess are soldiers come out of the portal, immediately capture you, and bring you into the portal. They are wearing strange black hats with a picture of a crab holding a blue kitchen knife on them.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, portalcastle, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def portalcastle():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'They bring you to a large castle that is covered in what the ancient civilizations called "memes."', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, portalcastle2, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def portalcastle2():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'You see a crab with a blue kitchen knife like the ones on the soldiers hats practicing its knife skills with it\'s knife.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, portalcastle3, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def portalcastle3():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'It sees you and yells out to you "What are you doing opening a portal to my land, the land of Oatmeal the Crab!"', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, OatmealDeath, "Accident",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, portalcastle4, "Join you",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def portalcastle4():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, '"You want to join me? First you must give me a copy of Big Chungus\' autobiography." Give it to him?', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, portalcastle5, "Yes",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, OatmealDeath, "No",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def portalcastle5():
    if items[2] in youritems:
        OatmealDeath2()
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, '"You can join my army." You are dressed with the soldiers clothes and told that you will be given a place to live in the castle.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, TheEnd, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

#gameovers
def downhillgameover():
    youritems=[]
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'As you walk down the hill, you trip and fall into a pit of lava before Einstein can warn you.\nGAME OVER', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def teaburnfaint():
    youritems=[]
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'You take the medicine and your burn feels better, but you faint a few seconds later.\nGAME OVER', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def TempleTunnelGameOver():
    youritems=[]
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'You reach a starcase that leads to a hatch in the ceiling. As you reach the starcase, a wall closes behind you trapping you in the tunnel. You don\'t have a key to unlock the hatch.\nGAME OVER', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def NobodySavesYou():
    youritems=[]
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'Nobody comes to save you so you are forced to stay in the cave for eternity.\nGAME OVER', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def BananaDeath():
    youritems=[]
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'You take the key and a giant banana falls on you.\nGAME OVER', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def ISleep():
    youritems=[]
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'You go back to sleep in the lake.\nGAME OVER', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def DonkeyKongGameOver():
    global StorySurface
    youritems=[]
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'Donkey Kong charges out, picks you up, and throws you to the middle of the ocean where the Banana Gods Carry you away.\nGAME OVER', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def ChungusHouseDeath():
    global StorySurface
    youritems=[]
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'Big Chungus opens the door and asks you to show him your copy of his autobiography. Since you don\'t have the autobiography, he throws you into the trash.\nGAME OVER', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def nogoldbook():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[4], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'Donkey Kong gets up and throws you out of the Banana Temple.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, DonkeyKongGameOver, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def OatmealDeath():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[3], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, 'Oatmeal clicks its claws together and a portal opens up beside you. Donkey Kong comes out of the portal and throws you through it back to the regular world.', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, DonkeyKongGameOver, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def OatmealDeath2():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, locations[13], (20, 10), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        blit_text(StorySurface, '"How dare you deface this book with writing!"', (20, 40), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()/3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/3, StorySurface.get_height()/12, DonkeyKongGameOver, "Next",greenbuttonregular,greenbuttonhover,white,None,None)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, itemscreen, "Inventory",grey,darkgrey,white,inspect.stack()[0][3],None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def TheEnd():
    global StorySurface
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        blit_text(StorySurface, 'The End', (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/6)))
        button(StorySurface.get_width()/5, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, startcave, "Restart",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()/5*3, StorySurface.get_height()/5*3.5, StorySurface.get_width()/5, StorySurface.get_height()/12, gamequit, "Quit",greenbuttonregular,greenbuttonhover,white,None,None)
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()

def itemscreen(curloc):
    global initemscreen, StorySurface
    initemscreen = True
    while initemscreen:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamequit()
            if event.type == pygame.VIDEORESIZE:
                StorySurface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        StorySurface.fill(lightgrey)
        button(0, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, closeitemscreen, "Back",grey,darkgrey,white,None,None)
        itemList=""
        for item in youritems:
            itemList=itemList+item+"\n"
        blit_text(StorySurface, itemList, (20, 20), pygame.font.SysFont('Arial', int(StorySurface.get_height()/12/2)))
        button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save3, "Save 3",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save2, "Save 2",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14, StorySurface.get_width()/6, StorySurface.get_height()/14, save1, "Save 1",grey,darkgrey,white,inspect.stack()[0][3],None), button(StorySurface.get_width()-StorySurface.get_width()/6, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load3, "Load 3",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*2, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load2, "Load 2",grey,darkgrey,white,None,None), button(StorySurface.get_width()-(StorySurface.get_width()/6)*3, StorySurface.get_height()-StorySurface.get_height()/14*2, StorySurface.get_width()/6, StorySurface.get_height()/14, load1, "Load 1",grey,darkgrey,white,None,None), pygame.display.update()
def closeitemscreen():
    global initemscreen
    initemscreen = False
def booksigning():
    removeitem(1)
    giveitem(2)
    leaveportal()
def walmartbuy(itemtype):
    if itemtype == "Sword":
        removeitem(4)
        giveitem(6)
    elif itemtype == "Cereal":
        removeitem(4)
        giveitem(7)
    elif itemtype == "Apples":
        removeitem(4)
        giveitem(8)
        giveitem(8)
    elif itemtype == "Autobiography50":
        removeitem(4)
        removeitem(3)
        giveitem(1)
        giveitem(8)
    elif itemtype == "Autobiography":
        removeitem(4)
        giveitem(1)
    gotohouse()
def giveandtravel(itm,loc):
    giveitem(itm)
    loc()
def removeandtravel(itm,loc):
    removeitem(itm)
    loc()
def gamequit():
    pygame.quit()
    raise SystemExit
def text_objects(text,font,colour):
    textSurface=font.render(text,True,colour)
    return textSurface,textSurface.get_rect()
def button(x,y,w,h,function,text,colourregular,colourhover,textcolour,variable1,variable2):
    global click3
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if mouse[0]>x and mouse[0]<x+w and mouse[1]>y and mouse[1]<y+h and pygame.mouse.get_focused() != 0:
        pygame.draw.rect(StorySurface, colourhover, ((x,y),(w,h)))
        if click[0]==1 and function!=None and click3==0:
            click3=1
            if variable1 != None and variable2 != None:
                function(variable1,variable2)
            elif variable1 != None and variable2 == None:
                function(variable1)
            elif variable1 == None and variable2 != None:
                function(variable2)
            else:
                function()
        if click[0]==0:
            click3=0 
    else:
        pygame.draw.rect(StorySurface, colourregular, ((x,y),(w,h)))
    smallText=pygame.font.SysFont("arial",int(h/2))
    textSurf,textRect=text_objects(text,smallText,textcolour)
    textRect.center=( (x+(w/2)),(y+(h/2)) )
    StorySurface.blit(textSurf,textRect)
def define(array):
    if array=="loc":
        loc=["Cave",#[0]
        "Cave Entrance",#[1]

        "Downhill",#[2]
        "Uphill",#[3]

        "Banana Temple",#[4]

        "Secret Passage",#[5]
        "Secret Passage - Left Room",#[6]
        "Secret Passage - Right Room",#[7]
        "Secret Passage - Stairway",#[8]

        "Field",#[9]

        "Walmart",#[10]

        "Big Chungus' Front Doorstep",#[11]
        "Big Chungus' House",#[12]

        "Portal World",#[13]
        "Portal World - Castle"]#[14]
        return loc
    elif array=="itm":
        itm=["Golden Book",#[0]

        "Big Chungus' Autobiography",#[1]
        "Big Chungus' Signed Autobiography",#[2]
        "Big Chungus' Autobiography 50% off coupon",#[3]

        "Banana",#[4]
        "Golden Key",#[5]

        "Sword",#[6]
        "Box of Cereal",#[7]
        "Apple"]#[8]
        return itm
locations=define("loc")
items=define("itm")
youritems=[]
def giveitem(itm):
    youritems.append(items[itm])
def removeitem(itm):
    youritems.remove(items[itm])
for x in range (0,len(youritems)):
    print(youritems[x],x)
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def save1(Loc):
    file=open("save1.txt","w+")
    file.write(str(Loc+"\n"))
    for x in youritems:
        file.write(str(x+"\n"))
def save2(Loc):
    file=open("save2.txt","w+")
    file.write(str(Loc+"\n"))
    for x in youritems:
        file.write(str(x+"\n"))
def save3(Loc):
    file=open("save3.txt","w+")
    file.write(str(Loc+"\n"))
    for x in youritems:
        file.write(str(x+"\n"))
def load1():
    youritems.clear()
    for x in save1items:
        youritems.append(x)
    if save1loc=="gamestart":
        gamestart()
    elif save1loc=="startcave":
        startcave()
    elif save1loc=="caveentrance":
        caveentrance()
    elif save1loc=="ChungusResponse":
        ChungusResponse()
    elif save1loc=="uphilldownhill":
        uphilldownhill()
    elif save1loc=="uphill":
        uphill()
    elif save1loc=="BananaTempleEntrance":
        BananaTempleEntrance()
    elif save1loc=="BananaTempleThanks":
        BananaTempleThanks()
    elif save1loc=="BananaTempleLeave":
        BananaTempleLeave()
    elif save1loc=="TempleTunnelMain":
        TempleTunnelMain()
    elif save1loc=="TunnelMain":
        TunnelMain()
    elif save1loc=="TempleTunnelLeft":
        TempleTunnelLeft()
    elif save1loc=="TempleTunnelRight":
        TempleTunnelRight()
    elif save1loc=="TempleTunnelExitMain":
        TempleTunnelExitMain()
    elif save1loc=="Field":
        Field()
    elif save1loc=="Walmart":
        Walmart()
    elif save1loc=="CaveEntranceAfterTemple":
        CaveEntranceAfterTemple()
    elif save1loc=="returnToCave":
        returnToCave()
    elif save1loc=="BigChungusSavesYou":
        BigChungusSavesYou()
    elif save1loc=="gotohouse":
        gotohouse()
    elif save1loc=="houseentrance":
        houseentrance()
    elif save1loc=="teaquestion":
        teaquestion()
    elif save1loc=="teaburn":
        teaburn()
    elif save1loc=="teamedgood":
        teamedgood()
    elif save1loc=="booksign":
        booksign()
    elif save1loc=="leaveportal":
        leaveportal()
    elif save1loc=="portalyes":
        portalyes()
    elif save1loc=="portalno":
        portalno()
    elif save1loc=="portalcastle":
        portalcastle()
    elif save1loc=="portalcastle2":
        portalcastle2()
    elif save1loc=="portalcastle3":
        portalcastle3()
    elif save1loc=="portalcastle4":
        portalcastle4()
    elif save1loc=="portalcastle5":
        portalcastle5()
    elif save1loc=="downhillgameover":
        downhillgameover()
    elif save1loc=="teaburnfaint":
        teaburnfaint()
    elif save1loc=="TempleTunnelGameOver":
        TempleTunnelGameOver()
    elif save1loc=="NobodySavesYou":
        NobodySavesYou()
    elif save1loc=="BananaDeath":
        BananaDeath()
    elif save1loc=="ISleep":
        ISleep()
    elif save1loc=="DonkeyKongGameOver":
        DonkeyKongGameOver()
    elif save1loc=="ChungusHouseDeath":
        ChungusHouseDeath()
    elif save1loc=="nogoldbook":
        nogoldbook()
    elif save1loc=="OatmealDeath":
        OatmealDeath()
    elif save1loc=="OatmealDeath2":
        OatmealDeath2()
    elif save1loc=="TheEnd":
        TheEnd()
def load2():
    youritems.clear()
    for x in save2items:
        youritems.append(x)
    if save2loc=="gamestart":
        gamestart()
    elif save2loc=="startcave":
        startcave()
    elif save2loc=="caveentrance":
        caveentrance()
    elif save2loc=="ChungusResponse":
        ChungusResponse()
    elif save2loc=="uphilldownhill":
        uphilldownhill()
    elif save2loc=="uphill":
        uphill()
    elif save2loc=="BananaTempleEntrance":
        BananaTempleEntrance()
    elif save2loc=="BananaTempleThanks":
        BananaTempleThanks()
    elif save2loc=="BananaTempleLeave":
        BananaTempleLeave()
    elif save2loc=="TempleTunnelMain":
        TempleTunnelMain()
    elif save2loc=="TunnelMain":
        TunnelMain()
    elif save2loc=="TempleTunnelLeft":
        TempleTunnelLeft()
    elif save2loc=="TempleTunnelRight":
        TempleTunnelRight()
    elif save2loc=="TempleTunnelExitMain":
        TempleTunnelExitMain()
    elif save2loc=="Field":
        Field()
    elif save2loc=="Walmart":
        Walmart()
    elif save2loc=="CaveEntranceAfterTemple":
        CaveEntranceAfterTemple()
    elif save2loc=="returnToCave":
        returnToCave()
    elif save2loc=="BigChungusSavesYou":
        BigChungusSavesYou()
    elif save2loc=="gotohouse":
        gotohouse()
    elif save2loc=="houseentrance":
        houseentrance()
    elif save2loc=="teaquestion":
        teaquestion()
    elif save2loc=="teaburn":
        teaburn()
    elif save2loc=="teamedgood":
        teamedgood()
    elif save2loc=="booksign":
        booksign()
    elif save2loc=="leaveportal":
        leaveportal()
    elif save2loc=="portalyes":
        portalyes()
    elif save2loc=="portalno":
        portalno()
    elif save2loc=="portalcastle":
        portalcastle()
    elif save2loc=="portalcastle2":
        portalcastle2()
    elif save2loc=="portalcastle3":
        portalcastle3()
    elif save2loc=="portalcastle4":
        portalcastle4()
    elif save2loc=="portalcastle5":
        portalcastle5()
    elif save2loc=="downhillgameover":
        downhillgameover()
    elif save2loc=="teaburnfaint":
        teaburnfaint()
    elif save2loc=="TempleTunnelGameOver":
        TempleTunnelGameOver()
    elif save2loc=="NobodySavesYou":
        NobodySavesYou()
    elif save2loc=="BananaDeath":
        BananaDeath()
    elif save2loc=="ISleep":
        ISleep()
    elif save2loc=="DonkeyKongGameOver":
        DonkeyKongGameOver()
    elif save2loc=="ChungusHouseDeath":
        ChungusHouseDeath()
    elif save2loc=="nogoldbook":
        nogoldbook()
    elif save2loc=="OatmealDeath":
        OatmealDeath()
    elif save2loc=="OatmealDeath2":
        OatmealDeath2()
    elif save2loc=="TheEnd":
        TheEnd()
def load3():
    youritems.clear()
    for x in save3items:
        youritems.append(x)
    if save3loc=="gamestart":
        gamestart()
    elif save3loc=="startcave":
        startcave()
    elif save3loc=="caveentrance":
        caveentrance()
    elif save3loc=="ChungusResponse":
        ChungusResponse()
    elif save3loc=="uphilldownhill":
        uphilldownhill()
    elif save3loc=="uphill":
        uphill()
    elif save3loc=="BananaTempleEntrance":
        BananaTempleEntrance()
    elif save3loc=="BananaTempleThanks":
        BananaTempleThanks()
    elif save3loc=="BananaTempleLeave":
        BananaTempleLeave()
    elif save3loc=="TempleTunnelMain":
        TempleTunnelMain()
    elif save3loc=="TunnelMain":
        TunnelMain()
    elif save3loc=="TempleTunnelLeft":
        TempleTunnelLeft()
    elif save3loc=="TempleTunnelRight":
        TempleTunnelRight()
    elif save3loc=="TempleTunnelExitMain":
        TempleTunnelExitMain()
    elif save3loc=="Field":
        Field()
    elif save3loc=="Walmart":
        Walmart()
    elif save3loc=="CaveEntranceAfterTemple":
        CaveEntranceAfterTemple()
    elif save3loc=="returnToCave":
        returnToCave()
    elif save3loc=="BigChungusSavesYou":
        BigChungusSavesYou()
    elif save3loc=="gotohouse":
        gotohouse()
    elif save3loc=="houseentrance":
        houseentrance()
    elif save3loc=="teaquestion":
        teaquestion()
    elif save3loc=="teaburn":
        teaburn()
    elif save3loc=="teamedgood":
        teamedgood()
    elif save3loc=="booksign":
        booksign()
    elif save3loc=="leaveportal":
        leaveportal()
    elif save3loc=="portalyes":
        portalyes()
    elif save3loc=="portalno":
        portalno()
    elif save3loc=="portalcastle":
        portalcastle()
    elif save3loc=="portalcastle2":
        portalcastle2()
    elif save3loc=="portalcastle3":
        portalcastle3()
    elif save3loc=="portalcastle4":
        portalcastle4()
    elif save3loc=="portalcastle5":
        portalcastle5()
    elif save3loc=="downhillgameover":
        downhillgameover()
    elif save3loc=="teaburnfaint":
        teaburnfaint()
    elif save3loc=="TempleTunnelGameOver":
        TempleTunnelGameOver()
    elif save3loc=="NobodySavesYou":
        NobodySavesYou()
    elif save3loc=="BananaDeath":
        BananaDeath()
    elif save3loc=="ISleep":
        ISleep()
    elif save3loc=="DonkeyKongGameOver":
        DonkeyKongGameOver()
    elif save3loc=="ChungusHouseDeath":
        ChungusHouseDeath()
    elif save3loc=="nogoldbook":
        nogoldbook()
    elif save3loc=="OatmealDeath":
        OatmealDeath()
    elif save3loc=="OatmealDeath2":
        OatmealDeath2()
    elif save3loc=="TheEnd":
        TheEnd()
def debugload():
    youritems.clear()
    for x in saveitems:
        youritems.append(x)
    if savedebugloc=="gamestart":
        gamestart()
    elif savedebugloc=="startcave":
        startcave()
    elif savedebugloc=="caveentrance":
        caveentrance()
    elif savedebugloc=="ChungusResponse":
        ChungusResponse()
    elif savedebugloc=="uphilldownhill":
        uphilldownhill()
    elif savedebugloc=="uphill":
        uphill()
    elif savedebugloc=="BananaTempleEntrance":
        BananaTempleEntrance()
    elif savedebugloc=="BananaTempleThanks":
        BananaTempleThanks()
    elif savedebugloc=="BananaTempleLeave":
        BananaTempleLeave()
    elif savedebugloc=="TempleTunnelMain":
        TempleTunnelMain()
    elif savedebugloc=="TunnelMain":
        TunnelMain()
    elif savedebugloc=="TempleTunnelLeft":
        TempleTunnelLeft()
    elif savedebugloc=="TempleTunnelRight":
        TempleTunnelRight()
    elif savedebugloc=="TempleTunnelExitMain":
        TempleTunnelExitMain()
    elif savedebugloc=="Field":
        Field()
    elif savedebugloc=="Walmart":
        Walmart()
    elif savedebugloc=="CaveEntranceAfterTemple":
        CaveEntranceAfterTemple()
    elif savedebugloc=="returnToCave":
        returnToCave()
    elif savedebugloc=="BigChungusSavesYou":
        BigChungusSavesYou()
    elif savedebugloc=="gotohouse":
        gotohouse()
    elif savedebugloc=="houseentrance":
        houseentrance()
    elif savedebugloc=="teaquestion":
        teaquestion()
    elif savedebugloc=="teaburn":
        teaburn()
    elif savedebugloc=="teamedgood":
        teamedgood()
    elif savedebugloc=="booksign":
        booksign()
    elif savedebugloc=="leaveportal":
        leaveportal()
    elif savedebugloc=="portalyes":
        portalyes()
    elif savedebugloc=="portalno":
        portalno()
    elif savedebugloc=="portalcastle":
        portalcastle()
    elif savedebugloc=="portalcastle2":
        portalcastle2()
    elif savedebugloc=="portalcastle3":
        portalcastle3()
    elif savedebugloc=="portalcastle4":
        portalcastle4()
    elif savedebugloc=="portalcastle5":
        portalcastle5()
    elif savedebugloc=="downhillgameover":
        downhillgameover()
    elif savedebugloc=="teaburnfaint":
        teaburnfaint()
    elif savedebugloc=="TempleTunnelGameOver":
        TempleTunnelGameOver()
    elif savedebugloc=="NobodySavesYou":
        NobodySavesYou()
    elif savedebugloc=="BananaDeath":
        BananaDeath()
    elif savedebugloc=="ISleep":
        ISleep()
    elif savedebugloc=="DonkeyKongGameOver":
        DonkeyKongGameOver()
    elif savedebugloc=="ChungusHouseDeath":
        ChungusHouseDeath()
    elif savedebugloc=="nogoldbook":
        nogoldbook()
    elif savedebugloc=="OatmealDeath":
        OatmealDeath()
    elif savedebugloc=="OatmealDeath2":
        OatmealDeath2()
    elif savedebugloc=="TheEnd":
        TheEnd()
time.sleep(1)
gamestart()