import customtkinter as ctk
# abrindo uma janela e definindo seu tamanho
window = ctk.CTk()
window.geometry('500x300')
# texto de 'Sign in'
text_login_notice = ctk.CTkLabel(window, text='Sign in')
text_login_notice.pack(padx=10, pady=10) 
# campo solicitando um e-mail
input_email = ctk.CTkEntry(window, placeholder_text='Your e-mail address')
input_email.pack(padx=10, pady=10)
# campo solicitando uma senha
input_pwd = ctk.CTkEntry(window, placeholder_text='Password', show='●')
input_pwd.pack(padx=10, pady=10)
# botão para realizar o login
button_login = ctk.CTkButton(window, text='Login', command='login_click')
button_login.pack(padx=10, pady=10)


window.mainloop()