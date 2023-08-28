peso = float (input("Digite o seu peso (kg): "))
altura = float (input ("Digite a sua altura (m): "))
imc = peso/(altura**2)
if imc < 17:
    print("estou muito abaixo do peso")
elif imc >= 17 and imc < 18.5:
    print("Estou abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print ("peso ideal")
else:
    print("Estou acima do peso")
    