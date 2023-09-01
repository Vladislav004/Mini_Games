# Craps Roller
# Программа суммирует два случайных числа и выводит сумму пользователю

import random

# Генерация случайных чисел от 1 до 6

# Использование варианта с randint
die1 = random.randint(1, 6)
# Использование варианта с randrange
die2 = random.randrange(6) + 1

# Сумма выпавших значений
total = die1 + die2

# Вывод пользователю
print("You rolled a", die1, "and a", die2, "for a total of", total)
