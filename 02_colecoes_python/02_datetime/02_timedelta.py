import datetime

dt = datetime.datetime(2023, 7, 19, 13, 45)
print(dt) #2023-07-19 13:45:00

# Adicionando uma semana
dt = dt + datetime.timedelta(weeks=1)
print(dt) # 2023-07-26 13:45:00