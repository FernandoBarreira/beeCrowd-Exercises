t = int(input())
hr = t // 3600
t = t - hr * 3600
min = t // 60
sec = t % 60
print(f'{hr}:{min}:{sec}')



