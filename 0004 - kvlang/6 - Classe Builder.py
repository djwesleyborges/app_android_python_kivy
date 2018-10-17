# coding: utf-8
import kivy

kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from  kivy.lang import Builder

"""
Desta forma, podemos misturar codigo kv com codigo Python
"""

# codigo kv
code = """
BoxLayout:
    Button:
        text: "1"
    Button:
        text: "2"
"""

class Estudo6App(App):

    def build(self):
        return Builder.load_string(code)


janela = Estudo6App()
janela.run()