def get_multiplied_digits(number):
    str_number = str(number)
    a_rep = str_number.replace('0', '')
    first = a_rep[0]
    if len(a_rep) > 1:
        first_i = int(first)
        return first_i * get_multiplied_digits(int(a_rep[1:]))
    else:
        first_i = int(first)
        return first_i

result = get_multiplied_digits(40203)
print(result)
