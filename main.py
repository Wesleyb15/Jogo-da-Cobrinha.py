import pygame
import sys 

# Inicializar o Pygame
pygame.init()

# Configurar a janela do jogo
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da  Cobrinha - Versão 1.2")

# Relógio para controlar a velocidade do jogo 
relogio = pygame.time.Clock()

# Definir as cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Configurações da  cobra
tamanho_bloco = 20 # Tamanho de cada segmento da cobra (20x20 pixels)

# O corpo é lista de coordenadas (x, y)
# A cabeça da cobra é o primeiro elemento da lista (cobra[0])
cobra = [[300, 200], [280, 200], [260, 200]]

#Direção inicial
direcao = "DIREITA"

# Loop principal do jogo
while True:
    # A. Capturar eventos do teclado
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

    # B. Lógica de movimento da cobra
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

    # Remover o último segmento da cobra (para simular o movimento)
    cobra.pop()

    # C. Desenhar a cobra na tela
    tela.fill(PRETO)

    for segmento in cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            (segmento[0], segmento[1], tamanho_bloco, tamanho_bloco),
        )

    pygame.display.flip()

    # Reduzir a velocidade do jogo para 10 FPS
    relogio.tick(10)

