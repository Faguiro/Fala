import speech_recognition as sr
from gtts import gTTS
import os
import time
from playsound import playsound
import tkinter as tk
from tkinter import *
import random
global texto
#root=TK()

root=Tk()

class App:
    texto="Olá!"
    #Funcao responsavel por falar 
    def cria_audio(texto):
            r1 = random.randint(1,10000000)
            r2 = random.randint(1,10000000)
            randfile = str(r2)+"randomtext"+str(r1) +".mp3"
    
            tts = gTTS(texto,lang='pt-br')
            #Salva o arquivo de audio
            tts.save(randfile)
            
            print("Estou aprendendo o que você disse...")
            #Da play ao audio
            

            playsound(randfile,True)
            time.sleep(10)
            os.remove(randfile)
            print('ok')
            


    #Funcao responsavel por ouvir e reconhecer a fala
            

    def ouvir_microfone():
            #Habilita o microfone para ouvir o usuario
            microfone = sr.Recognizer()
            with sr.Microphone() as source:
                    #Chama a funcao de reducao de ruido disponivel na speech_recognition
                    microfone.adjust_for_ambient_noise(source)
                    #Avisa ao usuario que esta pronto para ouvir
                    print("Diga alguma coisa: ")
                    #Armazena a informacao de audio na variavel
                    audio = microfone.listen(source)                    
                  


            try:
                    #Passa o audio para o reconhecedor de padroes do speech_recognition
                    frase = microfone.recognize_google(audio,language='pt-BR')
                    #Após alguns segundos, retorna a frase falada
                    print("Você disse: " + frase)
                    App.texto =frase
                    

                    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
            except:
                    print("Não entendi")

    def fala():
        app=App
        txt=app.texto
        app.cria_audio(txt)
root.geometry=('500x500+200+200')

botao_mic=tk.Button (text="Mic", command=App.ouvir_microfone)
botao_mic.place(x=20, y=20)  

botao_mic=tk.Button (text="Fala", command=App.fala)
botao_mic.place(x=60, y=20)  

root.mainloop()


#frase = ouvir_microfone()
#cria_audio(frase)


#root.mainloop()
