from datetime import datetime
from calendar import monthrange

# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2021, 2))
# Saída - (5, 29)
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês

# Caso queira retornar apenas um valor,
# você pode fazer o desempacotamento
dia_semana, ultimo_dia = monthrange(2021, 2)
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)

# Você também pode criar uma lista, assim como mdays,
# contendo todos os últimos dias de meses do ano atual.
ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
# Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Observação: meu ano atual é 2020 neste momento
