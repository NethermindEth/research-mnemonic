from math import log2

def encode_words (word_list, mnemonic_words_list, format_string):
    number_raw = []
    for mnemonic_word in mnemonic_words_list:
        number_raw.append(format(word_list.index(mnemonic_word), format_string))
    print (f'Original binary numbers: {number_raw}')
    number = "".join(number_raw)
    print (f'Obtained binary number from mnemonic: {number}')
    return int(number, 2)

def decode_words (word_list, mnemonic_number, format_string):
    mnemonic_number_binary = format(mnemonic_number, format_string)
    print (f'Mnemonic number in binary {mnemonic_number_binary}')   
    slice_size = int(log2(len(word_list)))
    slices = [str(mnemonic_number_binary)[i : i + slice_size] for i in
              range(0, len(str(mnemonic_number_binary)), slice_size)]
    print (f'Binary slices: {slices}')
    mnemonic = [word_list[int(word_index, 2)] for word_index in
                slices]
    return mnemonic
    
# read word list from the file
word_list = []
with open('wordlist.txt', 'r') as filehandle:
    for word in filehandle:
        word_list.append(word.rstrip('\n'))

word_list_size = len(word_list)
assert log2(len(word_list)).is_integer()

binary_length_word_list = int(log2(len(word_list)))
format_string = '0' + str(binary_length_word_list) + 'b'
print (format_string)

mnemonic_words_list = ['wedding',
                       'web',
                       'trust',
                       'gadget',
                       'forum',
                       'calm',
                       'cannon',
                       'busy']

print (f'Original nemonic: {mnemonic_words_list}')

number = encode_words (word_list, mnemonic_words_list, format_string)
print (f'Obtained mnemonic number {number}')

print (f'Re-created mnemonic {decode_words (word_list, number, format_string)}')
