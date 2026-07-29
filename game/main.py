import pygame
import random

# omg let's make this oopmaxxing

pygame.init()

# icon
icon = pygame.image.load("game/ui/icon.png")
pygame.display.set_icon(icon) 


white = (238,237,253)
black = (24, 14, 75)
blue = (46, 150, 255)
purple = (120, 146, 255)
cyan = (27,238,248)
pink = (244, 147, 242)
orange = (255, 198, 204)
yellow = (228,250,202)

counts = [("body",4), ("eye", 6), ("mouth", 7),("decor",6)]
# one less than amount for indexing
# haha six seven

class BorderThing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf= pygame.Surface((160,20))
        # self.surf.fill(colourpalette[bgindex])        

class BigButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((360,40))
        self.surf.fill(pink)

palette = [white,black,blue,purple,cyan,pink,orange,yellow]
colourpalette = [blue,purple,cyan,pink,orange,yellow]
# 960/6 = 160
bgindex = 0
bodyindex = 1


screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("SILLY PFP MAKER :3")
screen.fill(white)

for i in range(6):
    thing = BorderThing()
    thing.surf.fill(colourpalette[i])
    screen.blit(thing.surf,(i*160, 0))
    screen.blit(thing.surf,(i*160, 520))

savebutton = pygame.image.load("game/ui/savebutton.png").convert_alpha()
screen.blit(savebutton,(540,460))

pinkbutton = pygame.image.load("game/ui/button.png").convert_alpha()
screen.blit(pinkbutton, (630,150))

pfpArea = pygame.Surface((500,500))
pfpArea.fill(palette[bgindex])
pfpArea.blit(pygame.image.load("game/art/halftonebg.png").convert_alpha(),(0,0))


basecat = pygame.image.load(f"game/art/body{bodyindex}.png").convert_alpha()
pfpArea.blit(basecat,(0,0))

eyes = pygame.image.load("game/art/eye0.png").convert_alpha()
pfpArea.blit(eyes,(0,0))

mouth = pygame.image.load("game/art/mouth0.png").convert_alpha()
pfpArea.blit(mouth,(0,0))

screen.blit(pfpArea,(20,20))
# pygame.draw.rect(screen, black, [20, 20, 500, 500], 1)

font = pygame.font.Font("game/ui/comic.ttf",20)
title = font.render("hi welcome to my silly mini pfp maker", True, black)
screen.blit(title, (540,60))
text1 = font.render("in this game you gamble a cat.", True, black)
text2 = font.render("", True, black)
screen.blit(text1, (540, 90))
screen.blit(text2, (540, 110))

text3 = font.render("click the button above for a random cat :)", True, black)
screen.blit(text3,(540,420))

def updatePfp():
    global pfpArea
    global basecat,eyes, mouth
    global screen
    pfpArea.fill(palette[bgindex])
    pfpArea.blit(pygame.image.load("game/art/halftonebg.png").convert_alpha(),(0,0))
    pfpArea.blit(basecat,(0,0))
    pfpArea.blit(eyes,(0,0))
    pfpArea.blit(mouth,(0,0))
    screen.blit(pfpArea,(20,20))

def randomPfp():
    global pfpArea
    global basecat,eyes, mouth
    global counts
    global screen
    global bgindex
    bgindex = random.randint(0,7)
    pfpArea.fill(palette[bgindex])
    bgpattern = random.randint(0,4)
    # hardcoding here I goo
    if(bgpattern == 1):
        pfpArea.blit(pygame.image.load("game/art/halftonebg.png").convert_alpha(),(0,0))
    if(bgpattern == 2):
        pfpArea.blit(pygame.image.load("game/art/ditherbg.png").convert_alpha(),(0,0))
    if(bgpattern == 3):
        pfpArea.blit(pygame.image.load("game/art/gridbg.png").convert_alpha(),(0,0))
    if(bgpattern == 4):
        pfpArea.blit(pygame.image.load("game/art/linesbg.png").convert_alpha(),(0,0))
    for thing in counts:
        pfpArea.blit(pygame.image.load(f"game/art/{thing[0]}{random.randint(0,thing[1])}.png").convert_alpha(),(0,0))

    screen.blit(pfpArea,(20,20))

running = True
saved = 0
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
                whee = pygame.mouse.get_pos()
                if(whee[0] > 630 and whee[0] < 870 and whee[1] > 150 and whee[1] < 390):
                    randomPfp() 
                elif(whee[0] > 540 and whee[0] < 900 and whee[1] > 460 and whee[1] < 500):
                    pygame.image.save(pfpArea, f"random_herbycat_pfp{saved}.png")
                    saved += 1


pygame.quit()