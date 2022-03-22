"""Module """
from math import log2


def text_to_list(text_path):
    """Transforms a one-word-per-line text file into a Python list"""
    word_list = []
    with open(text_path, 'r') as filehandle:
        for word in filehandle:
            word_list.append(word.rstrip('\n'))
    return word_list


def get_dictionary_bits(word_list):
    """Gets the number of bits a given wordlist dictionary represents.
    
    The word list to be used as a dictionary for encoding/decoding purposes should always have 2^N 
    elements, since each mnemonic word will be encoded into an N-bit number. After checking for this
    condition, the number N=number_of_bits is returned as an integer.
    """

    number_of_bits = log2(len(word_list))
    assert number_of_bits.is_integer(), 'Number of words in dictionary should be a power of 2.'
    return int(number_of_bits)


def encode_words(word_list, seed_phrase):
    """Turns a seed phrase into a binary number, using a given word list for the encoding."""

    # First, turn each seed word into a binary number.
    binary_numbers = []
    format_string = '0' + str(get_dictionary_bits(word_list)) + 'b'
    for word in seed_phrase:
        binary_numbers.append(format(word_list.index(word), format_string))

    # Concatenate binary numbers and convert to hexadecimal.
    secret_number = "".join(binary_numbers)
    return secret_number


def decode_words(word_list, secret_number):
    """Turns a secret binary number into a seed phrase, using a given word list for the decoding."""

    slice_size = get_dictionary_bits(word_list)
    slices = [str(secret_number)[i : i + slice_size] for i in range(
        0, len(str(secret_number)), slice_size)]
    seed_phrase = [word_list[int(word_index, 2)] for word_index in slices]
    return seed_phrase