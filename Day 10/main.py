def is_opening_symbol(symbol):
    if symbol in ['(', '[', '{', '<']:
        return True
    return False


def get_matching_opening_symbol(symbol):
    if symbol == ')':
        return '('
    elif symbol == ']':
        return '['
    elif symbol == '}':
        return '{'
    else:
        return '<'


def get_error_points(symbol):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return points[symbol]

def get_last_openings_symbol(stack):
    stack.reverse()
    for symbol in stack:
        if is_opening_symbol(symbol):
            stack.reverse()
            return symbol
    stack.reverse()
    return ""


def verify_line(line):
    symbol_stack = []
    temp_line = ""
    for symbol in line:
        print(symbol_stack)
        temp_line += symbol
        if is_opening_symbol(symbol):
            symbol_stack.append(symbol)
        else:
            if get_matching_opening_symbol(symbol) in symbol_stack and get_last_openings_symbol(symbol_stack) == get_matching_opening_symbol(symbol):
                symbol_stack.reverse()
                symbol_stack.remove(get_matching_opening_symbol(symbol))
                symbol_stack.reverse()
            else:
                return get_error_points(symbol)
    return 0


def step1():
    file = open("input.txt", "r")
    lines = file.read().splitlines()

    error_score = 0
    for line in lines:
        error_score += verify_line(line)
    print(error_score)

def step2():
    pass

step1()


