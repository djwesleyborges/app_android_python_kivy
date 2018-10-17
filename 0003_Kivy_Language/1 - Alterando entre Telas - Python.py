# coding: utf-8


import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Tela1(BoxLayout):  # Extendendo o gerenciador de Layout de BoxLayout
    #  Alterna Tela1 para Tela 2
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)  # Remove a tela atual da tela
        janela.root_window.add_widget(Tela2())  # Adiciona a Tela2 na nova tela

    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs) # Cria uma nova instancia de Tela1
        self.orientation = "vertical"  # Criando o botão na vertical da tela
        bt1 = Button(text="Clique")  # Criando um novo Botão com label Clique
        self.add_widget(bt1)  # Adicionando este botão a tela
        bt1.on_press = self.on_press_bt  # Quando o botão e precionado, ele invota a função on_press_bt
        self.add_widget(Button(text="bt2"))  # Criando novo botão sem ação
        self.add_widget(Button(text="bt3"))  # Criando novo botão sem ação


class Tela2(BoxLayout):
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)  # Remove a tela atual da tela
        janela.root_window.add_widget(Tela1())  # Adiciona a Tela2 na nova tela

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.orientation = "vertical"
        bt = Button(text="Clique")
        bt.on_press = self.on_press_bt
        self.add_widget(bt)


class KVvsPY(App):  # Classe principal, que herda de App
    def build(self):
        return Tela1()  # Invocando a Classe Tela1


janela = KVvsPY()
janela.run()
