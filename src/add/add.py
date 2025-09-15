import re

from .exceptions import NegativeNumberException, WrongFormatException


def add(numbers: str) -> int:
    if numbers == "":
        return 0

    if numbers.startswith("//"):
        delimiter_sets, numbers = numbers.split("\n", 1)
        delimiter_sets = delimiter_sets.lstrip("//")

        if len(delimiter_sets) > 1:
            if not delimiter_sets.startswith("[") or not delimiter_sets.endswith("]"):
                raise WrongFormatException(
                    "Multi-char delimiter should be wrapped inside brackets"
                )
            delimiters = re.findall(r"\[(.*?)\]", delimiter_sets)
        else:
            delimiters = [delimiter_sets]
    else:
        delimiters = [","]

    delimiter_regex = "\n"
    for delimiter in delimiters:
        delimiter_regex += f"|{re.escape(delimiter)}"

    total = 0
    negative_numbers = ""
    for number in re.split(delimiter_regex, numbers):
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
