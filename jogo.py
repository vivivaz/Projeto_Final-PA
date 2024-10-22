import pygame
from pygame.locals import *
from sys import exit
class Jogo_vida_adulta:
    def main():
        pygame.init()
        largura = 500
        altura = 500
        tela = pygame.display.set_mode((largura, altura))
        tempo = pygame.time.Clock()
        pygame.display.set_caption('Jogo da Vida adulta')
        x = 0
        y = 0
        fonte = pygame.font.SysFont('arialblack',45, False, True)
        titulo = fonte.render('Jogo da Vida Adulta', True, (255,110,0))
        while True:
            tela.blit(titulo, (0,200))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            tempo.tick(27)
            pygame.display.update()
            tela.fill((30,144,255))
            pygame.draw.rect(tela, (240,230,140), (x,y,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+41,y+41,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+82,y+82,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+123,y+123,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+164,y+164,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+205,y+205,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+246,y+246,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+287,y+287,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+328,y+328,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+369,y+369,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+410,y+410,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+451,y+451,40,40))
            pygame.draw.rect(tela, (240,230,140), (x,y+451,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+41,y+410,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+82,y+369,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+123,y+328,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+164,y+287,40,40))
            # pygame.draw.rect(tela, (240,230,140), (x+205,y+246,40,40))
            # pygame.draw.rect(tela, (240,230,140), (x+246,y+205,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+287,y+164,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+328,y+123,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+369,y+82,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+410,y+41,40,40))
            pygame.draw.rect(tela, (240,230,140), (x+451,y,40,40))
    main()

