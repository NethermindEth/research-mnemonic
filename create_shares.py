from modules.get_primitive_poly import get_primitive_poly
from modules import shamir, word_coding
import argparse
import glob
import json
import re
import os

#Empty shares folder to avoid errors
files = glob.glob('shares/*')
for f in files:
    os.remove(f)

#Parser is used in taking the number of shares(-n) and threshold (-t) from terminal.
#Can also provide secret phrase directly into the terminal, as a space-separated phrase.
parser = argparse.ArgumentParser()
parser.add_argument('-n', metavar="", type=int, help='number of shares to generate', required=True)
parser.add_argument('-t', '--threshold', metavar="", type=int, help='number of shares needed to reconstruct the secret', required=True)
parser.add_argument('-s', '--secret', metavar="", type=str, help='secret to share. Input a string with the secret words separated by spaces, OR a path to a .txt file')
parser.add_argument('-v', '--verbose', action='store_true', help='use to include public reconstruction data in the JSON shares')

args = parser.parse_args()
n = args.n
t = args.threshold
assert n >= t, 'Number of shares(-n) cannot be lower than threshold(-t)!'
secret = args.secret
verbose = args.verbose

#Read dictionary, which should have 2^(nb) words for some integer nb.
word_list = word_coding.text_to_list('wordlist.txt')
nb = word_coding.get_dictionary_bits(word_list)

# Obtain the secret. Begin considering the possibility that it will be loaded from a .txt file.
if secret != None:
    regex = r"^[A-Za-z]:(\\|\/).*\.[tT][xX][tT]"
    file_path_found = re.search(regex, secret.strip())
    file_path = file_path_found.group(0) if file_path_found else None
else:
    #If no secret was provided, we will be loading secret.txt by default.
    file_path = 'secret.txt'

# If a file path was assigned above, load it.
if file_path != None:
    # It is assumed that the text file will contain a single row of words, separated by a space.
    with open(file_path, 'r') as file:
        secret = file.read()

#If no file path was assigned above, then -s is the secret phrase! 
secret = secret.strip().split(' ')
#Secret should have between 3 and 60 words, and all words in the secret should be in the dictionary.
assert len(secret) in range(3,61), "Secret has " + str(len(secret)) + " words, but it must have between 3 and 60 words"
assert set(secret).issubset(set(word_list)), "Not every word in the secret is contained in the dictionary"

#Compute Galois-field parameters, using the number of words of the secret.
#Get the primitive polynomial from the provided JSON.
nw = len(secret)
assert nw <= 60, "Secret can only have up to 60 words."
q = 2**(nb*nw)
primitive_poly = get_primitive_poly(nb*nw)
print('primitive_poly: ', primitive_poly)

#Convert secret to numerical form, so that shares can be generated.
binary_secret = word_coding.encode_words(word_list, secret)
decimal_secret = int(binary_secret,2)
shares = shamir.share_generation(decimal_secret, n, t, q, primitive_poly)

#Output public reconstruction data, which will be added to each share if --verbose is true:
reconstruction_data = {
    'total_shares' : n,
    'threshold' : t,
    'primitive_poly' : primitive_poly,
    'dictionary' : ' '.join(word_list)
    }
with open('shares/reconstruction_data.json', 'w') as file:
    json.dump(reconstruction_data, file, indent=4)

#For each share, output a JSON file including id and secret share (word-encoded).
for i in range (len(shares)):
    reconstructed_shared_secrets = word_coding.decode_words(word_list, format(shares[i], "b").zfill(nb*nw))
    print('id: ', i+1)
    print('share: ',reconstructed_shared_secrets)

    file_name = "shares/share_" + str(i+1) + ".json"
    share_data = {
            'id': i+1,
            'share' : reconstructed_shared_secrets,
            }
    if verbose:
        share_data.update(reconstruction_data)

    with open(file_name, 'w') as file:
        json.dump(share_data, file, indent=4)
