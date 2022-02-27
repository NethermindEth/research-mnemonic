from shamir import * 
import galois
import sys
import argparse
import word_coding




def print_wordlist():
	''' print wordlist displays wordlist therefore user can choose words as seed'''

	with open('wordlist.txt', 'r') as file_in:
		content = file_in.readlines()
	li = [x.strip() for x in content]
	return li



def word_Coding(seed_phrase = []):
	'''(Auxiliary) utilize word_coding. Gets seed list and output number''' 


	word_list = word_coding.text_to_list('wordlist.txt')
	#print(f'Original mnemonic: {seed_phrase}')
	number = word_coding.encode_words(word_list, seed_phrase)
	return number



def seed_phrase(x = 12):
	''' Gets number of mnemonics from list and outputs encoded number'''

	seed_phrase = []
	for i in range(x):
		seed_word = input("Enter a seed word of from the list \n")
		while (seed_word not in word_list_arr):
			print("The Word you choose is not in the List! ")
			seed_word = input("Enter another seed word of from the list \n")
		seed_phrase.append(seed_word)
		print ('Your Secret List:' , seed_phrase)
	return word_Coding(seed_phrase)



def output_secret_shares(shares):
	''' displays shares in terminal and outputs to txt files '''

	word_list = word_coding.text_to_list('wordlist.txt')

	#for each shares program outputs a file including id, shared secret(word encoded), degree and irr poly to construct unique GF.
	for i in range (len(shares)):
		reconstructed_shared_secrets = word_coding.decode_words(word_list, shares[i])
		print ('id: ', i+1)
		print ('shares: ',reconstructed_shared_secrets)
		print ('degree: ', init_galois_degree())
		print ('irr_poly: ', init_galois_irr_poly())
		print ('encoded_words:', shares[i],'\n\n\n')
		file_name = "share_" + str(i+1)
		f = open(file_name, "w")
		f.write ('id:' + str(i+1) + "\n")
		f.write ('words:' + str(reconstructed_shared_secrets)+ "\n")
		f.write ('degree:' + str(init_galois_degree())+ "\n")
		f.write ('irr_poly:' + str(init_galois_irr_poly())+ "\n")
		f.close()




# parser is used in taking the number of shares(-ns) and threshold numbers(-nt) from terminal 
parser = argparse.ArgumentParser()
parser.add_argument('-ns', type=int, help='number of secret', required=True)
parser.add_argument('-nt', type=int, help='number of threshold', required=True)

args = parser.parse_args()

if (args.ns < args.nt):
	print('Error: Number of shares(ns) cannot be lower than Number of thresholds(nt)!')
	sys.exit(0)

n = args.ns 
t = args.nt




#constructing Galois fields
nb = 11
nw = 12
q = 2**(nb*nw)




# display wordlist.txt to user can c
word_list_arr = print_wordlist()
print (word_list_arr)




#creating secret from taking words from list that is displayed above
shared_secret = seed_phrase()




#printing secret, number of shares and number of threshold
print('\nShared Secret is: ',shared_secret, '\nNumber of Shares is: ',args.ns, '\nNumber of Thresholds is:', args.nt ,'\n')



#share generation from shamir.py
shares = share_generation(shared_secret, n, t, q)



#calls for outputing secret sharing function
output_secret_shares(shares)








