import p5_module as pm


def main():
    while True:
        operator = pm.get_operation()
        if operator.lower() == "q":
            break

        number_of_integers = pm.get_integer_count()
        hex_inputs = list()
        for number in range(1, number_of_integers + 1):
            while True:
                hex_string = input(f"Enter integer {number}: ")
                if not pm.is_valid_hex_string(hex_string):
                    continue
                break
            hex_inputs.append("0x" + hex_string)

        hex_outputs = pm.hex_operation(hex_inputs, operator)
        binary_outputs = pm.binary_operation(hex_outputs)
        pm.print_results(hex_outputs, binary_outputs, operator)


if __name__ == "__main__":
    main()
