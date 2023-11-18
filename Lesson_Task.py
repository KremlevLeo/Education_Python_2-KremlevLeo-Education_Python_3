# 3.1 Вводим с клавиатуры десятичное число. Необходимо перевести его в двоичную систему счисления.
import math

num = int(input('Enter a number to converse: '))
res = ''
while num > 0:
    if num % 2 == 1:
        res += "1"
    else:
        res += "0"
    num = num//2
print(res)

# 3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.

s = str(input("Введите строку:"))
count_a = 0
count_b = 0
vowels = set("ауоыиэяюёе")
simbols = set(".,?!:' ")
for letter in s:
    if letter in vowels:
        count_a += 1
    elif letter in simbols:
        continue
    else:
        count_b +=1
print("Количество гласных равно:")
print(count_a)
print("Количество согласных равно:")
print(count_b)

# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом

s = str(input("Enter string: "))
if s == s[-1::-1]:
    print("Yes")
else: print("No")

# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами

s = str(input("Enter string: "))
half = math.ceil(len(s)/2)
print(s[half], end=" ")
print(s[:half])

# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре

s = str(input("Enter string: "))
coun_up = 0
for i in s:
    if i.isupper():
        coun_up+=1
print(coun_up)


# 3.6 Безопасный пароль. Пользователь вбивает пароль. Нужно сказать - безопасный он или нет. Безопасным считается, если он от 8 символов, есть верхний и нижний регистр. А так же цифры. Можеет, при желании, добавить и спец. символы

s = str(input("Enter password: "))
coun_up =0
coun_num =0
for i in s:
    if i.isupper(): coun_up+=1
    if i.isnumeric(): coun_num+=1
if len(s)<8: print("Password is simpl")
elif coun_up == 0: print("Password is simpl")
elif coun_num == 0: print("Password is simpl")
else: print("All Ok")

# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего

s = str(input("Enter for analiz: "))
c = dict()
for letter in s:
    c[letter] = c.get(letter, 0) + 1
res = max(c.items(), key=lambda item: item[1])[0]
print(f'The most common letter -> {res}')

# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"

s = str(input("Enter for analiz: "))
tmp = 0
res = ""
index = [i for i, x in enumerate(s) if x == 'в' or x == 'В']
print(f'Second "в" -> {index[1]}')
