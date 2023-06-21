import csv

print("Введите место назначения")
dest = input().upper()
print("Введите номер рейса")
num = input().upper()
print("Введите тип")
air = input().upper()

with open("fly.txt", mode="a", encoding="utf-8", newline="") as f:
    file_writer = csv.writer(f, delimiter=";", lineterminator="\r")
    file_writer.writerow([dest, num, air])
