import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
violet = (128,0,128)

dw = 1020
dh  = 720

img = pygame.image.load("sudimage.png")
img1 = pygame.image.load("1.png")
img3b = pygame.image.load("3b.png")
imgx = pygame.image.load("sudnam.png")

gameDisplay = pygame.display.set_mode((dw,dh))
pygame.display.set_caption('SUDOKU')

sfont = pygame.font.SysFont("calibri", 25)
mfont = pygame.font.SysFont("calibri", 50)
lfont = pygame.font.SysFont("bradleyhanditc", 80)

def text_objects(text,color,size):
    if size == "small":
        textSurface = sfont.render(text, True, color)
    elif size == "medium":
        textSurface = mfont.render(text, True, color)
    elif size == "large":
        textSurface = lfont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()

def mess(msg,color, y=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (dw / 2), (dh / 2)+y
    gameDisplay.blit(textSurf, textRect)

def game_start():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
   
        gameDisplay.fill(white)
        mess("Welcome to SUDOKu 2.0",violet,-100,"large")
        mess("The objective of the game is to Solve a sudoku",black,-30)

        mess("The more faster you solve, the more points you get",black,10)

        mess("c - Play & q - Quit",black,180)
    
        pygame.display.update()

        
def gameLoop():
    
    gameExit = False
    gameOver = False
    
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            mess("Game over",red,y_displace=-50,size="large")
            
            mess("C - Play \n Q - Quit",black,50,size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameDisplay.fill(white)
        gameDisplay.blit(img,(100,100))
        gameDisplay.blit(img1,(103,103))
        gameDisplay.blit(img3b,(253,103))
        gameDisplay.blit(imgx,(600,600))
        pygame.display.update()
        
    pygame.quit()

game_start()
gameLoop()
