with open("day2_input.txt") as file:
    lines = file.readlines()

x = 0
y = 0
aim = 0

for line in lines:
    line_split = line.split()
    direction = line_split[0]
    amount = line_split[1]
    if direction == "forward":
        x += int(amount)
        y += int(amount) * aim
    elif direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)
    else:
        continue

print(f"{x} * {y} = {x*y}")