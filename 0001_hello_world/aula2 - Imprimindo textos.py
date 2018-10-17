#coding: utf-8

# autor: Wesley Borges

from kivy.app import App
from kivy.uix.label import Label

def build():
    lb = Label()
    lb.text = "Curso de Python e Kivy"
    lb.italic = True
    lb.font_size = 50
    return lb
    # return Label(text="Curso de Python e Kivy", italic=True, font_size=50)

app = App()
app.build = build
app.run()