import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo MP3
pygame.mixer.music.load('C:/Users/user/Documents/workspace/estudos/Curso_de_Python_Gustavo_Guanabara/ex021/ex021.mp3')

# Reproduzir a música
pygame.mixer.music.play()

# Esperar até que a música acabe
while pygame.mixer.music.get_busy():
    pass
