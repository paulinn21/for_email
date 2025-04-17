from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import StringProperty
import re
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import OneLineListItem  

KV = '''
MDNavigationLayout:

    ScreenManager:
        id:screen_manager

# Tela principal ---------------------------------------------------------------
        MDScreen:
            name: "aplicativo"
            FloatLayout:

                # Parte roxa no topo
                MDBoxLayout:
                    size_hint: 1, None
                    height: "100dp"
                    pos_hint: {"top": 1}  # Fica colado no topo
                    md_bg_color: 0.294, 0, 0.51, 1  # Roxo escuro

                    Image:
                        source: "pequena.png"
                        size_hint: None, None
                        size: "400dp", "400dp"
                        pos_hint: {"center_y": 0.5} 

                    # Espaço à esquerda do botão
                    Widget:

                    MDIconButton:
                        icon: "menu"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        size_hint: None, None
                        pos_hint: {"center_y": 0.5}
                        on_release: nav_drawer.set_state("open")

                # Parte branca abaixo da imagem
                Widget:
                    size_hint: 1, None
                    height: self.parent.height - 100
                    pos_hint: {"x": 0, "y": 0}
                    canvas.before:
                        Color:
                            rgba: 1, 1, 1, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                MDCard:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "280dp", "180dp"
                    pos_hint: {"center_x": 0.5, "center_y":0.7}
                    elevation: 3
                    md_bg_color: 1, 1, 1, 1
                    height: self.minimum_height

                    MDLabel:
                        text: "Bem-vindo, {nome_exemplo}!"
                        halign: "center"
                        font_style: "H6"
                        size_hint_y: None
                        height: "48dp"             
 # perfil --------------------------------------------------------------------------------                       
        MDScreen:
            name: "perfil"

            MDBoxLayout:
                orientation: 'vertical'
                padding: "10dp"
                spacing: "20dp"
                md_bg_color: 0.294, 0, 0.51, 1  # Roxo escuro

                # Barra de navegação
                MDTopAppBar:
                    title: "Perfil"
                    left_action_items: [["arrow-left", lambda x: app.confirmar_saida()]]
                    icon_color: (0, 0, 0, 1)
                    d_bg_color: 1, 1, 1, 1

                ScrollView:

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "10dp"
                        spacing: "20dp"
                        size_hint_y: None
                        height: self.minimum_height
                        
                        # Título
                        MDLabel:
                            text: "Informações do Usuário"
                            halign: "center"
                            font_style: "H6"
                            size_hint_y: None
                            height: "48dp"

                        # Informações do usuário
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding: "10dp"
                            spacing: "20dp"
                            height: self.minimum_height

                            MDBoxLayout:
                                orientation: "horizontal"
                                size_hint_y: None
                                height: "48dp"
                                spacing: "10dp"

                                MDLabel:
                                    text: "Nome:"
                                    halign: "left"
                                    size_hint_x: None
                                    width: "100dp"

                                MDTextField:
                                    id: nome_field
                                    text: "Nome_exemplo"
                                    password: False
                                    halign: "left"
                                    mode: "rectangle"
                                    size_hint_x: None
                                    width: "300dp"
                                    height: "58dp"
                                    disabled: True

                            MDBoxLayout:
                                orientation: "horizontal"
                                size_hint_y: None
                                height: "58dp"
                                spacing: "10dp"

                                MDLabel:
                                    text: "Email:"
                                    halign: "left"
                                    size_hint_x: None
                                    width: "100dp"

                                MDTextField:
                                    id: email_field
                                    text: "email_exemplo@eq.ufrj.br"
                                    password: False
                                    halign: "left"
                                    mode: "rectangle"
                                    size_hint_x: None
                                    width: "300dp"
                                    height: "58dp"
                                    disabled: True

                            MDBoxLayout:
                                orientation: "horizontal"
                                size_hint_y: None
                                height: "48dp"
                                spacing: "10dp"

                                MDLabel:
                                    text: "Senha:"
                                    halign: "left"
                                    size_hint_x: None
                                    width: "100dp"

                                MDTextField:
                                    id: senha_field
                                    text: "@senha_exemplo"
                                    password: True
                                    halign: "left"
                                    mode: "rectangle"
                                    size_hint_x: None
                                    width: "300dp"
                                    height: "58dp"
                                    disabled: True

                                MDIconButton:
                                    id: show_password
                                    icon: "eye-off"
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    on_release: app.toggle_password()
                                
                            MDBoxLayout:
                                orientation: "horizontal"
                                spacing: "10dp"
                                size_hint_y: None
                                height: "80dp"
                                padding: "10dp"

                                MDRaisedButton:
                                    text: "Editar Perfil"
                                    on_release: app.editar_perfil() 

                                MDRaisedButton:
                                    text: "Salvar"
                                    on_release: app.salvar_perfil()

#configurações ---------------------------------------------------------------------------------
        MDScreen:
            name: "configuracoes"

            MDBoxLayout:
                orientation: 'vertical'
                padding: "10dp"
                spacing: "10dp"
                md_bg_color: 0.294, 0, 0.51, 1
                
                MDTopAppBar:
                    title: "Configurações"
                    left_action_items: [["arrow-left", lambda x: setattr(root.ids.screen_manager, "current", "aplicativo")]]
                    icon_color: (0, 0, 0, 1)

                MDBoxLayout: 
                    orientation:'horizontal'
                    spacing: "15dp"
                    size_hint_y: None
                    height: "500dp"

                    MDRaisedButton:
                        text: "Alterar Tema"
                        pos_hint: {"center_y": 0.5, "center_x":0.75}
                        on_release: print("Abrir opções de tema")
                        

                    MDRaisedButton:
                        text: "Alterar Idioma"
                        pos_hint: {"center_x": 0.5}
                        on_release: print("Abrir opções de idioma")

                    MDLabel:
                        text: "Ajustes do aplicativo"
                        halign: "center"
                        font_style: "H6"
                        size_hint_y: None
                        pos_hinx:{"center_x":0.5}
                        height: "950dp"

#Drawer ---------------------------------------------------------------------------------
    # Aba lateral (Navigation Drawer)
    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)
        md_bg_color: 1, 1, 1, 1

        BoxLayout:
            orientation: "vertical"
            padding: "10dp"
            spacing: "10dp"

            AnchorLayout:
                anchor_x: "center"
                anchor_y: "top"
                size_hint_y: None
                height: "120dp"
            
            MDLabel:
                text: "Menu"
                font_style: "H5"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1  # Branco

            MDLabel:
                text: "Olá, Usuário!"
                font_style: "Subtitle1"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "center"

            BoxLayout:
                size_hint_y: None
                height: "1dp"
                canvas:
                    Color:
                        rgba: 0.7, 0.7, 0.7, 1  # Cor cinza claro
                    Rectangle:
                        pos: self.pos
                        size: self.size

            # 👤 Botão de Perfil
            MDList:
                OneLineIconListItem:
                    text: "Meu Perfil"
                    on_release: 
                        nav_drawer.set_state("close")
                        app.abre_perfil()
                    IconLeftWidget:
                        icon: "account"

                OneLineIconListItem:
                    text: "Configurações"
                    on_release: 
                        nav_drawer.set_state("close")
                        app.abrir_config()
                    IconLeftWidget:
                        icon: "cog"

                OneLineIconListItem:
                    text: "Sair"
                    on_release: print("Sair clicado")
                    IconLeftWidget:
                        icon: "logout"
    
            
'''


class ForEmailApp(MDApp):
    primeiro_nome = StringProperty("")

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_string(KV)

    def toggle_password(self):
        # Alterna entre mostrar e esconder a senha
        senha_field = self.root.ids.senha_field
        show_password_icon = self.root.ids.show_password

        if senha_field.password:
            senha_field.password = False
            show_password_icon.icon = "eye"  # Ícone de olho aberto
        else:
            senha_field.password = True
            show_password_icon.icon = "eye-off"  # Ícone de olho fechado

    def voltar_para_home(self):
        if hasattr(self, 'dialog'):
            self.dialog.dismiss()

        # Restaurar os valores originais
        self.root.ids.nome_field.text = self.original_nome
        self.root.ids.email_field.text = self.original_email
        self.root.ids.senha_field.text = self.original_senha

        # Desabilita os campos
        for campo in [self.root.ids.nome_field, self.root.ids.email_field, self.root.ids.senha_field]:
            campo.disabled = True
            campo.text_color = (0.6, 0.6, 0.6, 1)
            campo.line_color_normal = (0.5, 0.5, 0.5, 1)

        # Volta pra tela inicial
        self.root.ids.screen_manager.current = "aplicativo"

    def confirmar_saida(self):
        senha_field = self.root.ids.senha_field
        nome_field = self.root.ids.nome_field
        email_field = self.root.ids.email_field

        if not senha_field.disabled or not nome_field.disabled or not email_field.disabled:
            self.dialog = MDDialog(
                title="Deseja salvar as alterações?",
                text="Você fez mudanças no perfil. Deseja salvar antes de sair?",
                buttons=[
                    MDRaisedButton(text="Salvar", on_release=lambda x: self.salvar_e_voltar()),
                    MDRaisedButton(text="Descartar", on_release=lambda x: self.voltar_para_home())
                ],
            )
            self.dialog.open()
        else:
            self.voltar_para_home()

    def salvar_e_voltar(self):
        self.dialog.dismiss()
        self.salvar_perfil()
        self.voltar_para_home()

    def editar_perfil(self):

        senha_field = self.root.ids.senha_field
        nome_field = self.root.ids.nome_field
        email_field = self.root.ids.email_field

        
        senha_field.disabled = False  # Ativa o campo para edição
        nome_field.disabled = False   # Ativa o campo para edição
        email_field.disabled = False  # Ativa o campo para edição


        # Muda a cor conforme o estado
        campos = [senha_field, nome_field, email_field]
        for campo in campos:
            if campo.disabled:
                campo.text_color = (0.6, 0.6, 0.6, 1)  #cinza quando desativado
                campo.line_color_normal = (0.5, 0.5, 0.5, 1)
            else:
                campo.text_color = (1, 1, 1, 1)     #branco quando ativado
                campo.line_color_normal = (1, 1, 1, 1)

    def salvar_perfil(self):
        
        self.original_nome = self.root.ids.nome_field.text
        self.original_email = self.root.ids.email_field.text
        self.original_senha = self.root.ids.senha_field.text
    
        senha_field = self.root.ids.senha_field
        nome_field = self.root.ids.nome_field
        email_field = self.root.ids.email_field

        campos = [senha_field, nome_field, email_field]

        for campo in campos:
            campo.disabled = True
            if campo.disabled:
                campo.text_color = (0.6, 0.6, 0.6, 1)  #cinza quando desativado
                campo.line_color_normal = (0.5, 0.5, 0.5, 1)
            else:
                campo.text_color = (1, 1, 1, 1)     #branco quando ativado
                campo.line_color_normal = (1, 1, 1, 1)
        

    def abrir_config(self):
        self.root.ids.screen_manager.current = "configuracoes"

    def abre_perfil(self):
        self.root.ids.screen_manager.current = "perfil"

        self.original_nome = self.root.ids.nome_field.text
        self.original_email = self.root.ids.email_field.text
        self.original_senha = self.root.ids.senha_field.text

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