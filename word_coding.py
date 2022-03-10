from math import log2


def text_to_list(text_path):
    """(Auxiliary) Transforms a one-word-per-line text file into a Python list"""
    word_list = []
    with open(text_path, 'r') as filehandle:
        for word in filehandle:
            word_list.append(word.rstrip('\n'))
    return word_list


def get_binary_format_string(word_list):
    """(Auxiliary) Gets the binary format that should be used to encode the words in word_list.
    
    The word list to be used as a dictionary for encoding/decoding purposes should always have 2^N 
    elements, since each mnemonic word will be encoded into an N-bit number. After checking for this
    condition, this function returns the format string to be used to convert integers to this form.
    """

    N = log2(len(word_list))
    assert N.is_integer()
    return '0' + str(int(N)) + 'b'


def encode_words(word_list, seed_phrase):
    """Turns a seed phrase into a number, using a given word list for the encoding."""

    #First, turn each seed word into a binary number.
    binary_numbers = []
    format_string = get_binary_format_string(word_list)
    for word in seed_phrase:
        binary_numbers.append(format(word_list.index(word), format_string))

    #Concatenate binary numbers and convert to hexadecimal.
    secret_number = "".join(binary_numbers)
    return secret_number


def decode_words(word_list, secret_number):
    """Turns a secret number into a seed phrase, using a given word list for the decoding."""

    slice_size = int(log2(len(word_list)))
    slices = [str(secret_number)[i : i + slice_size] for i in range(
        0, len(str(secret_number)), slice_size)]
    seed_phrase = [word_list[int(word_index, 2)] for word_index in slices]
    return seed_phrase