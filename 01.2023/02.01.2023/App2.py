# 1
from random import random

arr = [random() * 2000 for i in range(0, int(random() * 15))]
print(arr)
file = open("arrFile.txt", "w")
for i in range(len(arr)):
    file.write((str(arr[i]) + ", "))
file.close()
file = open("arrFile.txt", "r")
print(file.readline())

# 2
file = open("2File.txt", "w", encoding="utf-8")
file.write("")
file.close()
file = open("2File.txt", "a", encoding="utf-8")
file.write("1\n2\n")
userStr = input("Введите желаемую строку: ")
file.write(userStr)

# 3
word = input("Введите слово для поиска: ")
i = 0
if word == "":
    exit()

with open("text.txt", encoding="utf-8") as file:
    for line in file:
        i += 1
        if word in line:
            wordFromFile = word + f" : находится в строке {i}"
if wordFromFile == "":
    print("Слова нету в файле!")
else:
    print(wordFromFile)

# 4
with open('text.txt') as myfile:
    count = sum(1 for line in myfile)
print(count)

# 5
lst = []
with open('text.txt') as myfile:
    for line in myfile:
        lst.append(line.strip('\n'))
    lst = sorted(lst)
with open('text.txt', 'w') as myfile:
    for i in lst:
        myfile.write(i)
