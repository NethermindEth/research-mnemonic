import galois
from random import randint


def share_generation(secret, num_shares, threshold, num_words=12):
    """Implements Shamir secret sharing.

    This Shamir secret sharing implementation chooses a random polynomial f(x) of degree t-1
    such that the constant term is the secret to be shared.
    The secret is split into a number of shares, denoted num_shares. 
    Each share is given by (i, f(i)) for 1<=i<=num_shares, and returned as a list.

    Keyword arguments:
    * secret -- secret that will be encrypted.
    * num_shares -- number of shares that will be generated.
    * threshold -- minimum number of shares needed to reconstruct the secret.
    * num_words -- number of words that will be used in the mnemonic encoding the secret. 
    (Default value chosen above follows a BIP-39 seed mnemonic implementation)
    """

    #Sanity checks between the given parameters.
    assert num_shares>=threshold, 'Threshold cannot be larger than the number of shares!'
    assert 2**(11*num_words)>=secret, 'More words are needed to encode this secret!'

    q=2**(11*num_words)
    GF11 = galois.GF(q)
    coeff =[]
    for _ in range(threshold): 
        coeff.append(randint(0,q))
        
    coeff[threshold-1] = secret
    coefficient = GF11(coeff)

    poly = galois.Poly(coefficient, field = GF11)
    eval_point = GF11(list(range(1, num_shares + 1)))
    return poly(eval_point)


def lagrange_interpolation(x=[], y=[], q=2**(11*12)):
    """Implementation of Lagrange interpolation, used to reconstruct the secret from the shares."""

    GF11 = galois.GF(q)
    if len(x) == len(y):
        result = GF11.Zeros(1)
        for i in range(len(x)):
            LagrangeCoefficient = GF11([1])
            for j in range(len(x)):
                if i != j:
                    LagrangeCoefficient = LagrangeCoefficient * (x[j] / (x[j] - x[i]))
            result  = result + LagrangeCoefficient * y[i]  
    return result