from random import randint

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")
numero_secreto = randint(1, 10)
total_de_tentativas = 3
rodada = 1

#####################################################################################################
#CÓDIGO FEITO COM LAÇO DE REPEITÇÃO FOR
for rodada in range(1, 4):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        print("Você acertou na {} rodada".format(rodada))
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
            if(rodada == 3):
                print("O número secreto era {}".format(numero_secreto))
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
            if (rodada == 3):
                print("O número secreto era {}".format(numero_secreto))

#########################################################################################################
#CÓDIGO FEITO COM LAÇO DE REPETIÇÃO WHILE
# while (rodada <= total_de_tentativas):
#     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#
#     chute_str = input("Digite o seu número: ")
#     print("Você digitou " , chute_str)
#     chute = int(chute_str)
#
#     acertou = chute == numero_secreto
#     maior = chute > numero_secreto
#     menor = chute < numero_secreto
#
#     if(acertou):
#         print("Parabéns! Você acertou!")
#         rodada = 321345
#        print("Você acertou na {} rodada".format(rodada))
#     else:
#         if(maior):
#             print("O seu chute foi maior do que o número secreto!")
#             if(rodada == 3):
#                 print("O número secreto era {}".format(numero_secreto))
#         elif(menor):
#             print("O seu chute foi menor do que o número secreto!")
#             if(rodada == 3):
#                 print("O número secreto era {}".format(numero_secreto))
#
#     rodada = rodada + 1

print("Fim do jogo!")


