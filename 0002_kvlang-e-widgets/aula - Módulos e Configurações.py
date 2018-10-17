"""
Esta App foi criada para testar o modulo "inspector = " que foi adicionado no
arquivo config.ini em /home/ubuntu/.kivy/config.ini
pois quando a tela da app e executada, apertando Ctrl + E podemos ver as
propriedades da tela e editar ela.
"""


import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class TelinhaApp(App):



    def build(self):
        return Label(text='Ola')


TelinhaApp().run()