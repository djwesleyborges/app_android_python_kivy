#coding: utf-8
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    def click(self):
        print("OI")
        self.ids.lb1.text = ""  # Colocando o label do botão 1 vazio pela propriedade "ids"
        self.ids.lb2.text = "10"  # Colocando o label do botão 2 com valor 10 pela propriedade "ids"

class Estudo4App(App):
    pass


janela = Estudo4App()
janela.run()