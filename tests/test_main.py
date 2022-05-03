"""!Test main.py, by checking the entire process of share-creating and reconstruction"""

import unittest
from main import create_shares, reconstruct

def test_valid_seed():
    """!A BIP-39 compliant seed is tested."""

    seed = "abandon ability able about above absent absorb abstract absurd abuse access ability"
    assert reconstruct_is_successful(10, 6, seed), 'Reconstruction was not successful'


def test_invalid_seed():
    """!A seed which does not satisfy BIP-39 checksum standards is inputted and tested."""

    seed = "abandon ability able about above absent absorb abstract absurd abuse access ability"
    # This should throw an exception
    with self.assertRaises(AssertionError) as error:
        reconstruct_is_successful(10, 6, seed)


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


class ArgsForMain():
    def __init__(self, n, t, secret, verbose=False):
        self.n = n
        self.threshold = t
        self.secret = secret
        self.verbose = verbose