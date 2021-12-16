def sim_fish(list, days):
    index = 0
    length = len(list)
    while index < length:
        if list[index] == 0:
            list[index] = 6
            list.append(8)
        else:
            list[index] -= 1
        index += 1
    days -= 1
    print(f"Days left {days}")
    if days > 0:
        sim_fish(list, days)
    else:
        print(f"Total fish: {len(list)}")
        return


if __name__ == "__main__":
    with open("day6_input.txt") as file:
        lines = file.readlines()

    #with open("day6_ex_input.txt") as file:
    #    lines = file.readlines()

    initial = lines[0].strip().split(",")
    initial = list(map(lambda f: int(f), initial))
    print(initial)

    #sim_fish(initial.copy(), 18)
    sim_fish(initial.copy(), 80)