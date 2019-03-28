from hackattic import *
from hashlib import md5
import hashlib
import binascii
import base64
from os import remove

def main(token):
    # Name of the challenge
    challenge_name = 'collision_course'

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)

    # Unpack the elements
    challenge_string = challenge_dict['include']
    print(f'string: {challenge_string}')

    # Two differnet prefixes that have the same hash to add to the base_string
    # Due to the properties of md5 hash if you add to two strings that hashs to
    # the same value other strings that also hash to the same value the resulting
    # strings also hash to the same value.
    pref1 = 'd131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70'
    pref1_bytes = bytes.fromhex(pref1)
    pref2 = 'd131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70'
    pref2_bytes = bytes.fromhex(pref2) #+ pref1_bytes

    # Write the resuting files composed by the collision prefix and the given string
    with open('file1','wb') as file1:
        file1.write(pref1_bytes)
    with open('file1','a') as file1:
        file1.write(challenge_string)

    with open('file2','wb') as file2:
        file2.write(pref2_bytes)
    with open('file2','a') as file2:
        file2.write(challenge_string)

    # Encode the files in base64 to send to the server
    with open("file1", "rb") as file1:
        encoded_string_1 = base64.b64encode(file1.read())
    with open("file2", "rb") as file2:
        encoded_string_2 = base64.b64encode(file2.read())

    # Remove the files from disk
    remove("file1")
    remove("file2")

    # Dict for the solution
    challenge_solution = {"files": [encoded_string_1.decode('ascii'),
                                    encoded_string_2.decode('ascii')]}

    # Solution POST
    return solution_post(challenge_name, token, challenge_solution)

if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
