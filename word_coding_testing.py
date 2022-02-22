from word_coding import *

word_list = text_to_list('wordlist.txt')
format_string = get_binary_format_string(word_list)

seed_phrase = [
    'wedding',
    'web',
    'trust',
    'gadget',
    'forum',
    'calm',
    'cannon',
    'busy'
    ]

print(f'Original mnemonic: {seed_phrase}')
number = encode_words(word_list, seed_phrase)
print (f'Obtained secret number {number}')
print (f'Re-created mnemonic {decode_words (word_list, number)}')