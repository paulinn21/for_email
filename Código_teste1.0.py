from kivymd.app import MDApp
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabs
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar


sim = ["@","#","!","$","%*"]


class Tab(MDBoxLayout, MDTabsBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(MDLabel(text="Olá! Essa é uma aba.", halign="center"))


class ForEmailApp(MDApp):
    def build(self):
        
        Window.clearcolor = (0.5, 0.2, 10, 100)

        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        # Layout principal
        layout = MDBoxLayout(orientation='vertical', padding=0.5, spacing=100)

        imagem = Image(source = "imagem.png", size_hint=(0.5,0.4), height = 50)
        layout.add_widget(imagem)

        # Layout para os campos de entrada
        form_layout = GridLayout(cols=2, spacing=20, size_hint=(0.4, 0.4))

        # Campos de entrada
        form_layout.add_widget(MDLabel(text="Nome:"))
        self.nome_input = TextInput(multiline=False)
        form_layout.add_widget(self.nome_input)

        form_layout.add_widget(MDLabel(text="E-mail:"))
        self.email_input = TextInput(multiline=False)
        form_layout.add_widget(self.email_input)

        form_layout.add_widget(MDLabel(text="Senha:"))
        self.senha_input = TextInput(password=True, multiline=False)
        form_layout.add_widget(self.senha_input)

        # Botão de cadastro
        self.cadastrar_button = Button(text="Cadastrar", size_hint=(0.2, 0.1), background_color=(0.3, 0, 0.5, 0.6))
        self.cadastrar_button.bind(on_press=self.cadastrar)
        self.cadastrar_button.pos_hint = {'x' : 0.05 , 'y' : 0.4 }
        
        # Adicionando os widgets ao layout principal
        layout.add_widget(form_layout)
        layout.add_widget(self.cadastrar_button)
        

        return layout

    def cadastrar(self, instance):
        # Recuperar os dados inseridos pelo usuário
        nome = self.nome_input.text
        email = self.email_input.text
        senha = self.senha_input.text

        # Verificar se todos os campos foram preenchidos corretamente 

        if not nome or not email or not senha:
            self.show_popup("Erro", "Por favor, preencha todos os campos.")  
            return
        
        elif len(senha) <= 4:
            self.show_popup("Senha fraca", "Sua senha deve conter ao menos 4 digitos")
            return
        
        elif senha.isalpha() or senha.isnumeric() or senha.isalnum():
            self.show_popup("Senha fraca", "Sua senha deve conter ao menos uma letra, um número e um símbolo (!@#$%*).")
            return
        
        else: 
            for c in senha:
                if not c.isalpha() and not c.isnumeric():
            
                    if c in sim: 
                        continue
                    else:
                        self.show_popup("Erro", "Sua senha deve conter ao menor um síbolo (!@#$%*).")
                    

        # Se tudo estiver correto, mostrar a mensagem de sucesso
        self.show_popup("Cadastro Concluído", f"Cadastro realizado!\n\nNome: {nome}\nE-mail: {email}")

        # Limpar os campos após o cadastro
        self.nome_input.text = ""
        self.email_input.text = ""
        self.senha_input.text = ""

    def show_popup(self, title, message):
        # Função para mostrar a janela de popup com mensagem
        popup = Popup(title=title,
                      content=MDLabel(text=message),
                      size_hint=(None, None), size=(400, 200))
        popup.open()


# Rodando o aplicativo
if __name__ == '__main__':
    ForEmailApp().run()


