from PlatesList import plates_list
from plate_number_processor import get_number_sum, chek_plate_number

print('Type "exit" to quit the program.')
unique_numbers = set(plates_list)

while True:
    plate_number = input('Input interested plate number: ').upper()
    if chek_plate_number(plate_number):
        number_sum = get_number_sum(plate_number[2:6])
        if plate_number in plates_list:
            print(f'Plate number {plate_number} in the "Plate list": FOUND')
        else:
            print(f'Plate number {plate_number} in the "Plate list": NOT FOUND')
        print(f'The sum of digits: {number_sum}\n'
              f'Unique plates in the "Plate list": {len(unique_numbers)}')
    elif plate_number == 'EXIT':
        print('Bye, bye!')
        break
    else:
        print(f'Invalid input! Please try again.')
