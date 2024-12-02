import pygame
import sys
from classes import  Jogo  # Certifique-se de que classes.py está correto
from constants import WIDTH, HEIGHT, WHITE, YELLOW, BLACK  # Verifique se constants.py está correto

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Vida Adulta")

game = Jogo()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clique esquerdo
            pos = event.pos

            # Verificar clique no botão Oráculo
            if game.oraculo_button.is_clicked(pos):
                print("Botão Oráculo clicado")
                game.show_oraculo = not game.show_oraculo
                if not game.show_oraculo:
                    game.dica_atual = None

            # Verificar clique nos botões das alternativas
            if not game.capa and not game.show_oraculo:
                questao = game.fases[game.fase_atual].get_questao_atual()
                if questao:
                    for i, alternativa in enumerate(questao.alternativas):
                        button_rect = pygame.Rect(10, 130 + i * 59, 355, 39)
                        if button_rect.collidepoint(pos):
                            print(f"Alternativa {i} clicada!")
                            resultado = game.fases[game.fase_atual].resposta_questao(i)
                            game.processa_resposta(resultado)
                            break

            # Verificar clique no botão de "Jogar Agora" ou "Reiniciar"
            if game.capa:
                if game.play_button.is_clicked(pos):
                    game.inicia_jogo()

    # Atualizar tela e desenhar elementos
    
    screen.fill(WHITE)
    game.draw(screen)
    pygame.display.flip()


pygame.quit()
sys.exit()