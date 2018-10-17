#coding: utf-8
#coding: utf-8

# autor: Wesley Borges

from kivy.app import App
from kivy.uix.button import Button

def click():
    print("O botão foi clicado")

def build():
    bt = Button(text="Clique aqui")
    bt.on_press = click # Vinculando o clique do botão a função click pelo atributo on_press
    return bt

janela = App()
janela.build = build
janela.run()