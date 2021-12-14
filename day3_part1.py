with open("day3_input.txt") as file:
    lines = file.readlines()

# What am I doing...
zero_0 = 0
one_0 = 0
zero_1 = 0
one_1 = 0
zero_2 = 0
one_2 = 0
zero_3 = 0
one_3 = 0
zero_4 = 0
one_4 = 0
zero_5 = 0
one_5 = 0
zero_6 = 0
one_6 = 0
zero_7 = 0
one_7 = 0
zero_8 = 0
one_8 = 0
zero_9 = 0
one_9 = 0
zero_10 = 0
one_10 = 0
zero_11 = 0
one_11 = 0

# Buckle up, this is a wild ride
for line in lines:
    zero_0 += int(not int(line[0]))
    one_0 += int(line[0])
    zero_1 += int(not int(line[1]))
    one_1 += int(line[1])
    zero_2 += int(not int(line[2]))
    one_2 += int(line[2])
    zero_3 += int(not int(line[3]))
    one_3 += int(line[3])
    zero_4 += int(not int(line[4]))
    one_4 += int(line[4])
    zero_5 += int(not int(line[5]))
    one_5 += int(line[5])
    zero_6 += int(not int(line[6]))
    one_6 += int(line[6])
    zero_7 += int(not int(line[7]))
    one_7 += int(line[7])
    zero_8 += int(not int(line[8]))
    one_8 += int(line[8])
    zero_9 += int(not int(line[9]))
    one_9 += int(line[9])
    zero_10 += int(not int(line[10]))
    one_10 += int(line[10])
    zero_11 += int(not int(line[11]))
    one_11 += int(line[11])

# Variable name hell anyone?
if zero_0 > one_0:
    zero = 0
else:
    zero = 1

if zero_1 > one_1:
    one = 0
else:
    one = 1

if zero_2 > one_2:
    two = 0
else:
    two = 1

if zero_3 > one_3:
    three = 0
else:
    three = 1

if zero_4 > one_4:
    four = 0
else:
    four = 1

if zero_5 > one_5:
    five = 0
else:
    five = 1

if zero_6 > one_6:
    six = 0
else:
    six = 1

if zero_7 > one_7:
    seven = 0
else:
    seven = 1

if zero_8 > one_8:
    eight = 0
else:
    eight = 1

if zero_9 > one_9:
    nine = 0
else:
    nine = 1

if zero_10 > one_10:
    ten = 0
else:
    ten = 1

if zero_11 > one_11:
    eleven = 0
else:
    eleven = 1


# At this point I'm commited to this ridiculousness
gamma = f"{zero}{one}{two}{three}{four}{five}{six}{seven}{eight}{nine}{ten}{eleven}"
print(gamma)
epsilon = f"{int(not zero)}{int(not one)}{int(not two)}{int(not three)}{int(not four)}{int(not five)}{int(not six)}{int(not seven)}{int(not eight)}{int(not nine)}{int(not ten)}{int(not eleven)}"
print(epsilon)
int_gamma = int(gamma, 2)
int_epsilon = int(epsilon, 2)

# If you've made it this far, bravo! I would never do this in the real world, but it was fun to write myself out of that corner. It works! lol
print(f"{int_gamma} * {int_epsilon} = {int_gamma * int_epsilon}")
