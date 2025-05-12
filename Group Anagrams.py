from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())

# Take user input
input_line = input("Enter words separated by spaces: ")

# Split the input into a list of words
word_list = input_line.strip().split()

# Group anagrams
grouped = group_anagrams(word_list)

# Print the grouped anagrams
print("\nGrouped Anagrams:")
for group in grouped:
    print(group)
