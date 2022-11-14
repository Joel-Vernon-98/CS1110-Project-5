# Constants
VALID_OPERATIONS = ("|", "&", "^", "q")
VALID_HEX_DIGITS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
HEX_VALUES = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
              "4": "0100", "5": "0101", "6": "0110", "7": "0111",
              "8": "1000", "9": "1001", "A": "1010", "B": "1011",
              "C": "1100", "D": "1101", "E": "1110", "F": "1111",
              }


def is_valid_hex_string(hex_string: str) -> bool:
    text = "Please enter an 8-digit hexadecimal integer"
    if len(hex_string) > 8:
        print(text)
        return False
    for digit in hex_string:
        if digit in VALID_HEX_DIGITS:
            continue
        print(text)
        return False
    return True


def get_operation() -> str:
    text = "Please enter |, &, ^, or q"
    while True:
        operation = input("Enter operation: ")
        if operation in VALID_OPERATIONS:
            return operation
        print(text)


def get_integer_count() -> int:
    while True:
        integer_count = input("Enter number of integers: ")
        try:
            integer_count = int(integer_count)
            if integer_count < 2:
                raise ValueError
            return integer_count
        except ValueError:
            print(f"Error: Please enter an integer value greater than 1.")


def hex_operation(integer_list: list[str], operator: str, step=0) -> list[str]:
    result = hex(eval(f"{integer_list[step]} {operator} {integer_list[-1]}"))
    if step == 0:
        integer_list.append(result)
    if step == len(integer_list) - 2:
        return integer_list
    integer_list[-1] = result
    return hex_operation(integer_list, operator, step + 1)


def binary_operation(integer_list: list[str]) -> list[str]:
    result = []
    for hex_integer in integer_list:
        binary_string = ""
        hex_integer = hex_integer.removeprefix("0x")
        hex_digits = string_split(hex_integer, 1)
        for hex_digit in hex_digits:
            binary_string += HEX_VALUES[hex_digit.upper()]
        result.append(binary_string)
    return result


def string_split(input_string, split_length):
    i = 0
    result = []
    while i < len(input_string):
        result.append(input_string[i:i + split_length])
        i = i + split_length
    return result


def hex_formatter(hex_string: str) -> str:
    return hex_string.removeprefix("0x").zfill(8).upper()


def binary_formatter(binary_string: str) -> str:
    binary_string = binary_string.removeprefix("0b").zfill(32)
    byte_list = string_split(binary_string, 8)
    return "  ".join(byte_list)


def print_results(hex_integers: list[str], binary_integers: list[str], operator):
    print("Hexadecimal operation: ")
    i = 0
    while i < len(hex_integers):
        if i == 0:
            print(f"  {hex_formatter(hex_integers[i])}")
        elif i == len(hex_integers) - 1:
            print(f"= {hex_formatter(hex_integers[i])}")
        else:
            print(f"{operator} {hex_formatter(hex_integers[i])}")
        i += 1

    print("Binary operation:")
    i = 0
    while i < len(binary_integers):
        if i == 0:
            print(f"  {binary_formatter(binary_integers[i])}")
        elif i == len(binary_integers) - 1:
            print(f"= {binary_formatter(binary_integers[i])}")
        else:
            print(f"{operator} {binary_formatter(binary_integers[i])}")
        i += 1
