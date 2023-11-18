# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
num = int(input('Enter a number to converse: '))
digits = '0123456789abcdef'
res = ''
while num > 0:
    res = digits[num%16]+res
    num = num//16
print(res)

# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
s = input("Enter the line to analyze: ")
count_digit = 0
count_mark = 0
for i in s:
    if i.isdigit():
        count_digit += 1
    if i == "." or i == ",":
        count_mark += 1
    if i.isalpha():
        print("String is't a fractional number")
        break
if count_digit > 0 and 0 < count_mark < 2:
    print("String is a fractional number")
else:
    print("String is't a fractional number")

# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.
s = input("Enter the line to analyze: ")
letter = 'о'
count = 0
for i in s:
    if i == letter: count += 1
if count > 0:
    first_o = s.find(letter)
    last_o = s.rfind(letter)
    sub_s = s[first_o+1:last_o]
    invert_sub = sub_s[::-1]
    print(s[:first_o+1], invert_sub, s[last_o:])
else:
    print(f'Letter "о" occurs -> {count}')
