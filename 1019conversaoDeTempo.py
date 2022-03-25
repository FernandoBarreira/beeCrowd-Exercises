tempo = int(input())
hora = tempo // 3600
tempo = tempo - hora * 3600
minuto = tempo // 60
segundo = tempo % 60
print(f'{hora}:{minuto}:{segundo}')




