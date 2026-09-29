import pygame
import sys 
import random

# 1. Inicializar o Pygame
pygame.init()
fonte = pygame.font.SysFont(None, 36)

# Configurar a janela do jogo
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da  Cobrinha - Versão 1.4")

# Relógio para controlar a velocidade do jogo 
relogio = pygame.time.Clock()

# Cores (RGB)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRACO = (255, 255, 255)

# Configurações da  cobra
tamanho_bloco = 20 # Tamanho de cada segmento da cobra (20x20 pixels)
velocidade = 10 # Velocidade da cobra (quantos pixels se move por frame)

# Fontes
fonte_pontos = pygame.font.SysFont("arial", 25)
fonte_game_over = pygame.font.SysFont("arial", 40, bold=True)

# FUNÇÃO PARA GERAR COMIDA ALEATÓRIA
def gerar_comida():
    x = random.randint(0, (LARGURA - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
    y = random.randint(0, (ALTURA - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
    return [x, y]

def rodar_jogo():
    # Estado inicial do jogo
    cobra = [[300, 200], [280, 200], [260, 200]]
    direcao = "DIREITA" # Direção inicial da cobra
    comida = gerar_comida() # Gerar a primeira comida
    pontos = 0 # Pontuação inicial
    game_over = False # Indica se a cobra bateu
    while True:
        while game_over:
            tela.fill(PRETO)
            texto_fim = fonte_game_over.render("GAME OVER!", True, BRACO)
            texto_placar = fonte_pontos.render(f"Pontos: {pontos}", True, BRACO)
            texto_reiniciar = fonte_pontos.render("R: reiniciar   Q: sair", True, BRACO)
            tela.blit(texto_fim, (LARGURA // 2 - texto_fim.get_width() // 2, 100))
            tela.blit(texto_placar, (LARGURA // 2 - texto_placar.get_width() // 2, 180))
            tela.blit(texto_reiniciar, (LARGURA // 2 - texto_reiniciar.get_width() // 2, 260))
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:
                        rodar_jogo()
                    elif evento.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != "BAIXO":
                    direcao = "CIMA"
                elif evento.key == pygame.K_DOWN and direcao != "CIMA":
                    direcao = "BAIXO"
                elif evento.key == pygame.K_LEFT and direcao != "DIREITA":
                    direcao = "ESQUERDA"
                elif evento.key == pygame.K_RIGHT and direcao != "ESQUERDA":
                    direcao = "DIREITA"

        cabeca_x, cabeca_y = cobra[0]
        if direcao == "CIMA":
            cabeca_y -= tamanho_bloco
        elif direcao == "BAIXO":
            cabeca_y += tamanho_bloco
        elif direcao == "ESQUERDA":
            cabeca_x -= tamanho_bloco
        elif direcao == "DIREITA":
            cabeca_x += tamanho_bloco

        nova_cabeca = [cabeca_x, cabeca_y]
        hit_parede = cabeca_x < 0 or cabeca_x >= LARGURA or cabeca_y < 0 or cabeca_y >= ALTURA
        hit_corpo = nova_cabeca in cobra
        if hit_parede or hit_corpo:
            game_over = True
            continue

        cobra.insert(0, nova_cabeca)
        if nova_cabeca == comida:
            pontos += 1
            comida = gerar_comida()
        else:
            cobra.pop()

        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, pygame.Rect(comida[0], comida[1], tamanho_bloco, tamanho_bloco))
        for segmento in cobra:
            pygame.draw.rect(tela, VERDE, pygame.Rect(segmento[0], segmento[1], tamanho_bloco, tamanho_bloco))
        texto_placar = fonte_pontos.render(f"Pontos: {pontos}", True, BRACO)
        tela.blit(texto_placar, (10, 10))
        pygame.display.flip()
        relogio.tick(velocidade)


rodar_jogo()