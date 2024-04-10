# Method1 using the slicing technique
def check_palindrome_1(word):
    return 'Pallindrome' if word == word[::-1] else 'Not Pallindrome'

# Method 2 using string reversal
def check_palindrome_2(word):
    rev_str = ''
    for i in range(len(word)-1, -1, -1):
        rev_str += word[i]
    return 'Pallindrome' if word == rev_str else 'Not Pallindrome'

# Using 2 pointers
def check_palindrome_3(word):
    i = 0
    j = len(word) - 1
    while i<j:
        if word[i] != word[j]:
            return 'Not Pallindrome'
        i += 1
        j -= 1
    return 'Pallindrome'

if __name__ == "__main__":
    # Get Input from User
    word = input("Enter a word: ")
    # Call the function and print the result
    print(f"The word {word} is {check_palindrome_2(word)}")