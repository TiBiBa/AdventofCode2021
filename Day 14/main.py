
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
    file = open("input.txt", "r")
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
    #Idea: Restructure to dict of count
    #Each pair results in two new pairs, add these as values
    #Then, for each pair repeat the process 40 times
    #Count char of each key in the dict and sum
    pass

step1()