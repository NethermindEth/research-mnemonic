from word_coding import *

###TODO: if necessary, change print statements into logging statements.


def test_word_coding():
    word_list = text_to_list('wordlist.txt')

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

    #print(f'Original mnemonic: {seed_phrase}')
    number = encode_words(word_list, seed_phrase)
    #print (f'Obtained secret number {number}')
    reconstructed_seed = decode_words(word_list, number)
    #print (f'Re-created mnemonic {reconstructed_seed}')

    assert reconstructed_seed==seed_phrase, 'Reconstructed secret does not match'


    