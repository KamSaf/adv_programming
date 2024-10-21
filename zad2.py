
def check_arg_length(argument: list, length: int) -> bool:
    return len(argument) == length


def print_names(names: list[str]) -> None:
    if not check_arg_length(names, 5):
        print('Invalid names list length')
    for name in names:
        print(name)


def multiply_numbers(numbers: list[int]) -> list[int] | None:
    if not check_arg_length(numbers, 5):
        print('Invalid numbers list length')
    for index, num in enumerate(numbers):
        numbers[index] = num*2
    return numbers


def multiply_numbers_alt(numbers: list[int]) -> list[int] | None:
    if not check_arg_length(numbers, 5):
        print('Invalid numbers list length')
    return [num*2 for num in numbers]


def print_even_numbers(numbers: list[int]) -> None:
    if not check_arg_length(numbers, 10):
        print('Invalid numbers list length')
    for num in numbers:
        if num % 2 == 0:
            print(num)


def print_every_other_number(numbers: list[int]) -> None:
    if not check_arg_length(numbers, 10):
        print('Invalid numbers list length')
    for i in range(10):
        if i % 2 != 0:
            print(numbers[i])
