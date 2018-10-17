#coding: utf-8

# autor: Wesley Borges


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

def click():
    print(ed.text)

def build():
    layout = FloatLayout()
    ed = TextInput(text="eXcript")
    global ed
    ed.size_hint = None, None
    bt = Button(text="Clique Aqui")
    bt.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 100
    ed.y = 250

    layout.add_widget(ed)
    layout.add_widget(bt)
    bt.width = 200
    bt.height = 50
    bt.x = 200
    bt.y = 150
    bt.on_press = click # Evento do botão, chamando a função click


    return layout


janela = App()
janela.title = "eXcript" # Titulo da Janela
Window.size = 600,600


janela.build = build
janela.run()