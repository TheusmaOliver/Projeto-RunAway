import sys
from time import sleep
import pygame


class Funções:
    def __init__(self, *args, genero, **kwargs):
        super().__init__(*args, **kwargs)
        self.genero = genero

    def animation(self, frase):
        for cont in frase:
            print(cont, end='')
            sys.stdout.flush()
            sleep(0.05)

    def generos(self):
        if self.genero == 'masculino':
            return 'o'
        elif self.genero == 'feminino':
            return 'a'
        else:
            return 'e'

    def teclando(self):
        tecla = pygame.mixer.Sound('_music/teclado.ogg')
        return tecla
