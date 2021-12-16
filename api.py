import requests

# Reads in session cookie data from session.txt file
with open("session.txt") as file:
    lines = file.readlines()
cookies = {'session': lines[0]}

# Pulls the input data down and writes it to a file for use in other scripts.
# Returns the file name that was written to.
def get_input(day):
    url = f"https://adventofcode.com/2021/day/{day}/input"
    file_name = f"day{day}_input.txt"
    req = requests.get(url=url, cookies=cookies)
    with open(file_name, mode="w") as file:
        file.write(req.text)
    return file_name

# Creates the rest of the initial files needed for the day
def init(day):
    part1_file = f"day{day}_part1.py"
    part2_file = f"day{day}_part2.py"
    ex_file = f"day{day}_ex_input.txt"

    starter_txt = f'\n\n\n\nif __name__ == "__main__":\n    #with open("day6_input.txt") as file:\n    #    lines = file.readlines()\n\n    with open("day6_ex_input.txt") as file:\n        lines = file.readlines()'

    with open(part1_file, mode="w") as file:
        file.write(starter_txt)
    with open(part2_file, mode="w") as file:
        file.write(starter_txt)
    with open(ex_file, mode="w") as file:
        file.write("")

# Submits your answer and prints a short message if it's right or wrong.
# Also returns the response object for debugging, etc.
def submit_answer(day, part, answer):
    url = f"https://adventofcode.com/2021/day/{day}/answer"
    form_data = {"level": part, "answer": answer}
    req = requests.post(url, data=form_data, cookies=cookies)
    if "That\'s the right answer!" in req.text:
        print("CORRECT!")
    else:
        print("WRONG...")
    return req