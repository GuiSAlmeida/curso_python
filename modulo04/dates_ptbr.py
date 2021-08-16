from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime.now()
mes_atual = int(data.strftime('%m'))
formatacao1 = data.strftime('%A, %d de %B de %Y')
formatacao2 = data.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)

# total dias do mes
print(mes_atual, mdays[mes_atual])
