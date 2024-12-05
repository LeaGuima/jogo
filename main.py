from jogo_da_forca import escolher_palavra, processar_palpite

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_descobertas = ['_' for _ in palavra_secreta]
    letras_erradas = []
    tentativas_restantes = 6
    tentativas_totais = 0

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:")
    print(' '.join(letras_descobertas))

    while tentativas_restantes > 0:
        print(f"\nTentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")

        if tentativas_totais >= 4:
            palpite = input("Digite uma letra ou tente adivinhar a palavra inteira: ").lower()
        else:
            palpite = input("Digite uma letra: ").lower()

        mensagem, letras_descobertas, letras_erradas, tentativas_restantes = processar_palpite(
            palpite, palavra_secreta, letras_descobertas, letras_erradas, tentativas_restantes
        )

        print(mensagem)
        tentativas_totais += 1

        # Mostra o progresso
        print(' '.join(letras_descobertas))

        # Verifica se o jogador ganhou
        if '_' not in letras_descobertas:
            print("\nParabéns! Você descobriu a palavra!")
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

# Executa o jogo
if __name__ == "__main__":
    jogo_da_forca()
