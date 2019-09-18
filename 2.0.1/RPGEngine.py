import pygame

pygame.init()
pygame.display.set_caption("Random Story")
gameDisplay=pygame.display.set_mode((512,512))
OatmealLogo=pygame.image.load('logos/OatmealLogo.png')
PythonPygameLogo=pygame.image.load('logos/PythonPygameLogo.png')
newlocation=True
def fadein(width, height,image): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 50):
        fade.set_alpha(300-alpha*6)
        gameDisplay.blit((pygame.transform.scale(image,(512,512))),(0,0))
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
fadein(512,512,OatmealLogo)
def fadeout(width, height,image): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 50):
        fade.set_alpha(alpha*6)
        gameDisplay.blit((pygame.transform.scale(image,(512,512))),(0,0))
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
pygame.display.update()
purple=pygame.image.load('tiles/purple.png')
black=pygame.image.load('tiles/black.png')
transparent=pygame.image.load('tiles/transparent.png')
location="cave"
player=pygame.image.load("entities/playerdown.png")
playerlocx=64
playerlocy=64
wHeld=aHeld=sHeld=dHeld=shiftHeld=False
playerlocinfo=[64,64,96,96]
playerlocinfoprev=[64,64,96,96]
Gridx=Gridy=[32,64,96,128,160,192,224,256,288,320,352,384,416,448,480,512,0,0]
menu=EnterPress=False
menuSelection=1
youritems=[]
#region
def giveitem(itm):
    youritems.append(itm)
def cutscene(number):
    if number==1:
        for x in range(0,32):
            resetdisplay(True)
            gameDisplay.blit(((pygame.transform.scale(player,(32-x,32-x)))),(playerlocx+(x/2),playerlocy+(x/2)))
            pygame.display.update()

def removeitem(itm):
    youritems.remove(items[itm])

def changelocation(loc,playerlocationx,playerlocationy):
    gameDisplay.fill((255,255,255))
    pygame.display.update()
    global location
    global playerlocx
    global playerlocy
    global newlocation
    location=loc
    playerlocx=playerlocationx
    playerlocy=playerlocationy
    newlocation=True
    pygame.time.delay(250)

def checkhaveitem(itm):
    if itm in youritems:
        return True
    else:
        return False

def resetdisplay(noplayer=False):
    gameDisplay.fill((20,20,20))
    for x in range(0,16):
        gameDisplay.blit((pygame.transform.scale(Grid_A[x],(32,32))),(x*32,0))
        gameDisplay.blit((pygame.transform.scale(Grid_B[x],(32,32))),(x*32,32))
        gameDisplay.blit((pygame.transform.scale(Grid_C[x],(32,32))),(x*32,64))
        gameDisplay.blit((pygame.transform.scale(Grid_D[x],(32,32))),(x*32,96))
        gameDisplay.blit((pygame.transform.scale(Grid_E[x],(32,32))),(x*32,128))
        gameDisplay.blit((pygame.transform.scale(Grid_F[x],(32,32))),(x*32,160))
        gameDisplay.blit((pygame.transform.scale(Grid_G[x],(32,32))),(x*32,192))
        gameDisplay.blit((pygame.transform.scale(Grid_H[x],(32,32))),(x*32,224))
        gameDisplay.blit((pygame.transform.scale(Grid_I[x],(32,32))),(x*32,256))
        gameDisplay.blit((pygame.transform.scale(Grid_J[x],(32,32))),(x*32,288))
        gameDisplay.blit((pygame.transform.scale(Grid_K[x],(32,32))),(x*32,320))
        gameDisplay.blit((pygame.transform.scale(Grid_L[x],(32,32))),(x*32,352))
        gameDisplay.blit((pygame.transform.scale(Grid_M[x],(32,32))),(x*32,384))
        gameDisplay.blit((pygame.transform.scale(Grid_N[x],(32,32))),(x*32,416))
        gameDisplay.blit((pygame.transform.scale(Grid_O[x],(32,32))),(x*32,448))
        gameDisplay.blit((pygame.transform.scale(Grid_P[x],(32,32))),(x*32,480))
    if noplayer==False:
        gameDisplay.blit((pygame.transform.scale(player,(32,32))),(playerlocx,playerlocy))

def textbox(text,position="bottom"):
    if position=="top":
        pygame.draw.rect(gameDisplay, (255,255,255), ((4,4),(504,100)),5)
        pygame.draw.rect(gameDisplay, (255,255,255), ((12,12),(488,84)))
        blit_text(gameDisplay, text, (16, 16), pygame.font.SysFont('arial', int(32/2)))
    elif position=="bottom":
        pygame.draw.rect(gameDisplay, (255,255,255), ((4,408),(504,100)),5)
        pygame.draw.rect(gameDisplay, (255,255,255), ((12,416),(488,84)))
        blit_text(gameDisplay, text, (16, 420), pygame.font.SysFont('arial', int(32/2)))

def yesno(yesnoSelection=0,position="bottom",quit=False):
    nonselected=True
    EnterPress=False
    while nonselected:
        if position=="bottom":
            pygame.draw.rect(gameDisplay, (255,255,255), ((444,308),(64,92)),5)
            pygame.draw.rect(gameDisplay, (255,255,255), ((452,316),(48,76)))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if quit==False:
                    quitgame()
                elif quit==True:
                    pygame.quit()
                    raise SystemExit

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    yesnoSelection-=1
                if event.key == pygame.K_s:
                    yesnoSelection+=1
                if event.key == pygame.K_RETURN:
                    EnterPress=True

        menuText=pygame.font.SysFont("arial",int(32/2))
        
        menuText1=menuText.render("Yes",True,(0,0,0))
        textRect1=menuText1.get_rect()
        if position=="bottom":
            textRect1.center=((456+(40/2),(320+(32/2))))

        menuText2=menuText.render("No",True,(0,0,0))
        textRect2=menuText2.get_rect()
        if position=="bottom":
            textRect2.center=((456+(40/2),(356+(32/2))))

        gameDisplay.blit(menuText1,textRect1)
        gameDisplay.blit(menuText2,textRect2)

        if yesnoSelection==-1:
            yesnoSelection=1
        elif yesnoSelection==2:
            yesnoSelection=0
        if yesnoSelection==0:
            if position=="bottom":
                pygame.draw.rect(gameDisplay, (0,0,0), ((456,320),(40,32)),5)
        if yesnoSelection==1:
            if position=="bottom":
                pygame.draw.rect(gameDisplay, (0,0,0), ((456,356),(40,32)),5)
        if EnterPress and yesnoSelection==0:
            EnterPress=False
            nonselected=False
            return True
        if EnterPress and yesnoSelection==1:
            EnterPress=False
            nonselected=False
            return False
        pygame.display.update()
    
def quitgame():
    resetdisplay()
    textbox("Are you sure you want to quit?")
    if yesno(1,"bottom",True):
        pygame.quit()
        raise SystemExit

def blit_text(surface, text, pos, font, color=(0,0,0)):
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

def inventory():
    global menu
    inventoryOpen=True
    while inventoryOpen:
        gameDisplay.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitgame()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inventoryOpen=False
                    menu=False
        pygame.draw.rect(gameDisplay, (255,255,255), ((4,4),(504,504)),5)
        pygame.draw.rect(gameDisplay, (255,255,255), ((12,12),(488,488)))

        itemList=""
        for item in youritems:
            itemList=itemList+item+"\n"
        blit_text(gameDisplay, itemList, (16, 16), pygame.font.SysFont('arial', int(32/2)))

        pygame.display.update()
#endregion
def newloc():
    try:
        global Grid_A,Grid_B,Grid_C,Grid_D,Grid_E,Grid_F,Grid_G,Grid_H,Grid_I,Grid_J,Grid_K,Grid_L,Grid_M,Grid_N,Grid_O,Grid_P
        global WGrid_A,WGrid_B,WGrid_C,WGrid_D,WGrid_E,WGrid_F,WGrid_G,WGrid_H,WGrid_I,WGrid_J,WGrid_K,WGrid_L,WGrid_M,WGrid_N,WGrid_O,WGrid_P
        file=open("maps/"+location+".txt","r")
        lines=file.readlines()
        file.close()

        #region
        Grid_A=[(pygame.image.load("tiles/" + lines[0].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[1].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[2].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[3].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[4].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[5].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[6].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[7].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[8].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[9].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[10].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[11].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[12].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[13].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[14].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[15].rstrip('\r\n') + ".png"))]
        Grid_B=[(pygame.image.load("tiles/" + lines[16].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[17].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[18].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[19].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[20].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[21].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[22].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[23].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[24].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[25].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[26].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[27].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[28].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[29].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[30].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[31].rstrip('\r\n') + ".png"))]
        Grid_C=[(pygame.image.load("tiles/" + lines[32].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[33].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[34].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[35].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[36].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[37].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[38].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[39].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[40].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[41].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[42].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[43].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[44].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[45].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[46].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[47].rstrip('\r\n') + ".png"))]
        Grid_D=[(pygame.image.load("tiles/" + lines[48].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[49].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[50].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[51].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[52].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[53].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[54].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[55].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[56].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[57].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[58].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[59].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[60].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[61].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[62].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[63].rstrip('\r\n') + ".png"))]
        Grid_E=[(pygame.image.load("tiles/" + lines[64].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[65].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[66].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[67].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[68].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[69].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[70].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[71].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[72].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[73].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[74].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[75].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[76].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[77].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[78].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[79].rstrip('\r\n') + ".png"))]
        Grid_F=[(pygame.image.load("tiles/" + lines[80].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[81].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[82].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[83].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[84].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[85].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[86].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[87].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[88].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[89].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[90].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[91].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[92].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[93].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[94].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[95].rstrip('\r\n') + ".png"))]
        Grid_G=[(pygame.image.load("tiles/" + lines[96].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[97].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[98].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[99].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[100].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[101].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[102].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[103].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[104].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[105].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[106].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[107].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[108].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[109].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[110].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[111].rstrip('\r\n') + ".png"))]
        Grid_H=[(pygame.image.load("tiles/" + lines[112].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[113].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[114].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[115].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[116].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[117].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[118].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[119].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[120].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[121].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[122].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[123].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[124].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[125].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[126].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[127].rstrip('\r\n') + ".png"))]
        Grid_I=[(pygame.image.load("tiles/" + lines[128].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[129].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[130].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[131].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[132].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[133].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[134].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[135].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[136].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[137].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[138].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[139].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[140].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[141].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[142].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[143].rstrip('\r\n') + ".png"))]
        Grid_J=[(pygame.image.load("tiles/" + lines[144].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[145].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[146].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[147].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[148].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[149].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[150].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[151].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[152].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[153].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[154].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[155].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[156].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[157].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[158].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[159].rstrip('\r\n') + ".png"))]
        Grid_K=[(pygame.image.load("tiles/" + lines[160].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[161].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[162].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[163].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[164].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[165].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[166].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[167].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[168].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[169].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[170].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[171].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[172].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[173].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[174].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[175].rstrip('\r\n') + ".png"))]
        Grid_L=[(pygame.image.load("tiles/" + lines[176].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[177].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[178].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[179].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[180].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[181].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[182].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[183].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[184].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[185].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[186].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[187].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[188].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[189].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[190].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[191].rstrip('\r\n') + ".png"))]
        Grid_M=[(pygame.image.load("tiles/" + lines[192].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[193].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[194].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[195].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[196].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[197].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[198].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[199].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[200].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[201].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[202].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[203].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[204].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[205].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[206].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[207].rstrip('\r\n') + ".png"))]
        Grid_N=[(pygame.image.load("tiles/" + lines[208].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[209].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[210].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[211].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[212].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[213].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[214].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[215].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[216].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[217].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[218].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[219].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[220].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[221].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[222].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[223].rstrip('\r\n') + ".png"))]
        Grid_O=[(pygame.image.load("tiles/" + lines[224].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[225].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[226].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[227].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[228].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[229].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[230].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[231].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[232].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[233].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[234].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[235].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[236].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[237].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[238].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[239].rstrip('\r\n') + ".png"))]
        Grid_P=[(pygame.image.load("tiles/" + lines[240].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[241].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[242].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[243].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[244].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[245].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[246].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[247].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[248].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[249].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[250].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[251].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[252].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[253].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[254].rstrip('\r\n') + ".png")),(pygame.image.load("tiles/" + lines[255].rstrip('\r\n') + ".png"))]
        #endregion
        #region
        WGrid_A=[lines[0].rstrip('\r\n'),lines[1].rstrip('\r\n'),lines[2].rstrip('\r\n'),lines[3].rstrip('\r\n'),lines[4].rstrip('\r\n'),lines[5].rstrip('\r\n'),lines[6].rstrip('\r\n'),lines[7].rstrip('\r\n'),lines[8].rstrip('\r\n'),lines[9].rstrip('\r\n'),lines[10].rstrip('\r\n'),lines[11].rstrip('\r\n'),lines[12].rstrip('\r\n'),lines[13].rstrip('\r\n'),lines[14].rstrip('\r\n'),lines[15].rstrip('\r\n')]
        WGrid_B=[lines[16].rstrip('\r\n'),lines[17].rstrip('\r\n'),lines[18].rstrip('\r\n'),lines[19].rstrip('\r\n'),lines[20].rstrip('\r\n'),lines[21].rstrip('\r\n'),lines[22].rstrip('\r\n'),lines[23].rstrip('\r\n'),lines[24].rstrip('\r\n'),lines[25].rstrip('\r\n'),lines[26].rstrip('\r\n'),lines[27].rstrip('\r\n'),lines[28].rstrip('\r\n'),lines[29].rstrip('\r\n'),lines[30].rstrip('\r\n'),lines[31].rstrip('\r\n')]
        WGrid_C=[lines[32].rstrip('\r\n'),lines[33].rstrip('\r\n'),lines[34].rstrip('\r\n'),lines[35].rstrip('\r\n'),lines[36].rstrip('\r\n'),lines[37].rstrip('\r\n'),lines[38].rstrip('\r\n'),lines[39].rstrip('\r\n'),lines[40].rstrip('\r\n'),lines[41].rstrip('\r\n'),lines[42].rstrip('\r\n'),lines[43].rstrip('\r\n'),lines[44].rstrip('\r\n'),lines[45].rstrip('\r\n'),lines[46].rstrip('\r\n'),lines[47].rstrip('\r\n')]
        WGrid_D=[lines[48].rstrip('\r\n'),lines[49].rstrip('\r\n'),lines[50].rstrip('\r\n'),lines[51].rstrip('\r\n'),lines[52].rstrip('\r\n'),lines[53].rstrip('\r\n'),lines[54].rstrip('\r\n'),lines[55].rstrip('\r\n'),lines[56].rstrip('\r\n'),lines[57].rstrip('\r\n'),lines[58].rstrip('\r\n'),lines[59].rstrip('\r\n'),lines[60].rstrip('\r\n'),lines[61].rstrip('\r\n'),lines[62].rstrip('\r\n'),lines[63].rstrip('\r\n')]
        WGrid_E=[lines[64].rstrip('\r\n'),lines[65].rstrip('\r\n'),lines[66].rstrip('\r\n'),lines[67].rstrip('\r\n'),lines[68].rstrip('\r\n'),lines[69].rstrip('\r\n'),lines[70].rstrip('\r\n'),lines[71].rstrip('\r\n'),lines[72].rstrip('\r\n'),lines[73].rstrip('\r\n'),lines[74].rstrip('\r\n'),lines[75].rstrip('\r\n'),lines[76].rstrip('\r\n'),lines[77].rstrip('\r\n'),lines[78].rstrip('\r\n'),lines[79].rstrip('\r\n')]
        WGrid_F=[lines[80].rstrip('\r\n'),lines[81].rstrip('\r\n'),lines[82].rstrip('\r\n'),lines[83].rstrip('\r\n'),lines[84].rstrip('\r\n'),lines[85].rstrip('\r\n'),lines[86].rstrip('\r\n'),lines[87].rstrip('\r\n'),lines[88].rstrip('\r\n'),lines[89].rstrip('\r\n'),lines[90].rstrip('\r\n'),lines[91].rstrip('\r\n'),lines[92].rstrip('\r\n'),lines[93].rstrip('\r\n'),lines[94].rstrip('\r\n'),lines[95].rstrip('\r\n')]
        WGrid_G=[lines[96].rstrip('\r\n'),lines[97].rstrip('\r\n'),lines[98].rstrip('\r\n'),lines[99].rstrip('\r\n'),lines[100].rstrip('\r\n'),lines[101].rstrip('\r\n'),lines[102].rstrip('\r\n'),lines[103].rstrip('\r\n'),lines[104].rstrip('\r\n'),lines[105].rstrip('\r\n'),lines[106].rstrip('\r\n'),lines[107].rstrip('\r\n'),lines[108].rstrip('\r\n'),lines[109].rstrip('\r\n'),lines[110].rstrip('\r\n'),lines[111].rstrip('\r\n')]
        WGrid_H=[lines[112].rstrip('\r\n'),lines[113].rstrip('\r\n'),lines[114].rstrip('\r\n'),lines[115].rstrip('\r\n'),lines[116].rstrip('\r\n'),lines[117].rstrip('\r\n'),lines[118].rstrip('\r\n'),lines[119].rstrip('\r\n'),lines[120].rstrip('\r\n'),lines[121].rstrip('\r\n'),lines[122].rstrip('\r\n'),lines[123].rstrip('\r\n'),lines[124].rstrip('\r\n'),lines[125].rstrip('\r\n'),lines[126].rstrip('\r\n'),lines[127].rstrip('\r\n')]
        WGrid_I=[lines[128].rstrip('\r\n'),lines[129].rstrip('\r\n'),lines[130].rstrip('\r\n'),lines[131].rstrip('\r\n'),lines[132].rstrip('\r\n'),lines[133].rstrip('\r\n'),lines[134].rstrip('\r\n'),lines[135].rstrip('\r\n'),lines[136].rstrip('\r\n'),lines[137].rstrip('\r\n'),lines[138].rstrip('\r\n'),lines[139].rstrip('\r\n'),lines[140].rstrip('\r\n'),lines[141].rstrip('\r\n'),lines[142].rstrip('\r\n'),lines[143].rstrip('\r\n')]
        WGrid_J=[lines[144].rstrip('\r\n'),lines[145].rstrip('\r\n'),lines[146].rstrip('\r\n'),lines[147].rstrip('\r\n'),lines[148].rstrip('\r\n'),lines[149].rstrip('\r\n'),lines[150].rstrip('\r\n'),lines[151].rstrip('\r\n'),lines[152].rstrip('\r\n'),lines[153].rstrip('\r\n'),lines[154].rstrip('\r\n'),lines[155].rstrip('\r\n'),lines[156].rstrip('\r\n'),lines[157].rstrip('\r\n'),lines[158].rstrip('\r\n'),lines[159].rstrip('\r\n')]
        WGrid_K=[lines[160].rstrip('\r\n'),lines[161].rstrip('\r\n'),lines[162].rstrip('\r\n'),lines[163].rstrip('\r\n'),lines[164].rstrip('\r\n'),lines[165].rstrip('\r\n'),lines[166].rstrip('\r\n'),lines[167].rstrip('\r\n'),lines[168].rstrip('\r\n'),lines[169].rstrip('\r\n'),lines[170].rstrip('\r\n'),lines[171].rstrip('\r\n'),lines[172].rstrip('\r\n'),lines[173].rstrip('\r\n'),lines[174].rstrip('\r\n'),lines[175].rstrip('\r\n')]
        WGrid_L=[lines[176].rstrip('\r\n'),lines[177].rstrip('\r\n'),lines[178].rstrip('\r\n'),lines[179].rstrip('\r\n'),lines[180].rstrip('\r\n'),lines[181].rstrip('\r\n'),lines[182].rstrip('\r\n'),lines[183].rstrip('\r\n'),lines[184].rstrip('\r\n'),lines[185].rstrip('\r\n'),lines[186].rstrip('\r\n'),lines[187].rstrip('\r\n'),lines[188].rstrip('\r\n'),lines[189].rstrip('\r\n'),lines[190].rstrip('\r\n'),lines[191].rstrip('\r\n')]
        WGrid_M=[lines[192].rstrip('\r\n'),lines[193].rstrip('\r\n'),lines[194].rstrip('\r\n'),lines[195].rstrip('\r\n'),lines[196].rstrip('\r\n'),lines[197].rstrip('\r\n'),lines[198].rstrip('\r\n'),lines[199].rstrip('\r\n'),lines[200].rstrip('\r\n'),lines[201].rstrip('\r\n'),lines[202].rstrip('\r\n'),lines[203].rstrip('\r\n'),lines[204].rstrip('\r\n'),lines[205].rstrip('\r\n'),lines[206].rstrip('\r\n'),lines[207].rstrip('\r\n')]
        WGrid_N=[lines[208].rstrip('\r\n'),lines[209].rstrip('\r\n'),lines[210].rstrip('\r\n'),lines[211].rstrip('\r\n'),lines[212].rstrip('\r\n'),lines[213].rstrip('\r\n'),lines[214].rstrip('\r\n'),lines[215].rstrip('\r\n'),lines[216].rstrip('\r\n'),lines[217].rstrip('\r\n'),lines[218].rstrip('\r\n'),lines[219].rstrip('\r\n'),lines[220].rstrip('\r\n'),lines[221].rstrip('\r\n'),lines[222].rstrip('\r\n'),lines[223].rstrip('\r\n')]
        WGrid_O=[lines[224].rstrip('\r\n'),lines[225].rstrip('\r\n'),lines[226].rstrip('\r\n'),lines[227].rstrip('\r\n'),lines[228].rstrip('\r\n'),lines[229].rstrip('\r\n'),lines[230].rstrip('\r\n'),lines[231].rstrip('\r\n'),lines[232].rstrip('\r\n'),lines[233].rstrip('\r\n'),lines[234].rstrip('\r\n'),lines[235].rstrip('\r\n'),lines[236].rstrip('\r\n'),lines[237].rstrip('\r\n'),lines[238].rstrip('\r\n'),lines[239].rstrip('\r\n')]
        WGrid_P=[lines[240].rstrip('\r\n'),lines[241].rstrip('\r\n'),lines[242].rstrip('\r\n'),lines[243].rstrip('\r\n'),lines[244].rstrip('\r\n'),lines[245].rstrip('\r\n'),lines[246].rstrip('\r\n'),lines[247].rstrip('\r\n'),lines[248].rstrip('\r\n'),lines[249].rstrip('\r\n'),lines[250].rstrip('\r\n'),lines[251].rstrip('\r\n'),lines[252].rstrip('\r\n'),lines[253].rstrip('\r\n'),lines[254].rstrip('\r\n'),lines[255].rstrip('\r\n')]
        #endregion
    except:
        Grid_A=Grid_C=Grid_E=Grid_G=Grid_I=Grid_K=Grid_M=Grid_O=[black,purple,black,purple,black,purple,black,purple,black,purple,black,purple,black,purple,black,purple]
        Grid_B=Grid_D=Grid_F=Grid_H=Grid_J=Grid_L=Grid_N=Grid_P=[purple,black,purple,black,purple,black,purple,black,purple,black,purple,black,purple,black,purple,black]


def main():
    global newlocation,purple,black,transparent,location,player,playerlocx,playerlocy,wHeld,aHeld,sHeld,dHeld,shiftHeld,playerlocinfo,playerlocinfoprev,Gridx,Gridy,menu,EnterPress,menuSelection,youritems
    while True:
        if newlocation:
            newloc()
            newlocation=False
        gameDisplay.fill((20,20,20))
        for x in range(0,16):
            gameDisplay.blit((pygame.transform.scale(Grid_A[x],(32,32))),(x*32,0))
            gameDisplay.blit((pygame.transform.scale(Grid_B[x],(32,32))),(x*32,32))
            gameDisplay.blit((pygame.transform.scale(Grid_C[x],(32,32))),(x*32,64))
            gameDisplay.blit((pygame.transform.scale(Grid_D[x],(32,32))),(x*32,96))
            gameDisplay.blit((pygame.transform.scale(Grid_E[x],(32,32))),(x*32,128))
            gameDisplay.blit((pygame.transform.scale(Grid_F[x],(32,32))),(x*32,160))
            gameDisplay.blit((pygame.transform.scale(Grid_G[x],(32,32))),(x*32,192))
            gameDisplay.blit((pygame.transform.scale(Grid_H[x],(32,32))),(x*32,224))
            gameDisplay.blit((pygame.transform.scale(Grid_I[x],(32,32))),(x*32,256))
            gameDisplay.blit((pygame.transform.scale(Grid_J[x],(32,32))),(x*32,288))
            gameDisplay.blit((pygame.transform.scale(Grid_K[x],(32,32))),(x*32,320))
            gameDisplay.blit((pygame.transform.scale(Grid_L[x],(32,32))),(x*32,352))
            gameDisplay.blit((pygame.transform.scale(Grid_M[x],(32,32))),(x*32,384))
            gameDisplay.blit((pygame.transform.scale(Grid_N[x],(32,32))),(x*32,416))
            gameDisplay.blit((pygame.transform.scale(Grid_O[x],(32,32))),(x*32,448))
            gameDisplay.blit((pygame.transform.scale(Grid_P[x],(32,32))),(x*32,480))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    quitgame()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    wHeld=True
                if event.key == pygame.K_a:
                    aHeld=True
                if event.key == pygame.K_s:
                    sHeld=True
                if event.key == pygame.K_d:
                    dHeld=True
                if event.key ==pygame.K_LSHIFT:
                    shiftHeld=True
                if event.key == pygame.K_ESCAPE:
                    menu=True
                if event.key == pygame.K_r:
                    changelocation(location,playerlocx,playerlocy)
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_w:
                    wHeld=False
                if event.key == pygame.K_a:
                    aHeld=False
                if event.key == pygame.K_s:
                    sHeld=False
                if event.key == pygame.K_d:
                    dHeld=False
                if event.key ==pygame.K_LSHIFT:
                    shiftHeld=False

        if wHeld and shiftHeld:
            playerlocy-=8
            player=pygame.image.load("entities/playerup.png")
        elif sHeld and shiftHeld:
            playerlocy+=8
            player=pygame.image.load("entities/playerdown.png")
        elif dHeld and shiftHeld:
            playerlocx+=8
            player=pygame.image.load("entities/playerright.png")
        elif aHeld and shiftHeld:
            playerlocx-=8
            player=pygame.image.load("entities/playerleft.png")
        elif wHeld:
            playerlocy-=4
            player=pygame.image.load("entities/playerup.png")
        elif sHeld:
            playerlocy+=4
            player=pygame.image.load("entities/playerdown.png")
        elif dHeld:
            playerlocx+=4
            player=pygame.image.load("entities/playerright.png")
        elif aHeld:
            playerlocx-=4
            player=pygame.image.load("entities/playerleft.png")
        playerlocinfo=[playerlocx,playerlocy,(playerlocx+32),(playerlocy+32)]
        
        for x in range(0,16):
            if ("wall" in WGrid_A[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[0] or playerlocinfo[3]<Gridy[0]) and (playerlocinfo[1]>Gridy[0-1] or playerlocinfo[3]>Gridy[0-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[0]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[0-2]
            if ("wall" in WGrid_B[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[1] or playerlocinfo[3]<Gridy[1]) and (playerlocinfo[1]>Gridy[1-1] or playerlocinfo[3]>Gridy[1-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[1]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[1-2]
            if ("wall" in WGrid_C[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[2] or playerlocinfo[3]<Gridy[2]) and (playerlocinfo[1]>Gridy[2-1] or playerlocinfo[3]>Gridy[2-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[2]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[2-2]
            if ("wall" in WGrid_D[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[3] or playerlocinfo[3]<Gridy[3]) and (playerlocinfo[1]>Gridy[3-1] or playerlocinfo[3]>Gridy[3-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[3]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[3-2]
            if ("wall" in WGrid_E[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[4] or playerlocinfo[3]<Gridy[4]) and (playerlocinfo[1]>Gridy[4-1] or playerlocinfo[3]>Gridy[4-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[4]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[4-2]
            if ("wall" in WGrid_F[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[5] or playerlocinfo[3]<Gridy[5]) and (playerlocinfo[1]>Gridy[5-1] or playerlocinfo[3]>Gridy[5-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[5]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[5-2]
            if ("wall" in WGrid_G[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[6] or playerlocinfo[3]<Gridy[6]) and (playerlocinfo[1]>Gridy[6-1] or playerlocinfo[3]>Gridy[6-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[6]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[6-2]
            if ("wall" in WGrid_H[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[7] or playerlocinfo[3]<Gridy[7]) and (playerlocinfo[1]>Gridy[7-1] or playerlocinfo[3]>Gridy[7-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[7]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[7-2]
            if ("wall" in WGrid_I[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[8] or playerlocinfo[3]<Gridy[8]) and (playerlocinfo[1]>Gridy[8-1] or playerlocinfo[3]>Gridy[8-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[8]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[8-2]
            if ("wall" in WGrid_J[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[9] or playerlocinfo[3]<Gridy[9]) and (playerlocinfo[1]>Gridy[9-1] or playerlocinfo[3]>Gridy[9-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[9]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[9-2]
            if ("wall" in WGrid_K[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[10] or playerlocinfo[3]<Gridy[10]) and (playerlocinfo[1]>Gridy[10-1] or playerlocinfo[3]>Gridy[10-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[10]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[10-2]
            if ("wall" in WGrid_L[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[11] or playerlocinfo[3]<Gridy[11]) and (playerlocinfo[1]>Gridy[11-1] or playerlocinfo[3]>Gridy[11-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[11]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[11-2]
            if ("wall" in WGrid_M[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[12] or playerlocinfo[3]<Gridy[12]) and (playerlocinfo[1]>Gridy[12-1] or playerlocinfo[3]>Gridy[12-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[12]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[12-2]
            if ("wall" in WGrid_N[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[13] or playerlocinfo[3]<Gridy[13]) and (playerlocinfo[1]>Gridy[13-1] or playerlocinfo[3]>Gridy[13-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[13]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[13-2]
            if ("wall" in WGrid_O[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[14] or playerlocinfo[3]<Gridy[14]) and (playerlocinfo[1]>Gridy[14-1] or playerlocinfo[3]>Gridy[14-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[14]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[14-2]
            if ("wall" in WGrid_P[x]) and (playerlocinfo[0]<Gridx[x] or playerlocinfo[2]<Gridx[x]) and (playerlocinfo[0]>Gridx[x-1] or playerlocinfo[2]>Gridx[x-1]) and (playerlocinfo[1]<Gridy[15] or playerlocinfo[3]<Gridy[15]) and (playerlocinfo[1]>Gridy[15-1] or playerlocinfo[3]>Gridy[15-1]):
                if playerlocinfo[0]<playerlocinfoprev[0]:
                    playerlocx=Gridx[x]
                if playerlocinfo[1]<playerlocinfoprev[1]:
                    playerlocy=Gridy[15]
                if playerlocinfo[0]>playerlocinfoprev[0]:
                    playerlocx=Gridx[x-2]
                if playerlocinfo[1]>playerlocinfoprev[1]:
                    playerlocy=Gridy[15-2]
        gameDisplay.blit((pygame.transform.scale(player,(32,32))),(playerlocx,playerlocy))

        #region
        while menu:
            wHeld=aHeld=sHeld=dHeld=False
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quitgame()
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu=False
                    if event.key == pygame.K_w:
                        menuSelection-=1
                    if event.key == pygame.K_s:
                        menuSelection+=1
                    if event.key == pygame.K_RETURN:
                        EnterPress=True
            if menuSelection == 0:
                menuSelection = 3
            if menuSelection == 4:
                menuSelection = 1

            pygame.draw.rect(gameDisplay, (255,255,255), ((380,4),(128,256)),5)
            pygame.draw.rect(gameDisplay, (255,255,255), ((388,12),(112,240)))

            menuText=pygame.font.SysFont("arial",int(32/2))
            
            menuText1=menuText.render("Inventory",True,(0,0,0))
            textRect1=menuText1.get_rect()
            textRect1.center=((392+(104/2),(16+(32/2))))

            menuText2=menuText.render("Save",True,(0,0,0))
            textRect2=menuText2.get_rect()
            textRect2.center=((392+(104/2),(52+(32/2))))

            menuText3=menuText.render("Quit",True,(0,0,0))
            textRect3=menuText3.get_rect()
            textRect3.center=((392+(104/2),(88+(32/2))))

            gameDisplay.blit(menuText1,textRect1)
            gameDisplay.blit(menuText2,textRect2)
            gameDisplay.blit(menuText3,textRect3)

            if menuSelection==1:
                pygame.draw.rect(gameDisplay, (0,0,0), ((392,16),(104,32)),5)
            elif menuSelection==2:
                pygame.draw.rect(gameDisplay, (0,0,0), ((392,52),(104,32)),5)
            elif menuSelection==3:
                pygame.draw.rect(gameDisplay, (0,0,0), ((392,88),(104,32)),5)

            
            if menuSelection==1 and EnterPress:
                inventory()
                menu=False
                EnterPress=False
            elif menuSelection==2 and EnterPress:
                print("Save")
                menu=False
                EnterPress=False
            elif menuSelection==3 and EnterPress:
                quitgame()
                menu=False
                EnterPress=False



            pygame.display.update()
        #endregion

        pygame.time.Clock().tick(30)
        pygame.display.update()

        #cave
        if playerlocx==352 and playerlocy>=496 and location=="cave":
            changelocation("outsidecave",128,-12)

        #outsidecave
        if playerlocx==128 and playerlocy<=-16 and location=="outsidecave":
            changelocation("cave",352,492)
        if playerlocx<=-16 and 32<=playerlocy<=96 and location=="outsidecave":
            changelocation("downhill",492,playerlocy)
        if playerlocx>=496 and 32<=playerlocy<=96 and location=="outsidecave":
            changelocation("uphill",-12,playerlocy+288)

        #downhill
        if playerlocx>=496 and 32<=playerlocy<=96 and location=="downhill":
            changelocation("outsidecave",-12,playerlocy)

        #uphill
        if playerlocx<=-16 and 320<=playerlocy<=384 and location=="uphill":
            changelocation("outsidecave",492,playerlocy-288)
        if playerlocx==224 and playerlocy==192 and location=="uphill":
            changelocation("banana",240,492)

        #banana
        if 224<=playerlocx<=256 and playerlocy>=496 and location=="banana":
            changelocation("uphill",224,196)
        if playerlocx<=-16 and playerlocy==32 and location=="banana":
            changelocation("tunnel",492,32)
        
        #tunnel
        if playerlocx>=496 and playerlocy==32 and location=="tunnel":
            changelocation("banana",-12,32)
        if playerlocy>=480 and location=="tunnel":
            cutscene(1)
            changelocation("tunnelexit",playerlocx,64)

        #tunnelexit
        if 320<=playerlocx<=384 and playerlocy>=496 and location=="tunnelexit":
            changelocation("field",playerlocx,-12)

        #field
        if 320<=playerlocx<=384 and playerlocy<=-16 and location=="field":
            changelocation("tunnelexit",playerlocx,492)

        playerlocinfoprev=[playerlocx,playerlocy,(playerlocx+32),(playerlocy+32)]
        print((playerlocx,playerlocy))
pygame.time.delay(1000)
fadeout(512,512,OatmealLogo)
fadein(512,512,PythonPygameLogo)
pygame.time.delay(1000)
fadeout(512,512,PythonPygameLogo)

main()