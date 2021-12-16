def chek_plate_number(value: str):
    '''
    The function verified a string against a format.

    :param value: should be a string
    :return: Return a tuple of values | False
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
    Return a sum of values iterable object.

    :param value: should be an iterable object
    :return: Return type int
    '''
    value_sum = 0
    for i in value:
        value_sum += int(i)
    return value_sum
