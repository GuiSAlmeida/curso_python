"""
Sistemas de perguntas e respostas
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6'
        },
        'resposta_certa': 'c'
    },
}

respostas_certas = 0

for chave_pergunta, chave_resposta in perguntas.items():
    print(f'{chave_pergunta}: {chave_resposta["pergunta"]}')

    for resposta_chave, resposta_valor in chave_resposta['respostas'].items():
        print(f'[{resposta_chave}]: {resposta_valor}')
    print('-'*30)

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == chave_resposta['resposta_certa']:
        print('Acertou!!')
        respostas_certas += 1
    else:
        print('Errrrrrou!!')

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua % de acertos foi de {porcentagem_acerto}%.')
