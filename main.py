import pygame

# omg let's make this oopmaxxing

pygame.init()

# icon
icon = pygame.image.load("ui/icon.png")
pygame.display.set_icon(icon) 


white = (238,237,253)
black = (24, 14, 75)
blue = (46, 150, 255)
purple = (120, 146, 255)
cyan = (27,238,248)
pink = (244, 147, 242)
orange = (255, 198, 204)
yellow = (228,250,202)


class BorderThing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf= pygame.Surface((160,20))
        # self.surf.fill(colourpalette[bgindex])        

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



pfpArea = pygame.Surface((500,500))
pfpArea.fill(palette[bgindex])

basecat = pygame.image.load(f"art/body{bodyindex}.png").convert_alpha()
pfpArea.blit(basecat,(0,0))

eyes = pygame.image.load("art/eye2png.png").convert_alpha()
pfpArea.blit(eyes,(0,0))

screen.blit(pfpArea,(20,20))
pygame.draw.rect(screen, black, [20, 20, 500, 500], 1)

font = pygame.font.Font("ui/comic.ttf",20)
title = font.render("hi welcome to my stoopid lah pfp maker", True, black)
screen.blit(title, (540,60))
text1 = font.render("in this game you dress up a cat that does", True, black)
text2 = font.render("NOT look suspiciously like a boykisser", True, black)
screen.blit(text1, (540, 90))
screen.blit(text2, (540, 110))


running = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # idea: select the thing to change and use arrow keys???
        # later
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bgindex+= 1
                if(bgindex > 7):
                    bgindex = 0
                pfpArea.fill(palette[bgindex])
                basecat = pygame.image.load(f"art/body{bodyindex}.png").convert_alpha()
                pfpArea.blit(basecat,(0,0))
                pfpArea.blit(eyes,(0,0))
                screen.blit(pfpArea,(20,20))
    # keys = pygame.key.get_pressed()

    # if(keys[pygame.K_a]):
    #     bodyindex += 1
    #     if(bodyindex > 3):
    #         bodyindex = 0
    #     body = pygame.image.load(f"art/body{bodyindex}.png").convert_alpha()
    #     pfpArea.blit(body,(0,0))
    #     screen.blit(pfpArea,(20,20))
    #     pygame.display.update()




pygame.quit()