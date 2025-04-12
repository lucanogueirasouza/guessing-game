print ("-=-=-=-=-JOGO DA PALAVRA SECRETA-=-=-=-=-")

tentativa_jogador = 0
letras_acertadas_jogador = ""

while True: 
    PALAVRA_SECRETA = "python"
    letra_jogador = str(input(
         "Digite uma letra: "
    )).lower().strip()

    if len(letra_jogador) > 1:
        print (
            "É permitido apenas uma letra."
        )
        continue

    if not letra_jogador.isalpha():
        print (
            "Digite apenas strings. Tente Novamente."
        )
        continue

    for i in PALAVRA_SECRETA: 
        if letra_jogador == i: 
            print (
                f"Voce acertou a letra {letra_jogador}"
            )
            tentativa_jogador += 1
            letras_acertadas_jogador += letra_jogador
            print (
                f"A palavra até agora: {letras_acertadas_jogador}"
            )
            continue
        
    if letra_jogador not in PALAVRA_SECRETA: 
        print (
            "ERRADO! Tente novamente."
        )
        continue

    if letras_acertadas_jogador == "python": 
        print (
            f"Você acertou a palavra! {PALAVRA_SECRETA}\nQuantidade de tentativas: {tentativa_jogador}"
        )
        break