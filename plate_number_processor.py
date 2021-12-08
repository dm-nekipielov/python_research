from PlatesList import plates_list

while True:
    plate_number = input("Please enter your desired plate No: ").upper()
    rules = [len(plate_number) == 8,
             plate_number[0: 2].isalpha(),
             plate_number[2: 6].isdigit(),
             plate_number[-2:].isalpha()]
    # print(rules)
    if not all(rules):
        print(f'Invalid input! Please try again.')
        continue
    elif plate_number in plates_list:
        print(f'Plate number {plate_number} in the "Plate list": FOUND')
    else:
        print(f'Plate number {plate_number} in the "Plate list": NOT FOUND')
