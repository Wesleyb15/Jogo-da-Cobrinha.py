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
pygame.display.set_caption("Jogo da  Cobrinha - Versão 1.3")

# Relógio para controlar a velocidade do jogo 
relogio = pygame.time.Clock()

# Cores (RGB)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRACO = (255, 255, 255)

# Configurações da  cobra
tamanho_bloco = 20 # Tamanho de cada segmento da cobra (20x20 pixels)

# FUNÇÃO PARA GERAR COMIDA ALEATÓRIA
def gerar_comida():
    x = random.randint(0, (LARGURA - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
    y = random.randint(0, (ALTURA - tamanho_bloco) // tamanho_bloco) * tamanho_bloco
    return [x, y]
#Estado inicial do jogo
cobra = [[300, 200], [280, 200], [260, 200]] # Lista de segmentos da cobra (cada segmento é uma lista [x, y])
direcao = "DIREITA" # Direção inicial da cobra
comida = gerar_comida() # Posição inicial da comida
pontos = 0 # Pontuação inicial

# LOOP PRINCIPAL DO JOGO
while True:
    # A. CAPITURA DE EVENTOS
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

    # B. MOVIMENTAÇÃO
    # Pegar a posição da cabeça (x, y)
    cabeca_x, cabeca_y = cobra[0]

    # Atualizar a posição da cabeça com base na direção
    if direcao == "CIMA":
        cabeca_y -= tamanho_bloco
    elif direcao == "BAIXO":
        cabeca_y += tamanho_bloco
    elif direcao == "ESQUERDA":
        cabeca_x -= tamanho_bloco
    elif direcao == "DIREITA":
        cabeca_x += tamanho_bloco

    nova_cabeca = [cabeca_x, cabeca_y]

    # Adicionar a nova cabeça à cobra
    cobra.insert(0, nova_cabeca)

    # C. LÓGICA DA COMIDA E CRESCIMENTO
    if nova_cabeca == comida:
        pontos += 1
        comida = gerar_comida() # Gerar nova comida
    else:
        cobra.pop() # Remover o último segmento da cobra (não cresceu)
    # D. DESENHO DOS ELEMENTOS
    tela.fill(PRETO) # Limpar a tela

    # Desenhar a comida
    pygame.draw.rect(tela, VERMELHO, (comida[0], comida[1], tamanho_bloco, tamanho_bloco))

    # Desenhar a cobra
    for segmento in cobra:
        pygame.draw.rect(tela, VERDE, (segmento[0], segmento[1], tamanho_bloco, tamanho_bloco))
    # Desenhar o placar de pontos
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRACO)
    tela.blit(texto_pontos, (10, 10))

    pygame.display.flip() # Atualizar a tela
    relogio.tick(10) # Controlar a velocidade do jogo (10 frames por segundo)