"""Test shamir.py, by creating numerical shares out of a random number and reconstructing it"""

from modules.get_primitive_poly import get_primitive_poly
from random import randint, sample
from modules.shamir import *


def test_shamir():
    #Let us test 10 times.
    for _ in range(10):
        #Parameters for testing
        num_words = randint(3,30)
        q=2**(11*num_words)
        primitive_poly = get_primitive_poly(11*num_words)
        shared_secret = randint(1,q-1)
        num_shares = randint(5,15)
        threshold = randint(3, num_shares)

        #Run Shamir's secret sharing and store the shares
        shares = share_generation(shared_secret, num_shares, threshold, primitive_poly)
        pick_indices = sample(list(range(1,num_shares+1)), threshold)
        shares_picked = [shares[index-1] for index in pick_indices]
        reconstructed_secret = secret_reconstruction(pick_indices, shares_picked, primitive_poly)

        assert reconstructed_secret == shared_secret, 'A reconstructed secret does not match the original'