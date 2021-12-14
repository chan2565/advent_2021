with open("day3_input.txt") as file:
    lines = file.readlines()

#with open("day3_ex_input.txt") as file:
#    lines = file.readlines()


def find_counts(input_list, index):
    zero_count = 0
    one_count = 0

    for line in input_list:
        if line[index] == "0":
            zero_count += 1
        elif line[index] == "1":
            one_count += 1
        else:
            continue
    
    return zero_count, one_count


def find_matches(input_list, index):
    o2_match = []
    co2_match = []

    zero_count, one_count = find_counts(input_list, index)

    if one_count >= zero_count:
        for line in input_list:
            if line[index] == "1":
                o2_match.append(line)
            elif line[index] == "0":
                co2_match.append(line)
            else:
                continue
    elif zero_count > one_count:
        for line in input_list:
            if line[index] == "1":
                co2_match.append(line)
            elif line[index] == "0":
                o2_match.append(line)
            else:
                continue
    else:
        print("Most/least common determination failed.")
    
    return o2_match, co2_match


def find_o2_gen(input_list, start_index):
    curr_index = start_index
    curr_list = input_list
    while len(curr_list) > 1:
        curr_list, derp = find_matches(curr_list, curr_index)
        curr_index += 1
    return curr_list


def find_co2_gen(input_list, start_index):
    curr_index = start_index
    curr_list = input_list
    while len(curr_list) > 1:
        derp, curr_list = find_matches(curr_list, curr_index)
        curr_index += 1
    return curr_list

o2_gen_raw = find_o2_gen(lines, 0)
co2_gen_raw = find_co2_gen(lines, 0)
o2_gen = int(o2_gen_raw[0], 2)
co2_gen = int(co2_gen_raw[0], 2)
print(f"{o2_gen} * {co2_gen} = {o2_gen * co2_gen}")