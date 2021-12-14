def chek_plate_number(value: str):
    '''
    The function verified a string against a format.\n
    :param value: string
    :return: Return a tuple of values
    '''
    rules = [len(value) == 8,
             value[:2].isalpha(),
             value[2: 6].isdigit(),
             value[-2:].isalpha()]
    if not all(rules):
        return False
    else:
        items = (value[:2], value[2: 6], value[-2:])
        return tuple([items[0]] + list(items[1]) + [items[2]])


def get_number_sum(value):
    '''
    :param value: should be an iterable object
    :return: Return the sum of values iterable object.
    '''
    value_sum = 0
    for i in value:
        value_sum += int(i)
    return value_sum
