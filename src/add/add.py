import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    delimiter = ","
    if numbers.startswith("//"):
        delimiter, numbers = numbers.split("\n", 1)
        delimiter = delimiter.lstrip("//")

    total = 0
    for number in re.split(f"\n|{delimiter}", numbers):
        total += int(number)

    return total
