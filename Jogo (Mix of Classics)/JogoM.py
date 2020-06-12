# -*- coding: utf-8 -*-
"""

Autores: Keiya Nishio e Pedro Drumond
"""
#### Precisamos fazer
# fazer as paredes
# colisão entre os players
# vidas dos players
# mostrar as vidas
# tela de vencedor

## Iterações
# adicionar pontos
# mostrar os pontos

import pygame
import random

import FunçõesM as funcoes

from ConfiguraçõesM import Config 
from Player1M import Player1
from Player2M import Player2
from MapaM import Mapa

# puxa as configurações
CONFIGURACOES = Config()
TEXTOS = CONFIGURACOES.textos
CORES = CONFIGURACOES.cores

# roda o jogo
def rodar():

    #### INICIALIZA O JOGO ####
    # colocar essa música na tela de load https://www.youtube.com/watch?v=-bzWSJG93P8
    pygame.init()
    pygame.mixer.init()

    TELA = pygame.display.set_mode((CONFIGURACOES.largura_tela, CONFIGURACOES.altura_tela))
    CLOCK = pygame.time.Clock()

    pygame.display.set_caption(CONFIGURACOES.titulo_jogo)

    # inicialização de imagens  ------>  ainda precisamos ajeitar o mapa
    #MAPA = pygame.image.load('mapa.png').convert_alpha() #mudar mapa de fundo


    # booleanos do programa
    RODANDO = True
    TELA_INICIAL = True
    GAME_OVER = False

    # inicializando objetos
    MAPA = Mapa(TELA, CONFIGURACOES)           # chama a função para colocar o mapa de fundo
    PLAYER1 = Player1(TELA, CONFIGURACOES)
    PLAYER2 = Player2(TELA, CONFIGURACOES)    
    funcoes.init(CONFIGURACOES, TELA, PLAYER1, PLAYER2)

    #musica_starwars = pygame.mixer.music.load('') 
    musica_slide64 = pygame.mixer.music.load('slider-remix.mp3') 

    # apresenta a tela de início
    funcoes.apresenta_tela_inicial()

    ## LOOP PRINCIPAL ##
    #pygame.mixer.music.play()
    while RODANDO:
        
        CLOCK.tick(CONFIGURACOES.FPS)

        # atualiza booleanos do jogo
        TELA_INICIAL, RODANDO = funcoes.checa_eventos(TELA_INICIAL, GAME_OVER, RODANDO)

        # LOOP DO JOGO
        if not GAME_OVER and not TELA_INICIAL: 
            
            TELA.fill(CORES.fundo)
            MAPA.tela_jogando(TELA)
            #Map.desenha_grid(TELA)

            PLAYER1.update() # atualiza posição do player1
            PLAYER2.update() # atualiza posição do player2

            TELA.blit(PLAYER1.image, PLAYER1.rect)
            TELA.blit(PLAYER2.image, PLAYER2.rect)

        elif GAME_OVER:
            pass

        pygame.display.flip()


rodar()

            