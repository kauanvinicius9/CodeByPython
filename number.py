### Biblioteca random para escolhas ###
import random

class NumeroSorteador():
    def __init__ (self):
        ### Intervalo de números entre 0 a 100 ###
        self.__numero =  random.randint(0, 101)

    ### Analisa o número ###
    def analiseNumero(self, tentativas: int):
        if tentativas < self.__numero:
            return "\nO número sorteado, é maior que o número escolhido!" 
        
        elif tentativas > self.__numero:
            return "\nO número sorteado, é menor que o número escolhido!"
        
        else:
            return "\nBoa! Você acertou o número!"
        
    ### Mostra o número ###
    def mostrarNumero(self):
        return self.__numero
    
### Inicia o jogo ###
def comecar():
    print("===== JOGO INICIADO =====")
    print("-" * 30)
    print("\nAdivinhe um número dentro do intervalo de 0 a 100...")
    sorteado = NumeroSorteador()
    tentativas = 10

    ### Loop definido. Tentativas diminuem conforme o usuário erre-os ###
    while tentativas > 0:
        print(f"\nTentativas sobrando: {tentativas}.")
        opiniao = input("\nAdivinhe o número: ")

        ### Se a escolha não for número inteiro, dá erro ###
        if not opiniao.isdigit():
            print("\nInválido. Os números precisam ser inteiros!")
            continue

        suposicao = int(opiniao)

        ### Se a suposição for menor que 0 ou maior que 100, ou seja, fora do intervalo, dá erro ###
        if suposicao < 0 or suposicao > 100:
            print("\nInválido. O número está fora do intervalo!")
            continue

        resposta_correta = sorteado.analiseNumero(suposicao)
        print(resposta_correta)

        if resposta_correta == "\nBoa! Você acertou o número!":
            break

        tentativas -= 1

    ### Caso queira tentar novamente sem tentativas, não vai dar certo, apenas se for atualizado ###
    if tentativas == 0:
        print(f"\nSuas tentativas já acabaram. O número correto era {sorteado.mostrarNumero()}")
        
### Função se inicia ###
comecar()