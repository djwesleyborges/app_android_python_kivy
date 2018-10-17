#coding: utf-8

# autor: Wesley Borges

from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    #return TextInput(text="Componente TextInput")
    return TextInput()

janela = App()
janela.build = build
janela.run()