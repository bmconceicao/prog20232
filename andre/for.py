tempoExperimento = 1 #s
frequenciaSensor = 10 
qtdDados = tempoExperimento*frequenciaSensor
#coleta 
dado = []
# for contador in range (qtdDados):
#     dado.append(float(input()))

#dado = [89127, 1298,902, 3097, 10000, 23555, 8669422, 999238224, 1245555]

# soma = dado[0] + dado[1] + dado[2] + dado[3]
# print(soma)
# soma = 0
# for contador in range (len(dado)): 
#      soma = soma + dado[contador]
# print(soma)
# for data in dado:
#     soma = soma + (1 / frequenciaSensor) * data
# print(soma)

dicionario = {
                "Brasil":[1,2,3,4,5,6],
                "EUA":[3,4,56,6,4,2] 
                }
for país in dicionario:
    print(país)
    print(dicionario[país])
    