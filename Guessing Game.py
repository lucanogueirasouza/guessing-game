print("-=-=-=-=-JOGO DA PALAVRA SECRETA-=-=-=-=-")

PALAVRA_SECRETA = "python"
tentativa_jogador = 0
letras_acertadas_jogador = ""

while True:
    letra_jogador = input("Digite uma letra: ").lower().strip()

    if len(letra_jogador) > 1:
        print("É permitido apenas uma letra.")
        continue

    if not letra_jogador.isalpha():
        print("Digite apenas letras.")
        continue

    if letra_jogador in PALAVRA_SECRETA:
        if letra_jogador not in letras_acertadas_jogador:
            print(f"Você acertou a letra '{letra_jogador}'!")
            letras_acertadas_jogador += letra_jogador
        else:
            print(f"Você já tentou a letra '{letra_jogador}'.")
    else:
        print("ERRADO! Digite outra letra!")

    tentativa_jogador += 1

    palavra_formada = ""
    for letra in PALAVRA_SECRETA:
        if letra in letras_acertadas_jogador:
            palavra_formada += letra
        else:
            palavra_formada += "_"

    print(f"Palavra até agora: {palavra_formada}")

    if palavra_formada == PALAVRA_SECRETA:
        print(f"\nParabéns! Você acertou a palavra: {PALAVRA_SECRETA}")
        print(f"Quantidade de tentativas: {tentativa_jogador}")
        break