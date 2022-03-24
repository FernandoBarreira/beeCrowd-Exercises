dias = int(input())
d = dias
ano = d // 365
d = d - ano * 365
mes = d // 30
d = d - mes * 30
dia = d % 30
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')


