#Кешко Маргарита
import random #импортируем модуль рандома
from itertools import combinations #импортируем функцию для создания комбинаций 
random_combinations = [tuple(random.randint(-10, 10) for _ in range(4)) for _ in range(20)]#создаем список из 20 кортежей
print("Случайные комбинации (20 штук, по 4 числа в каждой):")#выводим текст 
for i, comb in enumerate(random_combinations, 1):#создаем цикл
    print(f"{i}: {comb}")#выводим номер комбинации
print()#пустая строка для эстетики
unique_combinations = set(tuple(sorted(comb)) for comb in random_combinations)#находим уникальные комбинации
print("Уникальные комбинации (отсортированные, без учета порядка):")#выводим текст для уникальных комб-ий
unique_list = list(unique_combinations)#преобразуем все в список
for i, comb in enumerate(unique_list, 1):#создаем цикл
    print(f"{i}: {comb}")#выводим номер и содержимое
print(f"Всего уникальных комбинаций: {len(unique_list)}")#выводим кол-во
print()#пустая строка для эстетики
try:
    target_sum = int(input("Введите целое число для сравнения суммы пар: "))#получаем число от поль-ля
except ValueError:#если поль-ль ввел не число
    print("Ошибка: нужно ввести целое число!")#предупреждаем об ошибке
    exit()#завершаем программу
pair_count = 0#переменная для пар
all_pairs = []#список для хранения всех пар
for comb in unique_list:#создаем цикл
    for pair in combinations(comb, 2):#создаем цикл
        if sum(pair) < target_sum:#проверка, меньше ли сумма пары
            pair_count += 1#если условие выполненно, то увеличиваем счетчик
            all_pairs.append(pair)#добавляем пару
print(f"\nПары, сумма которых меньше {target_sum}:")#выводим пары
if all_pairs:#проверяем, есть ли найденные пары
    for i, pair in enumerate(all_pairs, 1):#создаем цикл для нумерации
        print(f"{i}: {pair} - сумма = {sum(pair)}")#выводим номер пары и саму пару
else:#
    print("Таких пар не найдено")#если пар не найдено
print(f"\nОбщее количество пар с суммой меньше {target_sum}: {pair_count}")#выводим общее кол-во найденных пар