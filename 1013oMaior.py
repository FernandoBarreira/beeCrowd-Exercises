'''
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a > b and a > c:
    print(f'{a} eh o maior')
elif b > a and b > c:
    print(f'{b} eh o maior')
else:
    print(f'{c} eh o maior')
'''
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorAB = (a + b + abs(a - b)) / 2
MaiorDeTodos = (maiorAB + c + abs(maiorAB - c)) / 2
print(f'{int(MaiorDeTodos)} eh o maior')


