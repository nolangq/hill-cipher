'''
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Nolan Quinn
| Language: python
| To Execute: python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Summer 2024
| Instructor: McAlpin
| Due Date: 09/15/2024
'''

import sys
import numpy as np
import string

# open files
key = open(sys.argv[1], "r")
plain = open(sys.argv[2], "r", encoding='utf-8', errors='ignore')

# save dimension of key matrix
dimensions = int(key.readline())
# create key matrix
key_matrix = np.loadtxt(key, dtype=int)
# print key matrix
print("\nKey matrix:", end="")

for i in range(0, dimensions):
    for j in range(0, dimensions):
        if (j % dimensions == 0):
            print("")
        print(''.join(f'{key_matrix[i][j]:4d}'), end="")
print("\n")

# create plaintext matrix
plain_matrix = [i for i in plain.read()]
plain_matrix = np.asarray(plain_matrix, dtype=str)
# get rid of \n
plain_matrix = np.delete(plain_matrix, np.where(plain_matrix == '\n'))
# change uppercase to lowercase
for i in range(0, len(plain_matrix)):
    if plain_matrix[i].isupper() == True:
        plain_matrix[i] = plain_matrix[i].lower()
# change letters to ascii digit
plain_matrix = [ord(i) for i in plain_matrix]
# convert numbers to 0-25
for i in range(0, len(plain_matrix)):
    plain_matrix[i] = plain_matrix[i] - 97
# get rid of negative values
plain_matrix = [i for i in plain_matrix if i >= 0 and i < 26]
# add ascii number for 'x' as padding
while len(plain_matrix) % dimensions != 0:
    plain_matrix.append(23)

# print plaintext
print("Plaintext:", end="")
for i in range(0, len(plain_matrix)):
    if i % 80 == 0:
        print("")
    print(chr(plain_matrix[i] + 97), end="")
print("\n")
# reshape matrix
plain_matrix = np.reshape(plain_matrix, (dimensions, -1), order='F')


# multiply plain matrix and key matrix to get cipher matrix
cipher_matrix = np.dot(key_matrix, plain_matrix)

# change cipher matrix back to ascii values
for i in range(0, cipher_matrix.shape[0]):
    for j in range(0, cipher_matrix.shape[1]):
        cipher_matrix[i][j] = cipher_matrix[i][j] % 26
        cipher_matrix[i][j] = cipher_matrix[i][j] + 97

# print encrypted messsage
print("Ciphertext:", end="")
count = 0
for i in range(0, cipher_matrix.shape[1]):
    for j in range(0, cipher_matrix.shape[0]):
        if count % 80 == 0:
            print("")
        count = count + 1
        print(chr(cipher_matrix[j][i]), end="")
print("")

# close files
key.close()
plain.close()

'''
| I Nolan Quinn (5655015) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
'''