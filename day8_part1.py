def find_instances(lines):
    instances = 0
    
    for line in lines:
        out_vals = line.strip().split(" | ")[1]
        #print(out_vals)
        out_vals_split = out_vals.split()
        #print(out_vals_split)
        for val in out_vals_split:
           if (len(val) == 2) or (len(val) == 4) or (len(val) == 3) or (len(val) == 7):
               instances += 1
    
    print(instances)



if __name__ == "__main__":
    with open("day8_input.txt") as file:
        lines = file.readlines()

    #with open("day8_ex_input.txt") as file:
    #    lines = file.readlines()
    
    find_instances(lines)

