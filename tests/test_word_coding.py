from random import randint, sample
from modules.word_coding import *


def test_word_coding():
    word_list = text_to_list('wordlist.txt')

    for _ in range(10):
        seed_phrase_length = randint(1,20)
        seed_phrase = sample(word_list, seed_phrase_length)

        number = encode_words(word_list, seed_phrase)
        reconstructed_seed = decode_words(word_list, number)

        assert reconstructed_seed==seed_phrase, 'Reconstructed secret does not match'