"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = float(input("Введите результат первого дня в км: "))
b = float(input("Введите результат, к которому стремится спортсмен в км: "))
result_day = 1
while a < b:
    print(f"{result_day}-й день: {'%.2f' % a} км")
    a = a + a/10
    result_day += 1
print(f"{result_day}-й день: {'%.2f' % a} км")
print(f"Ответ: на {result_day}-й день спортсмен достиг результата — не менее {b} км.")
