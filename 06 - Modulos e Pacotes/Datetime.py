import datetime

agora = datetime.datetime.now()

t = datetime.time(7, 43, 28)

print(t)
print('Hora  :', t.hour)
print('Minute:', t.minute)
print('Segundo:', t.second)
print('Microsegundo:', t.microsecond)
print(datetime.time.min)

hoje = datetime.date.today()

print(hoje)
print('ctime:', hoje.ctime())
print('Ano:', hoje.year)
print('Mês :', hoje.month)
print('Dia :', hoje.day)

d1 = datetime.date(2015, 4, 28)
print('d1:', d1)

d2 = d1.replace(year=2016)
print('d2:', d2)

# Diferença em dias entre duas datas
print(d2 - d1)
