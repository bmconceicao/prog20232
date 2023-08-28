altura = float (input("Digite a sua altura (m): "))
peso = float (input("Digite o seu peso kg): "))
imc = peso/(altura**2)
print("Seu IMC é: ", imc)
print("Estou muito abaixo do peso?", imc < 17)
print("Estou abaixo do peso?", imc >= 17 and imc < 18.5)
print("Estou com peso dentro do normal?", imc >= 18.5 and imc <25)
print("Estou acima do peso normal?", imc >= 25 and imc <30)
print("Estou muito acima do peso?", imc > 30) 


