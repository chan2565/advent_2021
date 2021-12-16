# TODO - Optimize this. Currently ends with a memory error. Pypy is faster, but still.
def sim_fish(list, days):
    while True:
        index = 0
        length = len(list)
        while index < length:
            if list[index]:
                list[index] -= 1
            else:
                list[index] = 6
                list.append(8)
            index += 1
        days -= 1
        print(f"Days left {days}")
        if days == 0:
            break
    print(f"Total fish: {len(list)}")


if __name__ == "__main__":
    #with open("day6_input.txt") as file:
    #    lines = file.readlines()

    with open("day6_ex_input.txt") as file:
        lines = file.readlines()
    
    initial = lines[0].strip().split(",")
    initial = list(map(lambda f: int(f), initial))
    print(initial)

    sim_fish(initial.copy(), 256)