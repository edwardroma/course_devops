# This is the function to make sure that the input is an integer.


def get_integer_input(to_do):
    while True:
        input_string = ""
        try:
            input_string = int(input(f"Please give an integer {to_do}: "))
            break
        except ValueError:
            print(f"Your input '{input_string}' does look like an integer. Let's try again...")
    return input_string


if __name__ == "__main__":
    print(get_integer_input("to test 'get_integer'"))
