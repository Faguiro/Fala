#!/usr/bin/env python3
# Anchor extraction from HTML document
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pygame
from gtts import gTTS
import os


with urlopen('https://www.webnode.com.br/') as response:
    soup = BeautifulSoup(response, 'html.parser')
   # for anchor in soup.find_all('a'):
    texto=soup.get_text()
    print(texto)
    

        #print(anchor.get('href', '/'))

arquivo = open('arq01.txt','w', encoding = 'utf-8')

str(arquivo.write(texto)).encode(encoding='UTF-8',errors='strict')

arquivo.close()


    

voz=gTTS (str(texto), lang="pt-BR")
voz.save('voz.mp3')

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('voz.mp3')
pygame.mixer.music.play()
pygame.event.wait()

