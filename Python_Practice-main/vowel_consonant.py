# Asks the user to enter a string.
# Counts and prints:
# Number of vowels
# Number of consonants
# Prints the reversed string.
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in word:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
print("Reversed string:", word[::-1])
print("Thanks for using this program!")
