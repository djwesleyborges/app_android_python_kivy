# coding: utf-8
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')


class Tela1(BoxLayout):  # Extendendo o gerenciador de Layout de BoxLayout
    #  Alterna Tela1 para Tela 2
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)  # Remove a tela atual da tela
        janela.root_window.add_widget(Tela2())  # Adiciona a Tela2 na nova tela


class Tela2(BoxLayout):
    def on_press_bt(self):
        janela.root_window.remove_widget(janela.root)  # Remove a tela atual da tela
        janela.root_window.add_widget(Tela1())  # Adiciona a Tela2 na nova tela


class KVvsPY(App):  # Classe principal, que herda de App
    def build(self):
        return Tela1()  # Invocando a Classe Tela1


janela = KVvsPY()
janela.run()
