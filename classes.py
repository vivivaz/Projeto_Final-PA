import pygame
import random
import sqlite3
from constants import WIDTH, HEIGHT, WHITE, YELLOW, BLACK

# Carregar imagens
capa_img = pygame.image.load("img_jogo/capa.png")
backgrounds = [pygame.image.load(f"img_jogo/fundo_{i}.png") for i in range(4)]
header_img = pygame.image.load("img_jogo/header.png")
item_img = pygame.image.load("img_jogo/item.png")
oraculo_img = pygame.image.load("img_jogo/oraculo_estat.jpg")
oraculo_img = pygame.transform.scale(oraculo_img, (WIDTH, HEIGHT))


# Classe Button para interatividade
class Button:
    def __init__(self, x, y, width, height, texto, color=YELLOW):
        self.rect = pygame.Rect(x, y, width, height)
        self.texto = texto
        self.color = color
        self.font = pygame.font.Font(None, 24)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        texto_tela = self.font.render(self.texto, True, BLACK)
        screen.blit(texto_tela, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Classe Questao para armazenar cada pergunta e opções
class Questao:
    def __init__(self, id, texto, alternativas, alternativa_correta, dica_estat, dica_vida):
        self.id = id
        self.texto = texto
        self.alternativas = alternativas
        self.alternativa_correta = alternativa_correta
        self.dica_estat = dica_estat
        self.dica_vida = dica_vida

    def is_correta(self, index):
        return index == self.alternativa_correta

# Classe Fase para gerenciar fases e perguntas
class Fase:
    def __init__(self, jogo, background, questoes):
        self.jogo = jogo  # Referência ao objeto Jogo
        self.background = background
        self.questoes = questoes
        self.respostas_corretas = 0
        self.questao_atual = None
        self.questoes_respondidas = set()
        

    def escolher_nova_questao(self):
        """Seleciona uma nova questão que ainda não foi respondida."""
        unanswered_questoes = [
            i for i, questao in enumerate(self.questoes)
            if questao.id not in self.questoes_respondidas
        ]
        print(f"Questões não respondidas: {unanswered_questoes}")  # Depuração

        if unanswered_questoes:
            self.questao_atual = random.choice(unanswered_questoes)  # Escolhe uma questão ainda não respondida
            print(f"Nova questão selecionada: {self.questao_atual}")  # Depuração
        else:
            self.questao_atual = None  # Fim da fase (todas as questões respondidas)
    def get_questao_atual(self):
        """Retorna o objeto da questão atual ou None se não disponível."""
        if self.questao_atual is not None and 0 <= self.questao_atual < len(self.questoes):
            return self.questoes[self.questao_atual]  # Aqui acessamos o índice
        return None
    
    def resposta_questao(self, resposta_index):
        """Processa a resposta do jogador e avança no jogo."""
        if self.questao_atual is not None:
            questao_atual = self.get_questao_atual()

            # Adiciona a questão à lista de respondidas
            self.questoes_respondidas.add(questao_atual.id)
            print(f"Questão respondida (ID): {questao_atual.id}")  # Depuração
            print(f"Questões respondidas até agora: {self.questoes_respondidas}")  # Depuração

            # Verifica se a resposta está correta
            if questao_atual.is_correta(resposta_index):
                self.jogo.barra_progresso += 1
                self.respostas_corretas += 1
                print(f"Resposta correta! Total corretas: {self.respostas_corretas}")  # Depuração
                if self.respostas_corretas >= 4:
                    return "next_fase"

            # Verificar se todas as questões foram respondidas
            if len(self.questoes_respondidas) >= len(self.questoes):
                # Final da fase: verificar se o jogador ganhou ou perdeu
                return "game_over" if self.respostas_corretas < 4 else "next_fase"
            else:
                # Selecionar próxima questão
                self.escolher_nova_questao()

        return

################# Funcoes para ajuste do texto ######################
def draw_text_multiline(surface, text, x, y, font, color, max_width):
    """Renderiza texto em várias linhas se ultrapassar a largura máxima."""
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)  # Adiciona a última linha

    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (x, y + i * font.get_height()))

def adjust_font_size(text, font, max_width):
    """Reduz o tamanho da fonte até o texto caber no espaço definido."""
    font_size = font.get_height()  # Começa com o tamanho atual da fonte
    while font_size > 10:  # Define um limite mínimo para o tamanho da fonte
        if font.size(text)[0] <= max_width:  # Se o texto couber na largura
            return font  # Retorna a fonte ajustada
        font_size -= 1  # Reduz o tamanho da fonte
        font = pygame.font.Font(None, font_size)  # Atualiza a fonte com o tamanho ajustado
    return pygame.font.Font(None, 10)  # Garante uma fonte mínima para evitar None

def break_text_into_lines(text, font, max_width):
    """Quebra o texto em várias linhas com base na largura máxima."""
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)  # Adiciona a última linha

    return lines

#######################

# Classe Jogo para controlar o fluxo e lógica principal
class Jogo:
    
    @staticmethod
    def carregar_questoes(fase):
        import sqlite3

        # Validar fase e mapear para a tabela correta
        tabelas_por_fase = {
            1: "QuestoesBasicas",
            2: "QuestoesIntermediarias",
            3: "QuestoesAvancadas",
        }
        tabela = tabelas_por_fase.get(fase)
        if tabela is None:
            raise ValueError(f"Fase inválida: {fase}. As fases válidas são 1, 2 ou 3.")

        try:
            # Conectar ao banco de dados
            conn = sqlite3.connect("banco_questoes.db")
            cursor = conn.cursor()

            # Consultar questões
            query = f"""
            SELECT rowid, pergunta, A, B, C, D, Gabatito, Dica_estat, Dica_vida 
            FROM {tabela}
            """
            cursor.execute(query)
            questoes = cursor.fetchall()

        except sqlite3.Error as e:
            raise RuntimeError(f"Erro ao acessar o banco de dados: {e}")

        finally:
            # Garantir que a conexão seja fechada
            if conn:
                conn.close()
        
        # Criar lista de objetos Questao
        lista_questoes = []
        for row in questoes:
            try:
                # Extrair os campos
                id, pergunta, a, b, c, d, gabarito, dica_estat, dica_vida = row
                alternativas = [a, b, c, d]

                # Validar o gabarito e converter para índice
                if gabarito not in ["A", "B", "C", "D"]:
                    raise ValueError(f"Gabarito inválido '{gabarito}' para a questão ID {id}.")

                resposta_correta = ["A", "B", "C", "D"].index(gabarito)

                # Criar e adicionar a questão
                lista_questoes.append(Questao(id, pergunta, alternativas, resposta_correta, dica_estat, dica_vida))

            except ValueError as ve:
                print(f"Erro ao processar questão (ID: {row[0]}): {ve}")

        return lista_questoes
    
    def __init__(self):
        self.capa = True
        self.fases = []
        self.fase_atual = 0
        self.barra_progresso = 0
        self.font = pygame.font.Font(None, 32)
        self.font_peq = pygame.font.Font(None, 22)  # Fonte menor para texto longo
        self.dica_atual = None
        self.show_oraculo = False
        

        # Criando as fases
        self.fases.append(Fase(self, backgrounds[1], Jogo.carregar_questoes(1)))
        self.fases.append(Fase(self, backgrounds[2], Jogo.carregar_questoes(2)))
        self.fases.append(Fase(self, backgrounds[3], Jogo.carregar_questoes(3)))  # Fase 3: Avançado

        # Botões
        self.play_button = Button(280, 280, 115, 40, "Jogar Agora")
        self.oraculo_button = Button(WIDTH - 140, HEIGHT - 60, 80, 35, "Oráculo")
        self.show_oraculo = False


    def inicia_jogo(self):
        self.capa = False
        self.fase_atual = 0
        self.barra_progresso = 0
        self.fases[self.fase_atual].respostas_corretas = 0
        self.fases[self.fase_atual].questoes_respondidas.clear()
        self.fases[self.fase_atual].escolher_nova_questao()

    def processa_resposta(self, resultado):
        """Controla o fluxo do jogo baseado na resposta."""
        print(f"Resultado da resposta: {resultado}")  # Depuração

        if resultado == "next_fase":
            self.fase_atual += 1
            self.barra_progresso += 1  # Atualiza o progresso
            print(f"Avançando para a fase: {self.fase_atual}")  # Depuração

            if self.fase_atual >= len(self.fases):
                self.capa = "win"  # O jogador venceu o jogo
                print("Jogo concluído. Você venceu!")  # Depuração
            else:
                # Inicializar a próxima fase
                self.fases[self.fase_atual].respostas_corretas = 0
                self.fases[self.fase_atual].questoes_respondidas.clear()
                self.fases[self.fase_atual].escolher_nova_questao()

        elif resultado == "game_over":
            self.capa = "game_over"  # O jogador perdeu o jogo
            print("Fim do jogo. Você perdeu!")  # Depuração

        return resultado
    
    def draw_barra_progresso(self, screen):
        # Fundo da barra de progresso
        pygame.draw.rect(screen, WHITE, (610, 0, 55, HEIGHT))

        # Desenhar os blocos de progresso
        for i in range(14):  
            color = YELLOW if i < self.barra_progresso else BLACK
            pygame.draw.rect(screen, color, (622, HEIGHT - 20 - i * 20, 20, 20))

    def draw(self, screen):
        if self.capa == True:
            screen.blit(capa_img, (0, 0))
            self.play_button.draw(screen)
        elif self.capa == "game_over":
            screen.blit(backgrounds[0], (0, 0))
            texto_tela = self.font.render("Fim de Jogo!", True, BLACK)
            screen.blit(texto_tela, (280, 180))
            self.play_button = Button(280, 280, 140, 40, "Tente outra vez")
            self.play_button.draw(screen)
        elif self.capa == "win":
            screen.blit(backgrounds[0], (0, 0))
            texto_tela = self.font.render("Você venceu!", True, BLACK)
            screen.blit(texto_tela, (280, 180))
            self.play_button = Button(280, 280, 150, 40, "Jogar novamente")
            self.play_button.draw(screen)
        
        elif self.show_oraculo:
            # Fundo do Oráculo
            screen.blit(oraculo_img, (0, 0))  

            # Caixa branca para exibir a dica
            dica_box_rect = pygame.Rect(50, HEIGHT - 150, WIDTH - 100, 100)
            pygame.draw.rect(screen, WHITE, dica_box_rect)  # Fundo branco
            pygame.draw.rect(screen, BLACK, dica_box_rect, 2)  # Borda preta

            # Obter a dica da questão atual se não definida
            if self.dica_atual is None:
                questao = self.fases[self.fase_atual].get_questao_atual()
                if questao:
                    self.dica_atual = random.choice([questao.dica_estat, questao.dica_vida])

            # Renderizar a dica dentro da caixa
            if self.dica_atual:
                draw_text_multiline(
                    screen, self.dica_atual,
                    dica_box_rect.x + 10, dica_box_rect.y + 10,
                    self.font, BLACK, dica_box_rect.width - 20
                )

            # Botão do Oráculo para voltar ao jogo
            self.oraculo_button.draw(screen)
        else:
            # Tela normal do jogo
            fase = self.fases[self.fase_atual]
            screen.blit(fase.background, (0, 0))
            questao = fase.get_questao_atual()
            if questao:
                screen.blit(header_img, (5, 15))
                header_rect = pygame.Rect(5, 15, header_img.get_width(), header_img.get_height())

                # Tamanho máximo disponível para o texto dentro da header_img
                max_width_header = header_rect.width - 20  # Margem horizontal
                max_height_header = header_rect.height - 20  # Margem vertical

                # Definir tamanho inicial da fonte
                font_size = 28  # Tamanho base da fonte para perguntas
                adjusted_font = pygame.font.Font(None, font_size)
                line_height = adjusted_font.get_height()

                # Ajustar tamanho da fonte até que o texto caiba na área da pergunta
                while True:
                    lines = break_text_into_lines(questao.texto, adjusted_font, max_width_header)
                    total_text_height = len(lines) * line_height

                    # Verificar se o texto cabe no header
                    if total_text_height <= max_height_header or font_size <= 12:  # Limite mínimo da fonte
                        break

                    # Reduzir o tamanho da fonte
                    font_size -= 2
                    adjusted_font = pygame.font.Font(None, font_size)
                    line_height = adjusted_font.get_height()

                # Renderizar e desenhar cada linha do texto da pergunta
                total_text_height = len(lines) * line_height
                start_y = header_rect.y + (header_rect.height - total_text_height) // 2  # Centralizar verticalmente

                for j, line in enumerate(lines):
                    text_surface = adjusted_font.render(line, True, WHITE)

                    # Centralizar horizontalmente
                    text_x = header_rect.x + (header_rect.width - text_surface.get_width()) // 2
                    text_y = start_y + j * line_height

                    # Desenhar o texto
                    screen.blit(text_surface, (text_x, text_y))
                for i, alternativa in enumerate(questao.alternativas):
                    button_rect = pygame.Rect(10, 130 + i * 59, 355, 39)  # Posicionamento e tamanho do botão
                    screen.blit(item_img, button_rect)  # Desenhar o item_img

                    # Tamanho máximo disponível para o texto dentro do botão
                    max_width_item = button_rect.width - 20  # Margem horizontal de 10px
                    max_height_item = button_rect.height - 10  # Margem vertical de 5px em cada lado

                    # Definir tamanho inicial da fonte
                    font_size = 32  # Tamanho base da fonte
                    adjusted_font = pygame.font.Font(None, font_size)
                    line_height = adjusted_font.get_height()

                    # Ajustar tamanho da fonte até que o texto se encaixe
                    while True:
                        lines = break_text_into_lines(alternativa, adjusted_font, max_width_item)
                        total_text_height = len(lines) * line_height

                        # Verificar se o texto cabe no botão
                        if total_text_height <= max_height_item or font_size <= 12:  # Limite mínimo da fonte
                            break

                        # Reduzir o tamanho da fonte
                        font_size -= 2
                        adjusted_font = pygame.font.Font(None, font_size)
                        line_height = adjusted_font.get_height()

                    # Renderizar e desenhar cada linha
                    total_text_height = len(lines) * line_height
                    start_y = button_rect.y + (button_rect.height - total_text_height) // 2  # Centralizar verticalmente

                    for j, line in enumerate(lines):
                        text_surface = adjusted_font.render(line, True, WHITE)

                        # Centralizar horizontalmente
                        text_x = button_rect.x + (button_rect.width - text_surface.get_width()) // 2
                        text_y = start_y + j * line_height

                        # Desenhar o texto
                        screen.blit(text_surface, (text_x, text_y))
                self.oraculo_button.draw(screen)
                self.draw_barra_progresso(screen)
        pygame.display.update() 