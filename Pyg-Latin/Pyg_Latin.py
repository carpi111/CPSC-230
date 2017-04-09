# Pig latin translator
# Original was about 150 lines and didn't even work

def pig_latin(english_word):
    """Translates english_word to pig latin"""
    # if word starts with vowel, just add 'way' to end
    if english_word[0] == 'a' or english_word[0] == 'e' or english_word[0] == 'i' or english_word[0] == 'o' or \
            english_word[0] == 'u':
        return english_word + '-way'

    # if second letter is 'y'
    elif english_word[1] == 'y':
        return english_word[1:] + '-' + english_word[0] + 'ay'

    # if first two letters of word are consonants, move first two letters to back
    elif english_word[1] != 'a' and english_word[1] != 'e' and english_word[1] != 'i' and english_word[1] != 'o' and \
            english_word[1] != 'u':
        return english_word[2:] + '-' + english_word[0:2] + 'ay'

    else:
        return english_word[1:] + '-' + english_word[0] + 'ay'

def has_numbers(word_param):
    """Tests the word_param for numbers within inputted word"""
    return any(char.isdigit() for char in word_param)

translated = []

print ('Welcome to the Pyg Latin Translator.\n')

sentence = raw_input('Enter a word or sentence.\n\n')

# checks word for numbers
has_numbers(sentence)

# tests for eligibility of word
while has_numbers(sentence) is True or len(sentence) == 0:
    # if user doesn't type anything
    if len(sentence) == 0:
        sentence = raw_input('\nHow bout actually typing something... Try again. ')
        continue
    # if user inputs word with numbers
    if has_numbers(sentence) is True:
        sentence = raw_input('\nDon\'t use numbers, or special characters. Try again. ')

sentence = sentence.lower()

if ' ' in sentence:
    sentence = sentence.split()
    index = 0
    while index < len(sentence):
        for word in sentence:
            translated.append(pig_latin(sentence[index]))
            index += 1
    print ('')
    print (" ".join(translated))

else:
    print ('')
    print (pig_latin(sentence))
