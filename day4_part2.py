with open("day4_input.txt") as file:
    lines = file.readlines()

#with open("day4_ex_input.txt") as file:
#    lines = file.readlines()

draws = lines[0].strip().split(",")
all_boards = lines[2:]
all_boards.append("\n")
board_list = []

class BingoBoard:
    def __init__(self, rows):
        self.rows = rows
        self.marks = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]
    
    def mark_board(self, num):
        curr_row = 0
        curr_col = 0
        for row in self.rows:
            for space in row:
                if num == space:
                    self.marks[curr_row][curr_col] = "x"
                curr_col += 1
            curr_col = 0
            curr_row += 1
    
    def calc_unmarked(self):
        sum = 0
        curr_row = 0
        curr_col = 0
        for row in self.marks:
            for space in row:
                if space == "":
                    sum += int(self.rows[curr_row][curr_col])
                curr_col += 1
            curr_col = 0
            curr_row +=1
        return sum

    def check_board(self):
        # Check columns
        curr_row = 0
        curr_col = 0
        while curr_col < len(self.marks[0]):
            if curr_row >= len(self.marks):
                return self.calc_unmarked()
            elif self.marks[curr_row][curr_col] == "x":
                curr_row += 1
                continue
            else:
                curr_col += 1
                curr_row = 0

        # Check rows
        for row in self.marks:
            if row[0] == "x" and row[1] == "x" and row[2] == "x" and row[3] == "x" and row[4] == "x":
                return self.calc_unmarked()
        
        # Return 0 if no bingo
        return 0

def load_boards(all_boards, board_list):
    curr_board = []
    for line in all_boards:
        if line == "\n":
            new_board = BingoBoard(curr_board)
            board_list.append(new_board)
            curr_board = []
        else:
            curr_board.append(line.strip().split())


def mark_boards(board_list):
    for num in draws:
        board_index = 0
        remove_list = []
        while board_index < len(board_list):
            board_list[board_index].mark_board(num)
            result = board_list[board_index].check_board()
            if result > 0:
                print(f"sum unmarked = {result} current num = {num}")
                print(f"{result} * {num} = {result * int(num)}")
                print(board_list[board_index].marks)
                remove_list.append(board_list[board_index])
            board_index += 1
        for board in remove_list:
            board_list.remove(board)

load_boards(all_boards, board_list)
mark_boards(board_list)
