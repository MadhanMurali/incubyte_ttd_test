def add(numbers: str) -> int:
    if numbers == "":
        return 0

    total = 0
    for number in numbers.split(","):
        total += int(number)

    return total
