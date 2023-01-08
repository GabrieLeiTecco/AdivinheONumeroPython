from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

#VARIÁVEIS GERAIS DO JOGO
numero_secreto = randint(1, 10)
total_de_tentativas = 3
rodada = 1
pontos = 20


print("Escolha um nível de dificuldade")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")
print("4 - Impossivel")

nivel = int(input())

match (nivel):
    case 1:
        total_de_tentativas = 7

    case 2:
        total_de_tentativas = 5

    case 3:
        total_de_tentativas = 3

    case 4:
        total_de_tentativas = 1

#####################################################################################################
#CÓDIGO FEITO COM LAÇO DE REPEITÇÃO FOR
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 10: ")
    chute = int(chute_str)
    pontos_perdidos = numero_secreto - chute

    if(chute < 1 or chute > 10):
        print("O número digitado deve ser entre 1 e 10")
        print("Vai perder uma tentativa por isso!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        print("Você acertou na {} rodada".format(rodada))
        print("Fim do jogo!")
        print("Sua pontuação foi de: {}".format(pontos))
        break
    else:
        pontos = abs(pontos - pontos_perdidos)
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
            if(rodada == total_de_tentativas):
                print("O número secreto era {}".format(numero_secreto))
                print("Fim do jogo!")
                print("Sua pontuação foi de: {}".format(pontos))
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}".format(numero_secreto))
                print("Fim do jogo!")
                print("Sua pontuação foi de: {}".format(pontos))

#########################################################################################################
#CÓDIGO FEITO COM LAÇO DE REPETIÇÃO WHILE
# while (rodada <= total_de_tentativas):
#     chute_str = input("Digite um número entre 1 e 10: ")
#     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#     print("Você digitou " , chute_str)
#     chute = int(chute_str)
#     pontos_perdidos = numero_secreto - chute
#
#     if(chute < 1 or chute > 10):
#         print("O número digitado deve ser entre 1 e 10")
#         print("Vai perder uma tentativa por isso!")
#         rodada = rodada + 1
#         continue
#
#     acertou = chute == numero_secreto
#     maior = chute > numero_secreto
#     menor = chute < numero_secreto
#
#     if(acertou):
#         print("Parabéns! Você acertou!")
#         print("Você acertou na {} rodada".format(rodada))
#         print("Fim do jogo!")
#         print("Sua pontuação foi de: {}".format(pontos))
#         rodada = 1323221
#     else:
#         pontos = abs(pontos - pontos_perdidos)
#         if(maior):
#             print("O seu chute foi maior do que o número secreto!")
#             if(rodada == total_de_tentativas):
#                 print("O número secreto era {}".format(numero_secreto))
#                 print("Fim do jogo!")
#                 print("Sua pontuação foi de: {}".format(pontos))
#         elif(menor):
#             print("O seu chute foi menor do que o número secreto!")
#             if (rodada == total_de_tentativas):
#                 print("O número secreto era {}".format(numero_secreto))
#                 print("Fim do jogo!")
#                 print("Sua pontuação foi de: {}".format(pontos))
#
#     rodada = rodada + 1
#
# print("Fim do jogo!")
