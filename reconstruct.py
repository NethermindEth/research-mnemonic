from modules import shamir, word_coding
import glob
import json


#Initialize lists:
x_id = []
y_shares = []

#Search JSON files with names of the form 'share_i.json', where 'i' is an integer.
#Extract ID and mnenmonic share data.
first_iteration = True
for json_filename in glob.glob('shares/share*[0-9].json'): #TODO: does this work for numbers greater than 10?
	with open(json_filename, "r") as json_file:
		json_share = json.load(json_file)

	#Dictionary and irreducible polynomial should be consistent amongst shares.
	if(first_iteration):
		threshold = json_share['threshold']
		word_list = json_share['dictionary'].split(' ')
		dict_bits = word_coding.get_dictionary_bits(word_list)
		num_words = len(json_share['share'])
		q = 2**(dict_bits*num_words)
		expected_data = [json_share['total_shares'], threshold, json_share['irr_poly'], json_share['dictionary']]
	else:
		assert expected_data == [json_share['total_shares'], json_share['threshold'], json_share['irr_poly'], json_share['dictionary']], 'Shares have incompatible data'
	first_iteration = False

	x_id.append(json_share['id'])
	binary_share = word_coding.encode_words(word_list, json_share['share'])
	y_shares.append(int(binary_share,2))

#Call the reconstruction routine and save to file
assert threshold <= len(y_shares), 'Not enough shares for secret reconstruction' 
reconstructed_secret = shamir.secret_reconstruction(x_id, y_shares, q)
seed_phrase = word_coding.decode_words(word_list, format(reconstructed_secret, "b").zfill(dict_bits*num_words))
print(seed_phrase)
with open('secret_reconstructed.txt', 'w') as file:
	file.write(" ".join(seed_phrase))