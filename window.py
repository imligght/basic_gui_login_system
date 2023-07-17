import customtkinter as ctk

class Screen():

    def window_preset(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.window = ctk.CTk()
        self.window.title('Login System')
        self.window.geometry('500x300')

    def main_screen(self):
        self.window_preset()
        # texto de 'Sign in'
        self.text_login_notice = ctk.CTkLabel(self.window, text='Sign in')
        self.text_login_notice.pack(padx=10, pady=10) 
        # campo solicitando um e-mail
        self.input_email = ctk.CTkEntry(self.window, placeholder_text='Your e-mail address')
        self.input_email.pack(padx=10, pady=10)
        # campo solicitando uma senha
        self.input_pwd = ctk.CTkEntry(self.window, placeholder_text='Password', show='●')
        self.input_pwd.pack(padx=10, pady=10)
        # botão para realizar o login
        self.button_login = ctk.CTkButton(self.window, text='Login', command='login_click')
        self.button_login.pack(padx=10, pady=10)
        # checkbox para manter o usuário conectado
        self.login_checkbox = ctk.CTkCheckBox(self.window, text='Lembrar de mim')
        self.login_checkbox.pack(padx=10, pady=10)
        
        self.window.mainloop()