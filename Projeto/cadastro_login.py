from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import StringProperty
import re


#simbolos da senha
sim = ["@","#","!","$","%*"]

KV = '''
ScreenManager:
    id: screen_manager
    MDScreen:
        name: "cadastro"


        MDBoxLayout:
            orientation: 'vertical'
            padding: "24dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size_hint: 0.9, None
            height: self.minimum_height

            FitImage: 
                source: "imagem.png" 
                size_hint_y: None
                height: "100"
                radius: [1,]
                allow_stretch: True
                keep_ratio: True

            MDLabel:
                text: "Cadastro"
                halign: "center"
                theme_text_color: "Primary"
                font_style: "H5"

            MDTextField:
                id: nome
                hint_text: "Nome completo"
                icon_right: "account"
                mode: "rectangle"

            MDTextField:
                id: email
                hint_text: "E-mail"
                icon_right: "email"
                mode: "rectangle"

            MDTextField:
                id: senha
                hint_text: "Senha"
                password: True
                icon_right: "lock"
                mode: "rectangle"
            
            MDTextField:
                id: confirma_senha
                hint_text: "Confirmar senha"
                password: True
                icon_right: "lock-check"
                mode: "rectangle"
                
            MDRaisedButton:
                text: "Cadastrar"
                pos_hint: {"center_x": 0.5}
                on_release: app.cadastrar()

    MDScreen: 
        name:"login"


        MDBoxLayout:
            orientation: 'vertical'
            padding: "24dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size_hint: 0.9, None
            height: self.minimum_height

            FitImage: 
                source: "imagem.png" 
                size_hint_y: None
                height: "100"
                radius: [1,]
                allow_stretch: True
                keep_ratio: True

            MDLabel:
                text: "Login"
                halign: "center"
                font_style: "H5"

            MDTextField:
                id: login_email
                hint_text: "E-mail"
                icon_right: "email"
                mode: "rectangle"

            MDTextField:
                id: login_senha
                hint_text: "Senha"
                password: True
                icon_right: "lock"
                mode: "rectangle"

            MDRaisedButton:
                text: "Entrar"
                pos_hint: {"center_x": 0.5}
                on_release: app.fazer_login()
        
    MDScreen: 
        name: "aplicativo"

        MDBoxLayout:
            orientation: 'vertical'
            padding: "24dp"
            spacing: "20dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size_hint: 0.9, None
            height: self.minimum_height

            MDBoxLayout:
                size_hint_y: 0.3  # Definindo a altura da primeira parte
                md_bg_color: 0.5, 0.0, 0.5, 1  # Cor de fundo roxa
                padding: "10dp"
                spacing: "10dp"
            
            MDBoxLayout:
                size_hint_y: 0.7  # Definindo a altura da segunda parte
                padding: "10dp"
                spacing: "10dp"

                MDLabel:
                    id: saudacao
                    text: "Olá, " + app.primeiro_nome + "."
                    halign: "center"
                    theme_text_color: "Primary"
                    font_style: "H5"
                
                MDLabel:
                    text: "O app está em manutenção no momento."
                    halign: "center"
                    theme_text_color: "Primary"
                    font_style: "H5"
                
        
'''


class ForEmailApp(MDApp):
    primeiro_nome = StringProperty("")

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_string(KV)

    def cadastrar(self):
        nome = self.root.ids.nome.text.strip()
        email = self.root.ids.email.text
        senha = self.root.ids.senha.text
        confirma_senha = self.root.ids.confirma_senha.text


        if nome == "" or email == "" or senha == "" or confirma_senha=="" :
            self.mostrar_dialogo("Erro", "Por favor, preencha todos os campos!")
            return
        
        if len(senha) <= 4:
            self.mostrar_dialogo("Senha fraca", "Sua senha deve conter ao menos 4 digitos")
            return
        
        if senha != confirma_senha:
            self.mostrar_dialogo("Erro", "As senhas não coincidem!")
            return
        
        if not self.validar_email(email):
            self.mostrar_dialogo("Erro no email", "O email deve ser da Escola de Química!")
            return
            
        if senha.isalpha() or senha.isnumeric() or senha.isalnum():
            self.mostrar_dialogo("Senha fraca", "Sua senha deve conter ao menos uma letra, um número e um símbolo (!@#$%*).")
            return
        
        if not any(c.isalpha() for c in senha) or not any(c.isdigit() for c in senha):
            self.mostrar_dialogo("Senha fraca", "Sua senha deve conter ao menos uma letra e um número.")
            return

        if not any(c in sim for c in senha):
            self.mostrar_dialogo("Senha fraca", "Sua senha deve conter ao menos um símbolo (!@#$%*).")
            return

        self.email_cadastrado = email
        self.senha_cadastrada = senha
        self.nome_cadastrado = nome
        self.primeiro_nome = nome.split()[0]

        self.mostrar_dialogo("Sucesso", f"{nome}, seu cadastro foi realizado!")
        self.root.current = "login"

    def validar_email(self, email):
        #Regex p validar a estrutura do e-mail
        regex = r'^[a-zA-Z0-9_.+-]+@eq\.ufrj\.br$'
        return re.match(regex, email) is not None

    def fazer_login(self, *args):
        email = self.root.ids.login_email.text
        senha = self.root.ids.login_senha.text


        if email == self.email_cadastrado and senha == self.senha_cadastrada:
            self.mostrar_dialogo("Bem-vindo!", "Login realizado com sucesso!")
            #Mudar para a aba do app 
            self.root.current = "aplicativo"

        else:
            self.mostrar_dialogo("Erro", "E-mail ou senha incorretos.")

    def mostrar_dialogo(self, titulo, mensagem):
        if hasattr(self, 'dialog'):
            self.dialog.dismiss()
        self.dialog = MDDialog(
            title=titulo,
            text=mensagem,
            buttons=[
                MDRaisedButton(text="OK", on_release=lambda x: self.dialog.dismiss())
            ]
        )
        self.dialog.open()


if __name__ == '__main__':
    ForEmailApp().run()