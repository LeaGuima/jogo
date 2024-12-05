import random

def escolher_palavra():
    """Escolhe uma palavra aleatória da lista."""
    palavras = ['python', 'programacao', 'computador', 'desafio', 'jogo']
    return random.choice(palavras)

def processar_palpite(palpite, palavra_secreta, letras_descobertas, letras_erradas, tentativas_restantes):
    """Processa o palpite do jogador, atualizando o estado do jogo."""
    if len(palpite) == 1:  # Palpite é uma letra
        if palpite in letras_descobertas or palpite in letras_erradas:
            return "Você já tentou essa letra. Tente outra.", letras_descobertas, letras_erradas, tentativas_restantes

        if palpite in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == palpite:
                    letras_descobertas[i] = palpite
            return "Boa! Você acertou uma letra.", letras_descobertas, letras_erradas, tentativas_restantes
        else:
            letras_erradas.append(palpite)
            return "Ops! Essa letra não está na palavra.", letras_descobertas, letras_erradas, tentativas_restantes - 1

    elif len(palpite) == len(palavra_secreta):  # Palpite é uma palavra
        if palpite == palavra_secreta:
            return "Você adivinhou a palavra corretamente!", letras_descobertas, letras_erradas, tentativas_restantes
        else:
            return "Não é a palavra correta.", letras_descobertas, letras_erradas, tentativas_restantes - 1

    return "Entrada inválida. Tente novamente.", letras_descobertas, letras_erradas, tentativas_restantes
