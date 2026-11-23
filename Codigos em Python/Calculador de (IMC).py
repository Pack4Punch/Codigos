print("#################################")
print("#####Ìdice de Massa Corporal#####")
print("#################################")
print()
altura=float(input("Digite sua altura: "))
peso=int(input("Digiter seu peso: "))
imc=float(peso/(altura*altura))
print()
print("#################################")
print(f"Seu Índice de Massa Corporal é de: [{imc}]")
print("#################################")
if imc < 18.5:
    print("Seu peso está abaixo do normal")
elif 18.6 <= imc <= 24.9:
    print("Seu peso está normal")
elif 25.0 <= imc <= 29.9:
    print("Você está com pré obsidade")
elif 30.0 <= imc <= 34.9:
    print("Você nestá obsidade grau 1")
elif 35.0 <= imc <= 39.9:
    print("Você nestá obsidade grau 2(severa)")
elif imc >= 40.0:
    print("Você nestá obsidade grau 3(mórbida)")
print("#################################")
print()