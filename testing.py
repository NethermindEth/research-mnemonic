from random import randint
from shamir import *
import galois

#------------------------------------------------------------------------------------------------------------------------------------
#Driver Code
#------------------------------------------------------------------------------------------------------------------------------------
#Parameters for testing
num_words = 12
q=2**(11*num_words)
num_shares = 15
threshold = 7
secret = randint(1, q-1)

#Run Shamir's secret sharing and store the shares
share_list = share_generation(secret, num_shares, threshold, num_words)
print('\nThe secret to be shared is:', secret, '\n')
print('The shares are: \n')
for i in range (len(share_list)):
    print('(', i+1, ',', share_list[i], ')')

#here we define an access set which includes the x coordinates of t shares.
GF11 = galois.GF(q)
access = list(range(1,threshold+1))
access_set = GF11(access)
access_share = []
for i in access:
    access_share.append(share_list[i-1])
print('\nThe access set: \n')
for i in access:
    print ('(',i,',', access_share[i-1], ')')
    
#reconstruction
result_prime = lagrange_interpolation(access_set, access_share)
print ('\nThe reconstructed secret is:', int(result_prime))
if int(result_prime) == secret:
    print('Result:', True)
else:
    print('Result:', False)