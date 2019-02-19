
def palindrome(input_string):
    """Takes a string as an argument, cleans it of punctuation, spaces, and special characters, and returns True if it is a palindrome and False otherwise."""
    cleaned_input_string = (''.join(e for e in input_string if e.isalnum())).casefold()
    input_length = len(cleaned_input_string)
    mid_length = input_length // 2
    i = 0
    is_a_palindrome = True
    while i < mid_length:
        if cleaned_input_string[i] != cleaned_input_string[-1-i]:
            is_a_palindrome = False
            break
        i += 1
    return is_a_palindrome


def palindrome_recursively(input_string):
    """Takes a string as an argument, cleans it of punctuation, spaces, and special characters, and returns True if it is a palindrome and False otherwise."""
    cleaned_input_string = (''.join(e for e in input_string if e.isalnum())).casefold()
    if len(cleaned_input_string) <= 1:
        return True
    else:
        if cleaned_input_string.endswith(cleaned_input_string[0]):
            return palindrome_recursively(cleaned_input_string[1:len(cleaned_input_string)-1])
        else:
            return False


user_input = input("Write something to find out if it is a palindrome: ")

if palindrome(user_input):
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")