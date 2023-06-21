import pandas as pd

df = pd.read_csv('input.csv', encoding='utf-8')
dct = {}
for i in range(len(df)):
    if df['Фамилия водителя'][i] not in dct:
        dct[df['Фамилия водителя'][i]] = 0
        if df['Тип операции'][i] == 'Привоз':
            dct[df['Фамилия водителя'][i]] += df['Объем груза'][i]
        elif df['Тип операции'][i] == 'Вывоз':
            dct[df['Фамилия водителя'][i]] -= df['Объем груза'][i]
    else:
        if df['Тип операции'][i] == 'Привоз':
            dct[df['Фамилия водителя'][i]] += df['Объем груза'][i]
        elif df['Тип операции'][i] == 'Вывоз':
            dct[df['Фамилия водителя'][i]] -= df['Объем груза'][i]
dct1 = {'Фамилия водителя': list(dct.keys()),
        'Объем груза': list(dct.values())}
df1 = pd.DataFrame(dct1, columns=dct1.keys())
df1.to_csv('output.csv', encoding='utf-8', index=False)
