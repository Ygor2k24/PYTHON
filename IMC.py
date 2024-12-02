nome = input(f"Digite sue nome:")
peso = float(input(f"Digite seu peso:"))
altura = float(input(f"Digite sua altura:"))

print(f"Olá {nome}. Aguarde alguns instantes, até calcularmos o seu Indice de Massa Corporal (IMC).")

if peso / (altura ** 2):

imc = 0

print(f"Seu IMC é {imc:.2f}.")

if imc < 18.5:
    print(f"Você está abaixo do peso.")
if 18.5 <= imc < 29.99:
    print(f"Você está com o peso normal.")
if 30.0:
    pass