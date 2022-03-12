from modules import shamir, word_coding
import argparse
import json


#Parser is used in taking the number of shares(-n) and threshold (-t) from terminal.
#Can also provide secret phrase directly into the terminal, as a space-separated phrase.
parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, help='number of shares to generate', required=True)
parser.add_argument('-t', type=int, help='threshold: number of shares to reconstruct the secret', required=True)
parser.add_argument('-w', type=str, help='words to be shared as secret', required=False)
args = parser.parse_args()
assert args.n >= args.t, 'Number of shares(-n) cannot be lower than threshold(-t)!'
n = args.n 
t = args.t
secret = args.w

#Read dictionary, which should have 2^(nb) words for some integer nb.
word_list = word_coding.text_to_list('wordlist.txt')
nb = word_coding.get_dictionary_bits(word_list)

#If no secret was provided in the terminal, read secret from text file 'secret.txt'. It is assumed 
# that the text file will contain a single row of words, separated by a space.
if secret == None:
    with open('secret.txt', 'r') as file:
        secret = file.read()

#All words in the secret should be in the dictionary.
secret = secret.strip().split(' ')
assert set(secret).issubset(set(word_list)), "Not every word in the secret is contained in the dictionary"

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
