"""!Test main.py, by checking the entire process of share-creating and reconstruction"""

from random import randint
import pytest
from main import create_shares, reconstruct, get_checksum
from modules.word_coding import decode_words, text_to_list

def test_valid_seed():
    """!BIP-39 compliant seeds are tested."""
    for _ in range(3):
        for num_words in range(12, 61, 3):
            seed = construct_BIP39_seed(num_words)
            assert reconstruct_is_successful(10, 6, seed), 'Reconstruction was not successful'


def test_invalid_seed():
    """!A seed which does not satisfy BIP-39 checksum standards is inputted and tested."""

    seed = "abandon ability able about above absent absorb abstract absurd abuse access accident"
    with pytest.raises(AssertionError) as error:
        reconstruct_is_successful(10, 6, seed) # This should throw an exception
    assert error.value.args[0] == "The inputted seed is not BIP-39 compliant. Check for copying mistakes!"


def reconstruct_is_successful(n, t, seed):
    """!Runs create_shares and reconstruct with an inputted seed, number of shares, and threshold. 
    
    Returns true or false depending on whether the reconstructed seed matches the original one.."""

    # Create a parseargs-like object.
    args = ArgsForMain(n, t, seed)

    # Create shares and then reconstruct
    create_shares(args)
    reconstruct(args)
    with open('secret_reconstructed.txt', 'r') as file:
        reconstructed_seed = file.read()

    return reconstructed_seed==seed


def construct_BIP39_seed(num_words):
    """!Constructs a random seedphrase num_words long which is BIP-39 compliant.
    
    Do NOT use this function to create a seedphrase for a real wallet!
    num_words must be a multiple of 3.
    """

    assert num_words % 3 == 0, 'BIP-39 compliant seeds must have a number of words divisible by 3.'

    # Get entropy and checksum length (in bits):
    checksum_length = num_words//3
    entropy_length = checksum_length*32

    # Get random entropy and checksum
    entropy = randint(0, 2**entropy_length - 1)
    checksum = get_checksum(entropy, entropy_length//8, checksum_length)

    # Combine them into a single binary, then return the seedphrase
    secret_binary = format(entropy, 'b').zfill(entropy_length) + checksum
    word_list = text_to_list('wordlist.txt')
    return decode_words(word_list, secret_binary)


class ArgsForMain():
    def __init__(self, n, t, secret, verbose=False):
        self.n = n
        self.threshold = t
        self.secret = secret
        self.verbose = verbose