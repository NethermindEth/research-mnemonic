from math import floor, log2
from random import randint
import galois
import hmac
import os


def get_polynomial_degree(polynomial:str):
    return galois.Poly.String(polynomial).degree

def create_digest(randomness:bytes, shared_secret:bytes, digest_length=4):
    """Digest function according to SLIP39. Digest length set to 4 as per SLIP39"""

    return hmac.new(randomness, shared_secret, "sha256").digest()[:digest_length]
    #TODO: discuss the digest_length and the hash function.


def lagrange_interpolation(x:list, y:list, at_points:list, q:int, primitive_poly:str):
    """Implementation of Lagrange interpolation at a certain integer point."""

    # Construct the Galois field to do the reconstruction arithmetic.
    # To this end, a *primitive* polynomial on GF(2) of degree d such that q = 2^d will be needed.
    # Since this polynomial is primitive, we can assert x is a primitive element.
    # "Verify" is set to False, otherwise galois.GF attempts to verify the primitiveness of the
    # polynomial, which effectively freezes the script.
    GF = galois.GF(q, irreducible_poly=primitive_poly, primitive_element='x', verify=False)
    assert 2**get_polynomial_degree(primitive_poly) == q, 'Primitive polynomial does not have the correct degree. q=2^degree should hold'
    assert len(x) == len(y), "Number of x values (" + str(len(x)) + ") and number of y values (" + str(len(y)) + ") do not coincide."
    
    results = GF.Zeros(1)
    for i in range(len(x)):  
        numerators = GF([1])
        denominator = GF([1])
        for j in range(len(x)):
            if i != j:
                numerators = numerators * (GF([at_points]) - GF([x[j]]))
                denominator = denominator * (GF([x[i]]) - GF([x[j]]))
        lagrange_coefficients = numerators/denominator
        results  = results + lagrange_coefficients * GF([y[i]])
    return [int(field_element) for field_element in results[0]]


def share_generation(secret:list, num_shares:int, threshold:int, q:int, primitive_poly:str, digest_length=4):
    """Implements Shamir secret sharing.

    This Shamir secret sharing implementation constructs a random polynomial f(x) of degree t-1
    such that evaluation of f(x) at q-1 and q-2 yields the secret to be shared and its digest, respectively.

    Keyword arguments:
    * secret -- secret that will be encrypted.
    * num_shares -- number of shares that will be generated.
    * threshold -- minimum number of shares needed to reconstruct the secret.
    * q -- order of the finite field to be used for the polynomial's coefficients.
    (Default value chosen above follows a BIP-39 seed mnemonic implementation)
    """

    #Sanity checks between the given parameters.
    assert num_shares>=threshold, 'Threshold cannot be larger than the number of shares!'
    assert q>=int(secret), 'More words are needed to encode this secret!'

    #Choose a randomness for digest
    randomness_length = int(floor(log2(q)/8)-digest_length)
    randomness = os.urandom(randomness_length)

    #Compute digest with concatenation of randomness and secret as input. 
    #TODO: Consider generalizing the byte length.
    digest = create_digest(randomness, str(secret).encode(), digest_length)

    #Compute the digest share which is concatenation of digest and randomness in bytes
    digest_share_byte = digest + randomness
    digest_share_int = int.from_bytes(digest_share_byte, "big")

    #Adding the x and y coordinates of the secret and its digest to the correponding list. 
    initial_int_index = [q-1, 0]
    initial_int_shares = [digest_share_int, secret]

    #Sampling t-2 random shares in order to compute a random polynomial with degree t-1 on which secret and its digest exist.
    for i in range (threshold - 2):
        initial_int_index.append(i+1)
        initial_int_shares.append(randint(1, q-1))

    #Secret and digest values are removed from the final list
    final_x = initial_int_index[2:]
    final_y = initial_int_shares[2:]

    #Above we have chosen random t-2 shares from [1,q-1]. Now we compute n-t+2 more evaluations, and add them to the final_y list. 
    remaining_int_indices = [*range(threshold - 1, num_shares + 1)]
    final_x += remaining_int_indices
    final_y += lagrange_interpolation(initial_int_index, initial_int_shares, remaining_int_indices, q, primitive_poly)
    
    return final_y

def secret_reconstruction(x:list, y:list, q:int, primitive_poly:str, digest_length=4):
    """Reconstruct secret and digest, check whether they are consistent or not."""

    reconstructed_secret, reconstructed_digest = lagrange_interpolation(x, y, [0, q-1], q, primitive_poly)
    digest_byte = reconstructed_digest.to_bytes(int(floor(log2(q)/8)), 'big')
    
    assert digest_byte[:digest_length] == create_digest(digest_byte[digest_length:], str(reconstructed_secret).encode(), digest_length), "Invalid digest of the shared secret."
    return reconstructed_secret