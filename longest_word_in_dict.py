import sys
def find_longest_word_in_string(letters, words):
    letter_positions = dict()
    for index, letter in enumerate(letters):
        letter_positions.setdefault(letter, []).append(index)         
    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break
            possible_positions = [p for p in letter_positions[letter] if p >= pos]
            if not possible_positions:
                break
            pos = possible_positions[0] + 1
        else:
            return word

D = {"able", "ale", "apple", "bale", "kangaroo"}
S = "abpppleekangaroo"

output = find_longest_word_in_string(S, D)
print(output)
