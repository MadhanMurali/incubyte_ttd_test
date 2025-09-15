import re

from .exceptions import NegativeNumberException


def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        delimiter, numbers = numbers.split("\n", 1)
        delimiter = delimiter.lstrip("//")

    total = 0
    negative_numbers = ""
    for number in re.split(f"\n|{delimiter}", numbers):
        number_to_add = int(number)

        if number_to_add < 0:
            negative_numbers = (
                number_to_add
                if not negative_numbers
                else f"{negative_numbers},{number_to_add}"
            )
        elif number_to_add <= 1000 and not negative_numbers:
            total += number_to_add

    if negative_numbers:
        raise NegativeNumberException(f"negatives not allowed: {negative_numbers}")

    return total
