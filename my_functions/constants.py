list_digits: list[int | str] = [x for x in range(0, 10)]
list_letters_lowercase: list[int | str] = [chr(x) for x in range(ord('a'), ord('z') + 1)]
list_letters_uppercase: list[int | str] = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
string_specials: str = '][+-=@_!#$%^&*()<>?/\\|}{~:;,.'
list_specials: list[int | str] = [x for x in string_specials]
