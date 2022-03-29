"""!Module implementing the functions that perform Shamir secret sharing on numerical inputs/outputs"""

from math import floor, log2
from random import randint
import galois
import hmac
import os


def get_polynomial_degree(polynomial:str):
    """!Gets degree of a string-form polynomial on GF(2). Monomials must be of the form x^<number>"""
    
    monomials = polynomial.split('+')[0].strip()
    return int(monomials[2:])


def create_digest(randomness:bytes, shared_secret:bytes, digest_length=4):
    """!Digest function according to SLIP39. Digest length set to 4 by default as per SLIP39"""

    return hmac.new(randomness, shared_secret, "sha256").digest()[:digest_length]


def lagrange_interpolation(x:list, y:list, at_points:list, primitive_poly:str):
    """!Performs Lagrange interpolation on a Galois field GF(2^d), where d is the degree of primitive_poly.
    
    Given the data of n (x,y) points on a Galois field GF=GF(2^d), returns the outputs of a polynomial 
    of degree n-1 that passes through all of these points, evaluated at the list of points at_points.
    Notice that GF is not unique, and must be determined by a primitive polynomial of degree d on GF(2),
    which must be specified in the inputs.

    Inputs:
    * x: list of x-values of the points the interpolated polynomial must pass through.
    * y: list of y-values of the points the interpolated polynomial must pass through.
    * at_points: list of inputs at which the interpolated polynomial will be evaluated.
    * primitive_poly: primitive polynomial of degree d used to construct the Galois field, in string form.

    Output: The output of the interpolation at the elements at_points, converted to the integer
    representation of the elements in GF.
    """

    # Construct the Galois field and verify the validity of the parameters.
    # "Verify" is set to False, otherwise galois.GF attempts to verify the primitiveness of the 
    # polynomial, which effectively freezes the script.
    q = 2**get_polynomial_degree(primitive_poly)
    GF = galois.GF(q, irreducible_poly=primitive_poly, primitive_element='x', verify=False)
    assert len(x) == len(y), "Number of x values (" + str(len(x)) + ") and number of y values (" + str(len(y)) + ") do not coincide."
    
    # Perform a Lagrange interpolation routine (vectorized in case of multiple = elements in at_points)
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
    
    # Is results a list of field elements or a single field element?
    if hasattr(results, "__iter__"):
        # Arrays in the galois package have the field elements stored as an array in entry 0.
        results = [int(field_element) for field_element in results[0]]
    else:
        results = int(results)
    return results


def share_generation(secret:int, num_shares:int, threshold:int, primitive_poly:str, digest_length=4):
    """!Turns an element of a Galois Field (in integer representation) into many, via Shamir secret sharing

    This Shamir secret sharing implementation starts with a secret in decimal form, with secret<=q,
    and constructs a random polynomial f(x) of degree t-1 such that evaluation of f(x) at 0 and q-1
    yields the secret to be shared and a digest, respectively. The algorithm returns the outputs of
    the polynomial at the points [1, 2, ..., num_shares]; these are the secret shares.

    Inputs:
    * secret: integer secret that will be encrypted.
    * num_shares: number of shares that will be generated.
    * threshold: minimum number of shares needed to reconstruct the secret.
    * primitive_poly: primitive polynomial used to construct the Galois Field on GF(2), in string form.
    * digest_length: integer denoting the digest length, if the default value of 4 was not used.

    (Default value chosen above follows a BIP-39 seed mnemonic implementation)

    Output: list of integers representing the secret shares.
    """

    # Get the size of the Galois field to be used:
    q = 2**get_polynomial_degree(primitive_poly)

    # Sanity checks between the given parameters.
    assert num_shares>=threshold, 'Threshold cannot be larger than the number of shares!'
    assert q>=secret, 'More words are needed to encode this secret!'

    # Choose a randomness for digest
    randomness_length = int(floor(log2(q)/8)-digest_length)
    randomness = os.urandom(randomness_length)

    # Compute digest with concatenation of randomness and secret as input. 
    # TODO: Consider generalizing the byte length.
    digest = create_digest(randomness, str(secret).encode(), digest_length)

    # Compute the digest share which is concatenation of digest and randomness in bytes
    digest_share_byte = digest + randomness
    digest_share_int = int.from_bytes(digest_share_byte, "big")

    # Adding the x and y coordinates of the secret and its digest to the correponding list. 
    initial_int_index = [q-1, 0]
    initial_int_shares = [digest_share_int, secret]

    # Sampling t-2 random shares in order to compute a random polynomial with degree t-1 on which 
    # secret and its digest exist.
    for i in range (threshold - 2):
        initial_int_index.append(i+1)
        initial_int_shares.append(randint(1, q-1))

    # Secret and digest values are removed from the final list
    final_x = initial_int_index[2:]
    final_y = initial_int_shares[2:]

    # Above we have chosen random t-2 shares from [1,q-1]. Now we compute n-t+2 more evaluations,
    # and add them to the final_y list.
    remaining_int_indices = [*range(threshold - 1, num_shares + 1)]
    final_x += remaining_int_indices
    final_y += lagrange_interpolation(initial_int_index, initial_int_shares, remaining_int_indices, primitive_poly)
    return final_y

def secret_reconstruction(x:list, y:list, primitive_poly:str, digest_length=4):
    """!Reconstruct secret from the shares, and check for consistency with the encoded digest.

    Inputs:
    * x: list with the x-values corresponding to each numerical share.
    * y: list with the numerical share values.
    * primitive_poly: primitive polynomial used to construct the Galois Field on GF(2), in string form.
    * digest_length: integer denoting the digest length, if the default value of 4 was not used.

    Outputs: the reconstruction of the original secret as an integer value.
    """

    q = 2**get_polynomial_degree(primitive_poly)
    reconstructed_secret, reconstructed_digest = lagrange_interpolation(x, y, [0, q-1], primitive_poly)
    digest_byte = reconstructed_digest.to_bytes(int(floor(log2(q)/8)), 'big')
    
    assert digest_byte[:digest_length] == create_digest(digest_byte[digest_length:], str(reconstructed_secret).encode(), digest_length), "Invalid digest of the shared secret."
    return reconstructed_secret