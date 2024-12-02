nome = input(f"Digite sue nome:")
peso = float(input(f"Digite seu peso:"))
altura = float(input(f"Digite sua altura:"))

print(f"Olá {nome}. Aguarde alguns instantes, até calcularmos o seu Indice de Massa Corporal (IMC).")

if peso / (altura ** 2):

print(f"Seu IMC é {imc:.2f}.")

if imc < 18.5:
    print(f"Você está abaixo do peso.")
if 18.5 <= imc <