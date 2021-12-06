from PlatesList import plates_list
import re



# Надо определить сколько номерных знаков в этом списке уникальны
# Надо узнать есть ли введенный с клавиатуры номер в списке (без учета регистра букв)
# Надо узнать сумму всех чисел во введенном номере

unique_numbers = set(plates_list)

while True:
    plate_number = input('Input interested plate number: ').upper()
    if bool(re.fullmatch(r"^[A-Z]{2}\d{4}[A-Z]{2}$", plate_number)):
        if plate_number in plates_list:
            print(f'Plate number {plate_number} in the "Plate list": FOUND')
        else:
            print(f'Plate number {plate_number} in the "Plate list": NOT FOUND')
        break
    else:
        print(f'Invalid input! Please try again.')

number_sum = 0
for i in range(len(plate_number)):
    if plate_number[i].isdigit():
        number_sum += int(plate_number[i])

print(f'The sum of digits: {number_sum}')
print(f'Unique plates in the "Plate list": {len(unique_numbers)}')
