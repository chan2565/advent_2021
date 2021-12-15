from day5_part1 import load_points, build_diagram, find_overlaps

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
        if abs(delta_x) > 0 and abs(delta_y) > 0:
            for delta in range(abs(delta_x) + 1):
                if delta_x > 0 and delta_y > 0:
                    diagram[y1 - delta][x1 - delta] += 1
                elif delta_x > 0 and delta_y < 0:
                    diagram[y1 + delta][x1 - delta] += 1
                elif delta_x < 0 and delta_y > 0:
                    diagram[y1 - delta][x1 + delta] += 1
                elif delta_x < 0 and delta_y < 0:
                    diagram[y1 + delta][x1 + delta] += 1
                else:
                    print("INVALID")
                    break
    #for line in diagram:
    #    print(line)


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