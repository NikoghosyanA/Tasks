import random

card = ["Шесть", "Семь", "Восемь", "Девять", "Десять", "Валет", "Дама", "Король", "Туз"]
mast = ["Червы", "Бубны", "Пики", "Трефы"]
random_mast = random.choice(mast)
random_element = random.choice(card)
print(random_element + " " + random_mast)
