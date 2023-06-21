brothers = []
for i in range(3):
    brothers.append(int(input(f'Сколько денег у {i+1}-го брата? ')))

average = round(sum(brothers) / 3)
print(f'У братьев итого {sum(brothers)} рублей')
print(f'Они поделили сумму по {average} рублей')

for i in range(3):
    if brothers[i] < average:
        print(f'{i+1}-й брат получил {average - brothers[i]} рублей')
    elif brothers[i] > average:
        greater = list(filter(lambda x: x > average, brothers))
        ratio = greater[0] / greater[len(greater)-1]
        give = []
        for j in range(3):
            if greater[0] == brothers[i]:
                give.append(int((average - brothers[j]) * ratio / len(greater)))
            else:
                give.append(int((average - brothers[j]) * (1 / ratio) / len(greater)))
        for j in range(3):
            if give[j] > 0:
                print(f'{i+1}-й брат отдал {j+1}-му брату {give[j]} рублей')
            else:
                print(f'{i+1}-й брат остался при той же сумме')
