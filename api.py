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