import random

# Função para executar o jogo
def jogo(): 
    print("Olá, seja bem-vindo(a) ao adivinhucas! Adivinhe o número de 1 a 50 que o computador escolheu para vencer.") 

    print("\nJogo criado por: Lucas Boaratti.") 

    tentativas = 0 

    # Loop que inicia o jogo
    while True: 
        try: 
            escolhaNumero = input("\nDigite o número adivinhado pelo Computador: ") 
            escolhaNumero = int(escolhaNumero) 

            # Número aleatório de 1 a 50 é escolhido pelo random
            numeroAleatorio = random.randint(1, 50) 

            # Verificando se o usuário acertou o número aleatório
            if escolhaNumero == numeroAleatorio:
                print("\nParabéns! Você adivinhou o número sorteado! 🥳🥳🥳")  
                
                print(f"\nNúmero sorteado: {numeroAleatorio}") 

                print(f"\nVocê precisou de {tentativas} tentativas para acertar! Será que você consegue melhorar na próxima? 👀") 

                break 
            # Verificando se o usuário digitou um número de 1 a 50
            elif escolhaNumero > 50: 
                print("\nDigite apenas números de 1 a 50") 
                
                continue
            # Se o número que o usuário escolheu for menor que o número aleatório
            elif escolhaNumero < numeroAleatorio: 
                print("\nNúmero adivinhado foi abaixo do número sorteado.") 

                tentativas += 1
                
                print(f"\nTentativa atual: {tentativas}")
            # Se o número que o usuário escolheu for maior que o número aleatório
            elif escolhaNumero > numeroAleatorio: 
                print("\nNúmero adivinhado foi acima do número sorteado.")

                tentativas += 1

                print(f"\nTentativa atual: {tentativas}")

            # Verificando se o usuário chegou a 15 tentativas
            if tentativas == 15:
                print("\nQue pena! Você perdeu. Tente novamente. 😔")

                break

        # Caso o usuário digite algo diferente de um número
        except ValueError: 
            print("\nDigite apenas números inteiros!") 

jogo() 