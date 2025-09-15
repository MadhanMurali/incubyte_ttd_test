import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0

    total = 0
    for number in re.split("\n|,", numbers):
        total += int(number)

    return total
