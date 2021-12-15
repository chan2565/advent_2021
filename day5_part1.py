def load_points(lines, start_points, end_points):
    for line in lines:
        line_split = line.strip().split(" -> ")
        # Convert strings to tuples
        start_points.append(eval(line_split[0]))
        end_points.append(eval(line_split[1]))

def build_diagram(start_points, end_points, diagram):
    max_x = 0
    max_y = 0
    row = []

    for start in start_points:
        x,y = start
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    for end in end_points:
        x,y = end
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    for x in range(max_x + 1):
        row.append(0)
    for y in range(max_y + 1):
        diagram.append(row.copy())

def mark_diagram(start_points, end_points, diagram):
    num_lines = len(start_points)
    for index in range(num_lines):
        x1,y1 = start_points[index]
        x2,y2 = end_points[index]
        delta_x = x1 - x2
        delta_y = y1 - y2
        if delta_y == 0:
            for x in range(abs(delta_x) + 1):
                if delta_x > 0:
                    diagram[y1][x1 - x] += 1
                else:
                    diagram[y1][x1 + x] += 1
        if delta_x == 0:
            for y in range(abs(delta_y) + 1):
                if delta_y > 0:
                    diagram[y1 - y][x1] += 1
                else:
                    diagram[y1 + y][x1] += 1
    #for line in diagram:
    #    print(line)

def find_overlaps(diagram):
    overlaps = 0
    for row in diagram:
        for col in row:
            if col >= 2:
                overlaps += 1
    print(overlaps)


if __name__ == "__main__":
    with open("day5_input.txt") as file:
        lines = file.readlines()

    #with open("day5_ex_input.txt") as file:
    #    lines = file.readlines()

    start_points = []
    end_points = []
    diagram = []

    load_points(lines, start_points, end_points)
    build_diagram(start_points, end_points, diagram)
    mark_diagram(start_points, end_points, diagram)
    find_overlaps(diagram)
