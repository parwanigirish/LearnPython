def is_palindrome(word):
    word = word.lower().replace(" ", "")
    reversed_word = word[::-1]
    return word == reversed_word

def check_palindrome():
    user_input = input("Enter a word or phrase: ")
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")

check_palindrome()