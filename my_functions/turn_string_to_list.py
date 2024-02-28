import re


# # This is the function to convert a string of many words in a list.
def turn_string_to_list(input_string):
    output_list = ""
    try:
        output_list = re.split(';|,| |:|\\.|-', input_string)
    except ValueError:
        print(f"Your input '{output_list}' does look like valid. Let's try again...")
    return output_list


if __name__ == "__main__":
    print(turn_string_to_list("to test"))
