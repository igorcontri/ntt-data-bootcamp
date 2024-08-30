import datetime

d = datetime.datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M")) # 19/07/2023 14:20

# Convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d) # 2023-07-20 15:30:00