# AUTHOR: Edmond Ghislain Makolle
# Python3 Concept: Occurrence
# GITHUB: https://github.com/Edmond22-prog


while (True):
    word = input("Enter a word : ")

    # Loop to retrieve the words of the word/sentence
    letters_in_word = []
    for letter in word:
        if (letter not in letters_in_word):
            letters_in_word.append(letter.lower())

    # Loop to count occurrences of the letter
    letters_with_occurrence = []
    for letter in letters_in_word:
        occ = 0
        for occurrence in word:
            if (occurrence.lower() == letter):
                occ += 1
        letters_with_occurrence.append((letter, occ))
    
    for occurrence in letters_with_occurrence:
        print(occurrence[0] +" appears "+ str(occurrence[1]) +" time(s)")

    retry = input ("Do you want to continue ? (Y/N): ")
    if (retry in ("y", "Yes", "Y")):
        continue
    else:
        break

    
    
    
    
