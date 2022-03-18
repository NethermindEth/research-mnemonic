from msilib.schema import Error
from modules import shamir, word_coding
import argparse
import glob
import json

def get_polynomial_degree(polynomial):
	monomials = polynomial.split('+')[0].strip()
	return int(monomials[2:])

def get_reconstruction_data(dict):
	return (
		dict['total_shares'],
		dict['threshold'],
		dict['primitive_poly'],
		dict['dictionary'].split(' ')
		)

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='store_true', help='do JSON shares include public reconstruction data?')
args = parser.parse_args()
verbose = args.verbose

#Initialize lists:
x_id = []
y_shares = []

#Search JSON files with names of the form 'share_i.json', where 'i' is an integer.
list_of_share_filenames = glob.glob('shares/share*[0-9].json')

#Extract reconstruction data. It must be provided externally if the shares are not verbose.
#Otherwise, one of the shares is picked.
reconstruction_json_path = list_of_share_filenames[0] if verbose else 'shares/reconstruction_data.json'
with open(reconstruction_json_path, "r") as json_file:
	data = json.load(json_file)
try:
	total_shares, threshold, primitive_poly, word_list = get_reconstruction_data(data)
except KeyError:
	if verbose:
		raise RuntimeError('-v flag was added, but not all the shares are verbose')
	else:
		raise RuntimeError('shares/reconstruction_data.json does not contain all the reconstruction data')
		
dict_bits = word_coding.get_dictionary_bits(word_list)
num_words = get_polynomial_degree(primitive_poly)//dict_bits
q = 2**(dict_bits*num_words)

#Extract ID and mnenmonic share data from each share
for json_filename in list_of_share_filenames: #TODO: does this work for numbers greater than 10?
	with open(json_filename, "r") as json_file:
		json_share = json.load(json_file)

	#Check the consistency of the reconstruction data (if verbose) and number of words.
	if verbose:
		try:
			assert get_reconstruction_data(json_share) == (total_shares, threshold, primitive_poly, word_list), 'Shares have incompatible reconstruction data.'
		except KeyError:
			raise RuntimeError('-v flag was added, but not all the shares are verbose')
			
	assert len(json_share['share']) == num_words, 'A share has a number of words inconsistent with the given polynomial and dictionary'

	x_id.append(json_share['id'])
	binary_share = word_coding.encode_words(word_list, json_share['share'])
	y_shares.append(int(binary_share,2))

#Call the reconstruction routine and save to file
assert threshold <= len(y_shares), 'Not enough shares for secret reconstruction' 
reconstructed_secret = shamir.secret_reconstruction(x_id, y_shares, q, primitive_poly)
seed_phrase = word_coding.decode_words(word_list, format(reconstructed_secret, "b").zfill(dict_bits*num_words))
print(seed_phrase)
with open('secret_reconstructed.txt', 'w') as file:
	file.write(" ".join(seed_phrase))

