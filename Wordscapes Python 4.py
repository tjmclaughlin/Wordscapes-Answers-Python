#Wordscapes game by Thomas McLaughlin
#Version 1.0
#Started May 22 2020

#importing words from nltk corpus
from nltk.corpus import words
word_list = words.words()

#only accept words with duplicate characters if inputs have duplicate characters
def duplicates_test(word):
    status = True
    for char in word:
        if word.count(char) > 1:
            if characters.count(char) == 1:
                return False
                break
    return status

#take characters as input, store in list
input1 = input("Character 1: ")
input2 = input("Character 2: ")
input3 = input("Character 3: ")
input4 = input("Character 4: ")
input5 = input("Character 5: ")
input6 = input("Character 6: ")
characters = [input1, input2, input3, input4, input5, input6]
print(characters)

#create list for length grouping
chars_3 = []
chars_4 = []
chars_5 = []
chars_6 = []

#inform user of inputs
print("Words containing " + input1 + ", " + input2 + ", "  + input3 + ", "  + input4 + ", "  + input5 + " and " + input6 + ": ")

for word in word_list:
    word = word.lower()
    if duplicates_test(word) == True: #check if amound of duplicate characters in word matches duplicate characters in input
        if len(word) == 3:
            if word[0] in characters and word[1] in characters and word[2] in characters:
                if word not in chars_3: #eliminate duplicate word outputs
                    chars_3 += [word]
        elif len(word) == 4:
            if word[0] in characters and word[1] in characters and word[2] in characters and word[3] in characters:
                if word not in chars_4:
                    chars_4 += [word]
        elif len(word) == 5:
            if word[0] in characters and word[1] in characters and word[2] in characters and word[3] in characters and word[4] in characters:
                if word not in chars_5:
                    chars_5 += [word]
        elif len(word) == 6:
            if word[0] in characters and word[1] in characters and word[2] in characters and word[3] in characters and word[4] in characters and word[5] in characters:
                if word not in chars_6:
                    chars_6 += [word]

#print list of resulting word possibilities
print("\nWords with length 3:")
for word in range(len(chars_3)):
    print(chars_3[word])

print("\nWords with length 4:")
for word in range(len(chars_4)):
    print(chars_4[word])

print("\nWords with length 5:")
for word in range(len(chars_5)):
    print(chars_5[word])

print("\nWords with length 6:")
for word in range(len(chars_6)):
    print(chars_6[word])



