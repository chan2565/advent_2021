with open("day1_input.txt") as file:
    lines = file.readlines()

prev_line = 99999
count = 0
for line in lines:
    if int(line) > prev_line:
        count += 1
    prev_line = int(line)

print(count)