def optimize_pos(positions):
    pos_min = min(positions)
    pos_max = max(positions)

    fuel_costs = []

    for index in range(pos_min, pos_max):
        total_cost = 0
        for position in positions:
            fuel_cost = abs(position - index)
            total_cost += fuel_cost * (fuel_cost + 1) // 2
        fuel_costs.append(total_cost)
    
    min_fuel = min(fuel_costs)
    fuel_costs.index(min_fuel)

    print(f"Min fuel: {min_fuel} @ index: {index}")


if __name__ == "__main__":
    with open("day7_input.txt") as file:
        lines = file.readlines()

    #with open("day7_ex_input.txt") as file:
    #    lines = file.readlines()

    positions = lines[0].strip().split(",")
    positions = list(map(lambda f: int(f), positions))
    
    optimize_pos(positions)