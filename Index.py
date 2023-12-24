# Defina as variáveis iniciais (float cn = cn-1 + m)
c1 = 0.6
c2 = c1 + 0.596
c3 = c2 + 0.592
c4 = c3 + 0.591
c5 = c4 + 0.586
c6 = c5 + 0.582
c7 = c6 + 0.579
c8 = c7 + 0.575
c9 = c8 + 0.571
c10 = c9 + 0.568
c11 = c10 + 0.565
c12 = c11 + 0.561
c13 = c12 + 0.558
c14 = c13 + 0.554
c15 = c14 + 0.552
c16 = c15 + 0.549
c17 = c16 + 0.545
c18 = c17 + 0.541
c19 = c18 + 0.539
c20 = c19 + 0.536
c21 = c20 + 0.531
c22 = c21 + 0.528
c23 = c22 + 0.525
c24 = c23 + 0.523
c25 = c24 + 0.519
c26 = c25 + 0.517
c27 = c26 + 0.513
c28 = c27 + 0.511
c29 = c28 + 0.507
c30 = c29 + 0.503
c31 = c30 + 0.501
c32 = c31 + 0.498
c33 = c32 + 0.495
c34 = c33 + 0.491
c35 = c34 + 0.489
c36 = c35 + 0.489
c37 = c36 + 0.483
c38 = c37 + 0.480
c39 = c38 + 0.477
c40 = c39 + 0.475
c41 = c40 + 0.471
c42 = c41 + 0.469
c43 = c42 + 0.467
c44 = c43 + 0.464
c45 = c44 + 0.461
c46 = c45 + 0.457
c47 = c46 + 0.456
c48 = c47 + 0.453
c49 = c48 + 0.448
c50 = c49 + 0.447
c51 = c50 + 0.445
c52 = c51 + 0.442
c53 = c52 + 0.439
c54 = c53 + 0.437
c55 = c54 + 0.434
c56 = c55 + 0.430
c57 = c56 + 0.428
c58 = c57 + 0.426
c59 = c58 + 0.423
c60 = c59 + 0.420
c61 = c60 + 0.418
c62 = c61 + 0.416
c63 = c62 + 0.413
c64 = c63 + 0.410
c65 = c64 + 0.408
c66 = c65 + 0.406
c67 = c66 + 0.404
c68 = c67 + 0.401
c69 = c68 + 0.399
c70 = c69 + 0.396
c71 = c70 + 0.393
c72 = c71 + 0.392
c73 = c72 + 0.388
c74 = c73 + 0.387
c75 = c74 + 0.384
c76 = c75 + 20.627
c77 = c76 + 13.946
c78 = c77 + 9.429
c79 = c78 + 6.375
c80 = c79 + 4.306
c81 = c80 + 2.914
c82 = c81 + 1.970
c83 = c82 + 1.332
c84 = c83 + 0.901
c85 = c84 + 0.608
c86 = c85 + 0.411
c87 = c86 + 0.278
c88 = c87 + 0.187
c89 = c88 + 0.126
c90 = c89 + 0.265

# Pergunte ao usuário qual variável exibir
# Estrutura de Repetição.
resposta = True
while resposta:
    try:
        escolha = input("Qual numero de desejos?\n")
        escolha = int(escolha)
        if 1 <= escolha <= 90:
            variavel_escolhida = locals()[f'c{escolha}']
            print(f"A chance de obter um T5 com {escolha} desejos é de: {variavel_escolhida:.2f}%")
        else:
            print("Escolha inválida!")
    except ValueError:
        print("Escolha inválida! Digite um número de 1 a 90.")

    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() == 'n':
        break