def is_opening_symbol(symbol):
    if symbol in ['(', '[', '{', '<']:
        return True
    return False

def is_closing_symbol(symbol):
    if symbol in [')', ']', '}', '>']:
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

def get_matching_closing_symbol(symbol):
    if symbol == '(':
        return ')'
    elif symbol == '[':
        return ']'
    elif symbol == '{':
        return '}'
    else:
        return '>'


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


def get_repair_points(symbol):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    return points[symbol]


def calculate_repair_score(added_symbols):
    repair_score = 0
    for symbol in added_symbols:
        repair_score = (repair_score * 5) + get_repair_points(symbol)
    return repair_score


def complete_line(line):
    symbol_stack = []
    added_symbols = ""
    for symbol in "".join(reversed(line)):
        if is_closing_symbol(symbol):
            symbol_stack.append(symbol)
        else:
            if get_matching_closing_symbol(symbol) in symbol_stack:
                symbol_stack.reverse()
                symbol_stack.remove(get_matching_closing_symbol(symbol))
                symbol_stack.reverse()
            else:
                added_symbols += get_matching_closing_symbol(symbol)
    return calculate_repair_score(added_symbols)


def step1():
    file = open("input.txt", "r")
    lines = file.read().splitlines()

    error_score = 0
    for line in lines:
        error_score += verify_line(line)
    print(error_score)


def step2():
    file = open("input.txt", "r")
    lines = file.read().splitlines()
    corrupted_lines = []
    for line in lines:
        if verify_line(line) == 0:
            corrupted_lines.append(line)

    repair_scores = []
    for line in corrupted_lines:
        repair_scores.append(complete_line(line))
    repair_scores.sort()
    print(repair_scores[round(len(repair_scores) / 2)])

step2()


