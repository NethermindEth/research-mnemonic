from shamir import * 
import galois
import word_coding
import glob
import ast 


#initializations lists 


# initializations for ids
x_id = []

# initializations for y_shares
y_shares = []

# initializations degrees_list
degrees_list = []

# initializations irr_poly
irr_poly = []


def word_Decoding(secret_number):
	'''(Auxiliary) utilize word_decoding. Gets secretnumber and output words''' 


	word_list = word_coding.text_to_list('wordlist.txt')
	#print(f'Original mnemonic: {seed_phrase}')
	word_phrase = word_coding.decode_words(word_list, secret_number)
	return word_phrase



def word_Coding(seed_phrase = []):
	'''(Auxiliary) utilize word_coding. Gets seed list and output number''' 


	word_list = word_coding.text_to_list('wordlist.txt')
	#print(f'Original mnemonic: {seed_phrase}')
	number = word_coding.encode_words(word_list, seed_phrase)
	return number


def search_share_files():
	'''Search files that begins with 'share' in same directory 
	when it finds this kind of file, parse it and take id, words, degree and irr_poly''' 


	for i in glob.glob('share*'):
		f = open(i, "r")

		#read the data line by line
		data_in_f = f.readlines()

		# parse the id which is in front
		x_id.append(int(data_in_f[0].split(':')[1].rstrip()))

		#parse the words(shared mnemonics) in second order
		mnemonics_list = ast.literal_eval(data_in_f[1].split(':')[1].rstrip())
		print (mnemonics_list[0])
		print (mnemonics_list[1])
		print (mnemonics_list[2])
		print (mnemonics_list[3])
		print (word_Coding(mnemonics_list))
		y_shares.append(word_Coding(mnemonics_list))

		#parse the degree in third order (default 11x12 = 132) 
		degrees_list.append(int(data_in_f[2].split(':')[1].rstrip()))

		#parse the integer encoded irreducible polynomial
		irr_poly.append(int(data_in_f[3].split(':')[1].rstrip()))

		f.close()


	#display the lists. These can be commented.
	print(x_id)
	print(y_shares)
	print(degrees_list)
	print(irr_poly)




def check_func(x, check_name):
	'''(Auxiliary) Gets a list and arbitrary check_name and validate if there is different element in list. It is used for degree and irr_poly checking phase'''


	save_first = x[0]
	for i in range(len(x)-1):
		if (save_first != x[i+1]):
			print ('Error ! ' , check_name , ' is not same')
			return False
	#print (check_name, ' is checked! ')
	return True



def reconstruction_wrapper():
	'''Reconstruction is done here '''

	# In case of there is a disagreement about degree or irreducible polynomial  
	if ((check_func(degrees_list,'degree list') and check_func(irr_poly,'irr_poly')) == False ):
		print ('One of the secret\'s of degree or irr_poly is different! Please check the shared secrets' )
	else:
		#there is no disagreement degrees_list[i] = degrees_list[j] for all j
		q = 2 ** degrees_list[0]
		GF = galois.GF(q, irreducible_poly = irr_poly[0])
		#print(GF.irreducible_poly.integer)
		reconstructed_number = secret_reconstruction(x_id, y_shares, q)
		print ('reconstructed_number', reconstructed_number)
		reconstructed_words = word_Decoding(reconstructed_number)
		print ('reconstructed_words',reconstructed_words)





# call for function that is searching files in same directory
search_share_files()

# call for function that is re-constructioning.
reconstruction_wrapper()










			
