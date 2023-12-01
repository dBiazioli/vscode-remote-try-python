#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

opcoes = ['pedra', 'papel', 'tesoura']
pontuacao = {'jogador': 0, 'computador': 0}

while True:
    escolha_jogador = input('Escolha uma opção (pedra, papel, tesoura): ').lower()
    if escolha_jogador not in opcoes:
        print('Opção inválida. Tente novamente.')
        continue

    escolha_computador = random.choice(opcoes)
    print(f'O computador escolheu {escolha_computador}.')

    if escolha_jogador == escolha_computador:
        print('Empate!')
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra'):
        print('Você ganhou!')
        pontuacao['jogador'] += 1
    else:
        print('Você perdeu.')
        pontuacao['computador'] += 1

    print(f'Pontuação: Jogador - {pontuacao["jogador"]}, Computador - {pontuacao["computador"]}')

    jogar_novamente = input('Quer jogar novamente? (s/n): ').lower()
    if jogar_novamente != 's':
        break