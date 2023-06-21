import csv

d = []
with open("fly.txt", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        d.append(row)

print("Введите номер")
fly = input().upper()
d1 = []
for i in d:
    if i.get("номер рейса") == fly:
        d1.append(i)
if len(d1) == 0:
    print("Не найден")
else:
    for i in d1:
        print(f"{i.get('название пункта назначения рейса')} {i.get('номер рейса')} {i.get('тип самолета')}")
