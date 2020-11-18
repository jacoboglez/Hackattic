from hackattic import *
from zipfile import ZipFile
import os


CHALLENGE = "brute_force_zip"
# https://hackattic.com/challenges/brute_force_zip


'''
To bruteforce the .zip file we need to use a known plaintext attack. This attack is implemented in the following library:
https://github.com/kimci86/bkcrack
This package must be uncompressed in the directory ./zip.

The known plaintext file is the book Dunwich Horror, that can be found here:
http://www.gutenberg.org/ebooks/50133
The book in plaintext (dunwich_horror.txt) must be compressed with zip (dunwich_horror.zip) and placed also in the ./zip/ directory.

The program then downloads the protected .zip file, places it in the ./zip/ folder and calls the bkcrack program to obtain the keys, extract the secret file, and uncompress it.

This was designed for a UNIX system. Details of the program used can be found in the github repository.
'''


def main(token):
    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)

    # Get the file URL
    zip_url = challenge_dict['zip_url']
    file_request(zip_url, zip_name = "zip/protected.zip")

    # Get the keys
    os.system('./zip/bkcrack-1.0.0-Linux/bkcrack -C ./zip/protected.zip -c dunwich_horror.txt -P ./zip/dunwich_horror.zip -p dunwich_horror.txt > ./zip/keys.txt')

    # Read the keys
    with open('./zip/keys.txt','r') as file_handler:
        keys = file_handler.readlines()[-1].strip('\n')
    
    # Decypher 
    os.system(f'./zip/bkcrack-1.0.0-Linux/bkcrack -C ./zip/protected.zip -c secret.txt -k {keys} -d ./zip/secret.deflate')

    # Inflate the secret
    os.system(f'python ./zip/bkcrack-1.0.0-Linux/tools/inflate.py < ./zip/secret.deflate > ./zip/secret.txt')

    # Read secret
    with open('./zip/secret.txt','r') as file_handler:
        secret = file_handler.readline().strip('\n')
    
    # Post the solution
    solution_post(CHALLENGE, token, {'secret': secret})


if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
