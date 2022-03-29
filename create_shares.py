"""!Take a secret phrase and apply Shamir Secret Sharing to encode it into n secret phrases.

Using Shamir Secret Sharing, a secret phrase with "nw" words can be encoded into n secret phrases,
each with "nw" words as well. Before encoding, a threshold parameter t (with t<=n) is defined, so 
that only t shares are required for the reconstruction of the original secret. (To reconstruct the
secret, use the script reconstruct.py provided in this package.)


Requisites
----------
1) Before running this script, a dictionary of words to encode secret phrases, with the name
"wordlist.txt", must be provided in the same folder as the script. This dictionary must:
    * Have 2^nb words, where nb is an integer (so that each word represents an nb-bit number)
    * Be a .txt file where each line has a single word.

This package comes pre-loaded with BIP-39's 2048-word dictionary.

2) The secret phrase to be shared should:
    * Have between 3 and 60 words.
    * Have only words that are contained in the dictionary "wordlist.txt".
    * Be written in a single line, with each word separated by only a space.

By default, the secret that will be encoded is read from a .txt file called "secret.txt", to be
located in the same folder as this script. (The secret may also be provided right in the command line
at execution--see below).


Execution and inputs
--------------------
This script should be called from the command line, with the following mandatory inputs (flags):

-n: (integer) Number of shares that will be generated from the secret phrase.
-t, --threshold: (integer) Minimum number of shares that will be required at reconstruction.

The following flags are optional:

-s, --secret: (string) Allows for either of the following options:
    * Specify the secret phrase directly on the command line.
    * Specify a custom file path to a .txt file with the secret.
    (In either case, the secret must abide by the same format considerations stated above)
-v, --verbose: If this flag is used, the generated shares are verbose (see "outputs" below.)


Outputs
-------
During execution, the /shares folder is emptied, and its contents are replaced with the following 
JSON files:

* reconstruction_data.json: Contains the following entries:
    - total_shares: Number of shares n generated during encoding
    - threshold: Threshold t representing the minimum number of shares needed for reconstruction.
    - primitive_poly: Primitive polynomial used to generate the Galois field used for encryption;
      necessary for decryption. For more details, please read modules/shamir.py
    - dictionary: A copy of the contents of the dictionary wordlist.txt

* share_i.json (for 1<=i<=n): Contains the following entries:
    - id: ID number i, with 1<=i<=n, identifying the share.
    - share: list of words, one of the n secret phrases that the original secret was encoded into.
    Remark: if the --verbose flag was used at runtime, each of the JSON shares will also contain the
    reconstruction data.

The shares are also printed on the command line.
"""

from modules.get_primitive_poly import get_primitive_poly
from modules import shamir, word_coding
import argparse
import glob
import json
import re
import os


# Empty the contents of shares folder, create it if it doesn't exist.
if os.path.exists('shares'):
    files = glob.glob('shares/*')
    for f in files:
        os.remove(f)
else:
    os.mkdir('shares')

# Parser initialized to take command line arguments
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


# Obtain the secret, which will either be loaded from a .txt or directly from the command line.
# Case 1: will the secret be loaded from a .txt file?
if secret != None:
    regex = r"^(?:[A-Za-z]:)?(\\|\/).*"
    file_path_found = re.search(regex, secret.strip())
    if file_path_found:
        file_path = file_path_found.group(0)
        print("Loading secret file from path: " + file_path)
    else:
        file_path = None
        print("Loading secret phrase from command line")
else:
    #If no secret was provided, we will be loading secret.txt by default.
    file_path = 'secret.txt'
    print("Loading secret from 'secret.txt' in the script's directory")


# If a file path was assigned above, load it.
if file_path != None:
    try:
        with open(file_path, 'r') as file:
            secret = file.read()
    except FileNotFoundError:
        raise RuntimeError("No secret.txt file provided in the script's folder, or file not found at the custom specified location.")
# Case 2: if no file path was assigned above, then -s is the secret phrase! 


# Secret should have between 3 and 60 words, and all words in the secret should be in the dictionary.
secret = secret.strip().split(' ')
nw = len(secret)
assert nw in range(3,61), "Secret has " + str(nw) + " words, but it must have between 3 and 60 words"
assert set(secret).issubset(set(word_list)), "Not every word in the secret is contained in the dictionary"


# Convert secret to numerical form with word_coding.py, so that shares can be generated with shamir.py
binary_secret = word_coding.encode_words(word_list, secret)
decimal_secret = int(binary_secret,2)
primitive_poly = get_primitive_poly(nb*nw)
shares = shamir.share_generation(decimal_secret, n, t, primitive_poly)


# Output public reconstruction data.
reconstruction_data = {
    'total_shares' : n,
    'threshold' : t,
    'primitive_poly' : primitive_poly,
    'dictionary' : ' '.join(word_list)
    }
with open('shares/reconstruction_data.json', 'w') as file:
    json.dump(reconstruction_data, file, indent=4)


# For each share, output a JSON file including id and secret share (word-encoded).
for i in range (len(shares)):
    reconstructed_shared_secrets = word_coding.decode_words(word_list, format(shares[i], "b").zfill(nb*nw))
    file_name = "shares/share_" + str(i+1) + ".json"
    share_data = {
            'id': i+1,
            'share' : reconstructed_shared_secrets
            }
    print(share_data)

    # Add public reconstruction data to each share if --verbose was used.
    if verbose:
        share_data.update(reconstruction_data)

    with open(file_name, 'w') as file:
        json.dump(share_data, file, indent=4)