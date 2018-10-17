from kivy.app import App

"""
Criamos um arquivo hello.kv e colocamos a linguagem de
marcação dentro dele.
O FrameWork Kivy identifica esse arquivo pelo nome da Class
O nome da Classe deve ser o mesmo nome do arquivo, sem existir o 
prefixo App apos ele.
"""

class HelloApp(App):
    pass

HelloApp().run()