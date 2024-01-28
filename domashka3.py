import re

def normalize_phone(phone_number):
    clean_number = re.sub(r'[^0-9+]', '', phone_number)
    
    if clean_number.startswith('+'):
        return clean_number
    elif clean_number.startswith('38'):
        return '+' + clean_number[::]
    else:
        return '+38' + clean_number[::]

phone_numbers = [
    "+38(050)123-32-34",
    "0503451234ggg",
    "***(050)8889900",
    "yyyy38050-111-22-22",
    "3t8050 111 22 11   "
]

for i in phone_numbers:
    normalized_number = normalize_phone(i)
    print('Вiдредактованi номери: ', normalized_number)
