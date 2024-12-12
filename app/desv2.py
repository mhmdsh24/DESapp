# Util
# Hexadecimal to binary conversion
def hex2bin(s):
	mp = {'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'A': "1010",
		'B': "1011",
		'C': "1100",
		'D': "1101",
		'E': "1110",
		'F': "1111"}
	bin = ""
	for i in s.upper():
		bin = bin + mp[i]
	return bin

# Binary to hexadecimal conversion
def bin2hex(s):					#using hex() doesnt preserve leading zeros
	mp = {"0000": '0',
		"0001": '1',
		"0010": '2',
		"0011": '3',
		"0100": '4',
		"0101": '5',
		"0110": '6',
		"0111": '7',
		"1000": '8',
		"1001": '9',
		"1010": 'A',
		"1011": 'B',
		"1100": 'C',
		"1101": 'D',
		"1110": 'E',
		"1111": 'F'}
	hex = ""
	for i in range(0, len(s), 4):
		ch = ""
		ch = ch + s[i]
		ch = ch + s[i + 1]
		ch = ch + s[i + 2]
		ch = ch + s[i + 3]
		hex = hex + mp[ch]

	return hex

# Binary to decimal conversion
def bin2dec(binary):
	decimal, i = 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	return decimal

# Decimal to binary conversion
def dec2bin(num):
	res = bin(num).replace("0b", "")
	if(len(res) % 4 != 0):
		div = len(res) / 4
		div = int(div)
		counter = (4 * (div + 1)) - len(res)
		for i in range(0, counter):
			res = '0' + res
	return res

# Permutation function to rearrange the bits
def permute(k, arr, n):
	permutation = ""
	for i in range(0, n):
		permutation += k[arr[i] - 1]
	return permutation

# Left circular shift
def shift_left(binary: str, shift: int) -> str:
    shift = shift % len(binary)
    return binary[shift:] + binary[0: shift]

# XOR function
def xor(a, b):
	ans = str()
	for i in range(len(a)):
		if a[i] == b[i]:
			ans += "0"
		else:
			ans += "1"
	return ans


# Tables
# Initial Permuation (IP)
IP = [58, 50, 42, 34, 26, 18, 10, 2,
	  60, 52, 44, 36, 28, 20, 12, 4,
	  62, 54, 46, 38, 30, 22, 14, 6,
	  64, 56, 48, 40, 32, 24, 16, 8,
	  57, 49, 41, 33, 25, 17,  9, 1,
	  59, 51, 43, 35, 27, 19, 11, 3,
	  61, 53, 45, 37, 29, 21, 13, 5,
	  63, 55, 47, 39, 31, 23, 15, 7]

# Expansion Permutation (E)
E_table = [32,  1,  2,  3,  4,  5,  4,  5,
		    6,  7,  8,  9,  8,  9, 10, 11,
		   12, 13, 12, 13, 14, 15, 16, 17,
		   16, 17, 18, 19, 20, 21, 20, 21,
	  	   22, 23, 24, 25, 24, 25, 26, 27,
	  	   28, 29, 28, 29, 30, 31, 32,  1]

# Permutation Function (P)
P_table = [16,  7, 20, 21, 29, 12, 28, 17,
	        1, 15, 23, 26,  5, 18, 31, 10,
			2,  8, 24, 14, 32, 27,  3,  9,
		   19, 13, 30,  6, 22, 11,  4, 25]
		   
# S-boxes
sbox = [[[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
		 [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
		 [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
		 [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]],

		[[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
		 [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
		 [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
		 [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]],

		[[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
		 [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
		 [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
		 [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],

		[[ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
		 [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
		 [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
		 [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]],

		[[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
		 [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
		 [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
		 [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]],

		[[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
		 [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
		 [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
		 [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],

		[[ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
		 [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
		 [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
		 [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]],

		[[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
		 [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
		 [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
		 [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]]
    
# Inverse Initial Permutation (IP^-1)
inverse_IP = [40, 8, 48, 16, 56, 24, 64, 32,
			  39, 7, 47, 15, 55, 23, 63, 31,
			  38, 6, 46, 14, 54, 22, 62, 30,
			  37, 5, 45, 13, 53, 21, 61, 29,
			  36, 4, 44, 12, 52, 20, 60, 28,
			  35, 3, 43, 11, 51, 19, 59, 27,
			  34, 2, 42, 10, 50, 18, 58, 26,
			  33, 1, 41,  9, 49, 17, 57, 25]

# Permuted Choice One (PC-1)
PC1 = [57, 49, 41, 33, 25, 17,  9,
		1, 58, 50, 42, 34, 26, 18,
	   10,  2, 59, 51, 43, 35, 27,
	   19, 11,  3, 60, 52, 44, 36,
	   63, 55, 47, 39, 31, 23, 15,
		7, 62, 54, 46, 38, 30, 22,
	   14,  6, 61, 53, 45, 37, 29,
	   21, 13,  5, 28, 20, 12,  4]

# Permuted Choice Two (PC-2)
PC2 = [14, 17, 11, 24,  1,  5,  3, 28,
	   15,  6, 21, 10, 23, 19, 12,  4,
	   26,  8, 16,  7, 27, 20, 13,  2,
	   41, 52, 31, 37, 47, 55, 30, 40, 
	   51, 45, 33, 48, 44, 49, 39, 56, 
	   34, 53, 46, 42, 50, 36, 29, 32]
			
# Schedule of Left Shifts
shift_table = [1, 1, 2, 2, 2, 2, 2, 2,1, 2, 2, 2,2, 2, 2, 1]



def key_gen(key):
    # Step 1: Convert to binary
    key = hex2bin(key)

    # Step 2: Permute the key through the PC-1 table
    PC1key = permute(key, PC1, 56)

    # Splitting
    left = PC1key[0:28]
    right = PC1key[28:56]

    rkb = []  # Round keys in binary
    key_rounds = [{'Round':'0','Key':key,'Key after PC1':PC1key,'L0':left,'R0':right }]  # Store details of each key generation round

    for i in range(16):
        round_details = {"Round": str(i + 1)}  # Store details for the current round

        # Shifting the bits by nth shifts by checking from shift table
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])

        # Combination of left and right string
        combine_str = left + right
        round_details["Left Half"] = left
        round_details["Right Half"] = right

        # Permute the key through the PC-2 table
        round_key = permute(combine_str, PC2, 48)
        round_details["Round Key (Binary)"] = round_key
        round_details["Round Key (Hexadecimal)"] = bin2hex(round_key)

        # Append round key to the list
        rkb.append(round_key)

        # Append the round details to the list
        key_rounds.append(round_details)

    return rkb, key_rounds

def encrypt(message, key):
    message = hex2bin(message)  # Convert message to binary
    rkb,_ = key_gen(key)  # Generate round keys

    # Initial Permutation
    IPmessage = permute(message, IP, 64)

    # Splitting (32 bits each)
    left = IPmessage[0:32]
    right = IPmessage[32:64]
    rounds = [{'Round':'0','Message':message,'Message after IP':IPmessage,'Left':left,'Right':right ,'Result':right}]

    for i in range(0, 16):
        round_details = {"Round": str(i + 1)}
        round_details["Left"] = left
        round_details["Right"] = right
        # Expansion to 48 bits
        right_expanded = permute(right, E_table, 48)
        round_details["Right Expanded"] = right_expanded
        # XOR with round key
        xor_rkb = xor(right_expanded, rkb[i])
        round_details["XOR with Key"] = xor_rkb
        # S-box substitution
        sbox_str = str()
        for j in range(0,8):
            row = bin2dec(int(xor_rkb[j * 6] + xor_rkb[j * 6 + 5]))
            col = bin2dec(int(xor_rkb[j * 6 + 1] + xor_rkb[j * 6 + 2] + xor_rkb[j * 6 + 3] + xor_rkb[j * 6 + 4]))
            val = sbox[j][row][col]
            sbox_str += dec2bin(val)
        round_details["S-box Substitution"] = sbox_str
        # Sbox permutation
        sbox_str = permute(sbox_str, P_table, 32)
        round_details["Permutation"] = sbox_str
        # XOR left with S-box result
        result = xor(left, sbox_str)
        round_details["Result"] = result
        
        left = result
        # Swapping
        if i != 15:
            left, right = right, left
        rounds.append(round_details)

    # Final Combination
    combine = left + right

    # Final Permutation
    cipher_text = permute(combine, inverse_IP, 64)
    cipher_text = bin2hex(cipher_text)
    return cipher_text , rounds

def decrypt(cipher_text, key):
	cipher_text = hex2bin(cipher_text)  # Convert message to binary
	rkb, rk = key_gen(key)  # Generate round keys
	rkb = rkb[::-1]
	rk = rk[::-1]
	# Initial Permutation
	IPcipher_text = permute(cipher_text, IP, 64)

	# Splitting (32 bits each)
	left = IPcipher_text[0:32]
	right = IPcipher_text[32:64]
	rounds = [{'Round':'0','Message':cipher_text,'Message after IP':IPcipher_text,'Left':left,'Right':right ,'Result':right}]

	for i in range(0, 16):
		round_details = {"Round": str(i + 1)}
		round_details["Left"] = left
		round_details["Right"] = right
		# Expansion to 48 bits
		right_expanded = permute(right, E_table, 48)
		round_details["Right Expanded"] = right_expanded
		# XOR with round key
		xor_rkb = xor(right_expanded, rkb[i])
		round_details["XOR with Key"] = xor_rkb
		# S-box substitution
		sbox_str = str()
		for j in range(0,8):
			row = bin2dec(int(xor_rkb[j * 6] + xor_rkb[j * 6 + 5]))
			col = bin2dec(int(xor_rkb[j * 6 + 1] + xor_rkb[j * 6 + 2] + xor_rkb[j * 6 + 3] + xor_rkb[j * 6 + 4]))
			val = sbox[j][row][col]
			sbox_str += dec2bin(val)
		round_details["S-box Substitution"] = sbox_str
		# Sbox permutation
		sbox_str = permute(sbox_str, P_table, 32)
		round_details["Permutation"] = sbox_str
		# XOR left with S-box result
		result = xor(left, sbox_str)
		round_details["Result"] = result

		left = result
		# Swapping
		if i != 15:
			left, right = right, left
		rounds.append(round_details)

    # Final Combination
	combine = left + right

    # Final Permutation
	message = permute(combine, inverse_IP, 64)
	message = bin2hex(message)
	return message , rounds

def sentence_to_hex(sentence):
    """Convert a sentence into a hexadecimal string using UTF-8 encoding."""
    return sentence.encode('utf-8').hex()

def hex2sentence(hex_string):
    bytes_object = bytes.fromhex(hex_string)
    return bytes_object.decode('utf-8', errors='ignore')

def pad_hex_blocks(hex_string, block_size=16):
    """Pad the hexadecimal string to ensure it is a multiple of the block size."""
    padding_length = block_size - (len(hex_string) % block_size)
    if padding_length != block_size:
        hex_string += '0' * padding_length
    return hex_string

def encrypt_sentence(sentence, key):
    """Encrypt a sentence using DES."""
    # Step 1: Convert the sentence to hex
    hex_sentence = sentence_to_hex(sentence)
    # Step 2: Pad the hex string to ensure it fits into 16-character blocks
    padded_hex = pad_hex_blocks(hex_sentence)
    # Step 3: Divide the hex string into 16-character blocks
    blocks = [padded_hex[i:i+16] for i in range(0, len(padded_hex), 16)]
    # Step 4: Encrypt each block
    ciphertext = ""
    for block in blocks:
        encrypted_block, _ = encrypt(block, key)
        ciphertext += encrypted_block
    
    return ciphertext, blocks

def decrypt_sentence(ciphertext, key):
    """Decrypt a ciphertext using DES."""
    blocks = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)]
    plaintext = ""
    for block in blocks:
        decrypted_block, _ = decrypt(block, key)
        plaintext += decrypted_block
    plaintext = hex2sentence(plaintext)
    return plaintext,blocks

# Example usage:
# key = "1111111111111111"  # 16-character hex key
# sentence = "hello my name is mhmd"
# ciphertext = encrypt_sentence(sentence, key)
# print(f"Ciphertext: {ciphertext}")

# pt = "48454c4c4f204445"

# print("Encryption")
# cipher_text,_ = encrypt(pt,key)
# print(cipher_text)
# # print(key_gen(key))
# print("Decryption")
# cipher_text = decrypt(pt,key)
# print(cipher_text)

