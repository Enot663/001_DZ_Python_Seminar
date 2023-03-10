# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# Пример:

# 385916 -> yes
# 123456 -> no

a = input('Введите номер билета из шести цифр: ') # Предложение пользователю ввести номер билета в строковой форме.
sum1 = int(a[0]) + int(a[1]) + int(a[2]) # вычисление суммы првых трех чисел
sum2 = int(a[3]) + int(a[4]) + int(a[5]) # вычисление суммы последних трех чисел
if sum1 == sum2: # сравнение суммы  чисел 
    print(a, '-> yes') # при совпадении суммы чисел билет счастливый 
else:
    print(a, '-> no') # иначе нет 

