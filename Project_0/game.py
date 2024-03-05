#play 'found the number'
import numpy as np
number = np.random.randint(1, 101) # number
count = 0
while True:
    count += 1
    predikt_number = int(input("Угадай число от 1 до 100"))
    if predikt_number > number:
        print("Число должно быть меньше!")

    elif predikt_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла