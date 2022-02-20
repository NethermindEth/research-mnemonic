from random import randint
import galois

#parameters
q = 2**132
N = 12
GF11 = galois.GF(q)

#The Dealer determines the n (number of shares) and t (threshold value)
#The Dealer chooses a random polynomial f(x) of degree t-1 such that constant term is the secret to be shared.
#The Dealer computes the share for the i-th user which is (i, f(i))
def share_generation(num_share, threshold, secret):  
    coeff =[]
    for i in range(threshold): 
        coeff.append(randint(0,q))
    
    coeff[threshold-1] = secret
    coefficient = GF11(coeff)

    poly = galois.Poly(coefficient, field = GF11)
    #print('\n', poly, '\n')
    eval_point = GF11(list(range(1, num_share + 1)))
    return poly(eval_point)

#Reconstruction (Lagrange Interpolation)
def Lagrange_Interpolation(x=[], y=[]):
    if len(x) == len(y):
        result = GF11.Zeros(1)
        for i in range(len(x)):
            LagrangeCoefficient = GF11([1])
            for j in range(len(x)):
                if i != j:
                    LagrangeCoefficient = LagrangeCoefficient * (x[j] / (x[j] - x[i]))
            result  = result + LagrangeCoefficient * y[i]  
    return result

#------------------------------------------------------------------------------------------------------------------------------------
#Driver Code
#------------------------------------------------------------------------------------------------------------------------------------
#This secret is for testing. Normally it will be taken from the words.txt file
Secret = randint(1, q-1)
# n: number of shareholders and t: threshold
n = 15
t = 7

#sharing
share_list = share_generation(n, t, Secret)

print('\nThe secret to be shared is:', Secret, '\n')
print('The shares are: \n')

for i in range (len(share_list)):
    print('(', i+1, ',', share_list[i], ')')

#here we define an access set which includes the x coordinates of t shares.
access = list(range(1,t+1))
access_set = GF11(access)
access_share = []
for i in access:
    access_share.append(share_list[i-1])
print('\nThe access set: \n')
for i in access:
    print ('(',i,',', access_share[i-1], ')')
    
#reconstruction
result_prime = Lagrange_Interpolation(access_set, access_share)
print ('\nThe reconstructed secret is:', int(result_prime))
if int(result_prime) == Secret:
    print('Result:', True)
else:
    print('Result:', False)