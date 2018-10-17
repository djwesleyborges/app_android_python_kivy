# coding: utf-8

# autor: Wesley Borges

# from kivy.app import App
# from kivy.uix.label import Label
#
#
# class MeuPrograma(App):  # Criando uma classe MeuPrograma que sera Filha da class App
#
#     def build(self):
#         return Label()
#
#
# MeuPrograma().run()

################################

'''
Foi criado a classe MeuPrograma, e incluido as
funções click e build como metodos da mesma e passado o parametro self nestes metodos.
'''

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MeuPrograma(App):
    def click(self):
        print(ed.text)

    def build(self):
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
        bt.on_press = self.click  # Evento do botão, chamando a função click

        return layout


MeuPrograma().run()