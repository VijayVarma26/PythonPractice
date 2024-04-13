def count_vowels(str):
    vowels = 'aeiou'
    count = 0
    for char in str.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("vijay"))