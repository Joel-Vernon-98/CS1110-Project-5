import re
# Constants
HEX_VALUES = ["0000", "0001", "0010", "0011",
              "0100", "0101", "0110", "0111",
              "1000", "1001", "1010", "1011",
              "1100", "1101", "1110", "1111",
              ]


def is_valid_hex_string(hex_string: str) -> bool:
    text = "Please enter an 8-digit hexadecimal integer"
    if len(hex_string) <= 8 and re.search("^[a-fA-F0-9]*$", hex_string):
        return True
    print(text)
    return False


def get_operation() -> str:
    text = "Please enter |, &, ^, or q"
    while True:
        operation = input("Enter operation: ")
        if re.search("^[|^&q]$", operation):
            return operation
        print(text)


def get_integer_count() -> int:
    text = "Error: Please enter an integer value greater than 1."
    while True:
        integer_count = input("Enter number of integers: ")
        regex_string = "[2-9][0-9]*$|^[1-9][0-9]+$"
        if re.search(regex_string, integer_count):
            return int(integer_count)
        print(text)


def hex_operation(integer_list, operator: str, step=0):
    result = hex(eval(f"{integer_list[step]} {operator} {integer_list[-1]}"))
    if step == 0:
        integer_list.append(result)
    if step == len(integer_list) - 2:
        return integer_list
    integer_list[-1] = result
    return hex_operation(integer_list, operator, step + 1)


def binary_operation(integer_list):
    result = []
    for hex_integer in integer_list:
        binary_string = ""
        hex_integer = hex_integer.lstrip("0x")
        hex_digits = string_split(hex_integer, 1)
        for hex_digit in hex_digits:
            binary_string += HEX_VALUES[int(eval(f"0x{hex_digit}"))]
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
    return hex_string.lstrip("0x").zfill(8).upper()


def binary_formatter(binary_string: str) -> str:
    binary_string = binary_string.lstrip("0b").zfill(32)
    byte_list = string_split(binary_string, 8)
    return "  ".join(byte_list)


def print_results(hex_integers, binary_integers, operator):
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
