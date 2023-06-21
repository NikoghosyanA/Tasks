def get_prov_and_village_or_city(c):
    prov = {
        'A': 'Newfoundland',
        'B': 'Nova Scotia',
        'C': 'Prince Edward Island',
        'E': 'New Brunswick',
        'G': 'Quebec',
        'H': 'Quebec',
        'J': 'Quebec',
        'K': 'Ontario',
        'L': 'Ontario',
        'M': 'Ontario',
        'N': 'Ontario',
        'P': 'Ontario',
        'R': 'Manitoba',
        'S': 'Saskatchewan',
        'T': 'Alberta',
        'V': 'British Columbia',
        'X': 'Nunavut or Northwest Territories',
        'Y': 'Yukon'
    }
    c = c.replace(' ', '')
    good_val = (c[0]+c[2]+c[4]).isalpha() and (c[1]+c[3]+c[5]).isdigit()
    if not good_val or c[0] not in prov:
        return 'Индекс некорректный.'
    return f'{ ["Городской","Сельский"][ int(c[1])==0 ] } адрес в провинции { prov[c[0]] }.'


code = input('-> ')
print(get_prov_and_village_or_city(code))
