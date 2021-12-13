with open("day1_input.txt") as file:
    lines = file.readlines()

# lines = ["199", "200", "208", "210", "200", "207", "240", "269", "260", "263"]

count = 0
win_start = 0
prev_sum = 99999

while(win_start + 2 < len(lines)):
    sum = int(lines[win_start]) + int(lines[win_start + 1]) + int(lines[win_start + 2])
    if sum > prev_sum:
        count += 1
    prev_sum = sum
    win_start += 1

print(count)