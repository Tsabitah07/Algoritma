VOWELS = "aeiouAEIOU"

paragraph = [
    "Twinkle, twinkle, little star,", #7
    "How I wonder what you are!", #9
    "Up above the world so high,", #8
    "Like a diamond in the sky." #8
]

# total_vowel_count = 0
#
# for line in paragraph:
#     for vowel in line:
#         if vowel in VOWELS:
#             total_vowel_count += 1
#
# print(f"Total vowels: {total_vowel_count}")
#

def vowel_counter(Text, Vowels):
    vowel_count = 0
    for line in Text:
        for vowel in line:
            if vowel in Vowels:
                vowel_count += 1

    return vowel_count

total_vowel_in_text = vowel_counter(paragraph, VOWELS)

print(f'The grand total of all vowels found is: {total_vowel_in_text}')