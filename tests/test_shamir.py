from random import randint, sample

from scipy import rand
from shamir import *
import galois


def test_shamir():
    #Parameters for testing
    q=2**(11*12)
    shared_secret = randint(1,q-1)
    num_shares = randint(5,15)
    threshold = randint(3, num_shares)
    randomness_length = 12
    digest_length = 4

    #Let us test 5 times.
    for _ in range(5):
        #Run Shamir's secret sharing and store the shares
        shares = share_generation(shared_secret, num_shares, threshold, q, randomness_length, digest_length)
        pick_indices = sample(list(range(1,num_shares)), threshold)
        shares_picked = [shares[index-1] for index in pick_indices]
        reconstructed_secret = secret_reconstruction(pick_indices, shares_picked, q)

        assert reconstructed_secret == shared_secret, 'A reconstructed secret does not match the original'