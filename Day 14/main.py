
def replace_mutations_by_dict(mutations):
    mutations_dict = {}
    for mutation in mutations:
        start = mutation.split("->")[0][:-1]
        end = mutation.split("->")[1][1:]

        mutations_dict[start] = end
    return mutations_dict


def check_mutation(mutations, substring):
    if substring in mutations:
        return mutations[substring]
    else:
        return None


def step1():
    file = open("example_input.txt", "r")
    file_data = file.read().splitlines()
    template = file_data[0]
    mutations = replace_mutations_by_dict(file_data[2:])

    for _ in range(0, 10):
        substrings = []
        for i in range(0, len(template)-1):
            substrings.append(template[i:i+2])
        for substring in substrings:
            mutation = check_mutation(mutations, substring)
            if mutation:
                location = template.find(substring)
                template = template[:location+1] + mutation + template[location+1:]
    for char in set(template):
        print(char + " has " + str(template.count(char)) + " occurrences")


def step2():
    file = open("input.txt", "r")
    file_data = file.read().splitlines()
    template = file_data[0]
    mutations = replace_mutations_by_dict(file_data[2:])

    substrings_dict = {}

    for i in range(0, len(template) - 1):
        if template[i:i + 2] in substrings_dict:
            substrings_dict[template[i:i + 2]] = substrings_dict[template[i:i + 2]] + 1
        else:
            substrings_dict[template[i:i + 2]] = 1

    for _ in range(0, 40):
        to_be_removed = {}
        substrings_dict_copy = substrings_dict.copy()
        for substring, count in substrings_dict.items():
            mutation = check_mutation(mutations, substring)
            if mutation:
                if substring in to_be_removed:
                    to_be_removed[substring] = to_be_removed[substring] + count
                else:
                    to_be_removed[substring] = count
                new_part1 = substring[0] + mutation
                new_part2 = mutation + substring[1]
                if new_part1 in substrings_dict_copy:
                    substrings_dict_copy[new_part1] = substrings_dict_copy[new_part1] + count
                else:
                    substrings_dict_copy[new_part1] = count
                if new_part2 in substrings_dict_copy:
                    substrings_dict_copy[new_part2] = substrings_dict_copy[new_part2] + count
                else:
                    substrings_dict_copy[new_part2] = count
        for substring, count in to_be_removed.items():
            substrings_dict_copy[substring] = substrings_dict_copy[substring] - count
        substrings_dict = substrings_dict_copy.copy()

    char_dict = {}
    for substring, count in substrings_dict.items():
        for char in substring:
            if char in char_dict:
                char_dict[char] = char_dict[char] + count
            else:
                char_dict[char] = count
    for char, count in char_dict.items():
        char_dict[char] = char_dict[char] / 2
    print("---------------------")
    print(char_dict)

    print({k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1])})

step2()
