# https://docs.python.org/3/library/datetime.html

from datetime import datetime, timedelta

# data = datetime(ano, mes, dia, hora[opcional], minuto[opcional], segundo[opcional])
data = datetime(2021, 3, 24)
# strptime(str, fmt)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
#
# print(datetime.strptime('20/04/2019', '%d/%m/%Y'))
# print(data.timestamp())
# print(datetime.fromtimestamp(1616554800.0))

# timedelta modifica datas
data = data + timedelta(days=5, seconds=59)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# diferença entre datas
d1 = datetime.strptime('20/04/2019 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/2019 21:30:00', '%d/%m/%Y %H:%M:%S')
diff = d2 - d1
print(diff)
print(diff.seconds)
print(diff.total_seconds())
print(diff.days)

print(d1.time())
