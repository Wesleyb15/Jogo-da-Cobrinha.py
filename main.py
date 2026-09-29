import pygame
import sys 

# 1. Inicializar o Pygame
pygame.init()

# 2. Configurar a janela do jogo
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo da  Cobrinha")

# 3.Relógio para controlar a velocidade do jogo 
relogio = pygame.time.Clock()

# 4. definir as cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# 5. Loop principal do jogo
while True:
    # 6. Verificar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. Desenhar na tela
    tela.fill(PRETO)
    # 9. Atualizar a tela
    pygame.display.flip()

    # 10. Controlar a velocidade do jogo
    relogio.tick(60)  # Limitar a 60 quadros por segundo

