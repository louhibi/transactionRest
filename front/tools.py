def clean_number(number):
    return number.replace(" ","").replace("-", "")

def is_valid_number(number):
    return is_number(number) and is_length(number, 10)

def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def is_length(number, length):
    return True if len(number)==length else False
