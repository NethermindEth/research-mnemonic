from modules import shamir, word_coding
import argparse
import json


#Parser is used in taking the number of shares(-ns) and threshold numbers(-nt) from terminal. 
parser = argparse.ArgumentParser()
parser.add_argument('-ns', type=int, help='number of shares to generate', required=True)
parser.add_argument('-nt', type=int, help='threshold: number of shares to reconstruct the secret', required=True)
args = parser.parse_args()
assert args.ns >= args.nt, 'Number of shares(ns) cannot be lower than threshold(nt)!'
n = args.ns 
t = args.nt

#Read dictionary, which should have 2^N words for some integer N.
word_list = word_coding.text_to_list('wordlist.txt')
nb = word_coding.get_dictionary_bits(word_list)

#Read secret from text file 'secret.txt'. It is assumed that the text file will contain a single row
#of words, separated by a space. Also, all the words in the secret should be in the dictionary.
with open('secret.txt', 'r') as file:
    secret = file.read().strip().split(' ')
assert set(secret).issubset(set(word_list)), "Not all the words in the secret are contained in the dictionary"

#Constructing Galois fields, using the number of words of the secret.
nw = len(secret)
q = 2**(nb*nw)

#Convert secret to numerical form, so that shares can be generated.
binary_secret = word_coding.encode_words(word_list, secret)
decimal_secret = int(binary_secret,2)
shares = shamir.share_generation(decimal_secret, n, t, q)

#For each share, program outputs a file including id, shared secret(word encoded), degree and irr poly to construct unique GF.
for i in range (len(shares)):
    reconstructed_shared_secrets = word_coding.decode_words(word_list, format(shares[i], "b").zfill(nb*nw))
    print ('id: ', i+1)
    print ('share: ',reconstructed_shared_secrets)
    print ('irr_poly: ', shamir.init_galois_irr_poly())
    print ('encoded_words:', shares[i],'\n\n')

    file_name = "shares/share_" + str(i+1) + ".json"
    with open(file_name, 'w') as file:
        json.dump(
            {
            'id': i+1,
            'total_shares' : n,
            'threshold' : t,
            'share' : reconstructed_shared_secrets,
            'irr_poly' : shamir.init_galois_irr_poly(),
            'dictionary' : ' '.join(word_list)
            },
            file, 
            indent=4
            )