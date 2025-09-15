def add(numbers: str) -> int:
    if numbers == "":
        return 0

    total = 0
    numbers_list = numbers.split(",")

    if len(numbers_list) == 1:
        total = int(numbers_list[0])
    elif len(numbers_list) == 2:
        total = int(numbers_list[0]) + int(numbers_list[1])

    return total
