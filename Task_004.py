# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# Пример:

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек шоколадки по длинне n: '))
m = int(input('Введите количество долек шоколадки по ширыне m: '))
k = int(input('Введите количество долек которые желаете отломить k: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print(n, m, k, '-> yes')
else:
    print(n, m, k, '-> no')
