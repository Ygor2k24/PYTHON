user_correto = "email@gmail.com"
senha_correta = "senha1234"

user_digitado = input("Digite seu email:")
senha_digitada = input("Digite sua senha:")

if user_correto == user_digitado and senha_correta == senha_digitada:
    print(f"Seu email e senha está correto.")
else:
    print(f"Seu email ou senha está incorreto.")