try:
    a = 1/0
    print(a)
except NameError as erro:
    print(f'Erro: {erro}')
except (IndexError, KeyError) as erro:
    print(f'Erro de índice ou chave')
except Exception as erro:
    print(f'Erro: inesperado')
else:
    print('Seu cpodigo foi executado com sucesso!')
finally:
    print('Sempre executado!')
    a = 'Valor default'

print(a)
print('Continua...')
