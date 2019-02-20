
def clean_text(input_string):
    """Takes a string as an argument and returns it all lower case and with no special characters or punctuation"""
    return (''.join(e for e in input_string if e.isalnum())).casefold()


def palindrome(input_string):
    """Takes a string as an argument, cleans it of punctuation, spaces, and special characters, and returns True if it is a palindrome and False otherwise."""
    cleaned_input_string = clean_text(input_string)
    return cleaned_input_string == cleaned_input_string[::-1]


def palindrome_recursively(input_string):
    """Takes a string as an argument, cleans it of punctuation, spaces, and special characters, and returns True if it is a palindrome and False otherwise."""
    cleaned_input_string = clean_text(input_string)
    return (len(cleaned_input_string) <= 1) or ((cleaned_input_string.endswith(cleaned_input_string[0])) and palindrome_recursively(cleaned_input_string[1:len(cleaned_input_string)-1]))


user_input = input("Write something to find out if it is a palindrome: ")

if palindrome_recursively(user_input):
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")