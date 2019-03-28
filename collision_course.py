from hackattic import *
from hashlib import md5
import hashlib
import binascii

def main(token):
    # Name of the challenge
    # challenge_name = 'collision_course'
    #
    # # Data of the challenge to a dict
    # challenge_dict = data_request(challenge_name, token)
    # # Test data
    # # challenge_dict = {'difficulty':8,
    # #                   'block': {"data":[],"nonce":None}}
    #
    # # Unpack the elements
    # challenge_string = challenge_dict['include']
    # hashed_string = hash_string(challenge_string)
    # print(f'string: {challenge_string}')
    # print(f'hash: {hashed_string}')

    target_str = 'me cago en san dios'
    target_bytes = str.encode(target_str)
    print('str bytes')
    print(target_bytes)
    pref1 = 'd131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70'
    # pref1 += target_hex
    pref1_bytes = bytes.fromhex(pref1)
    print('\npref bytes')
    print(pref1_bytes+target_bytes)
#     pref1 = '''d131dd02c5e6eec4 693d9a0698aff95c 2fcab58712467eab 4004583eb8fb7f89
# 55ad340609f4b302 83e488832571415a 085125e8f7cdc99f d91dbdf280373c5b
# d8823e3156348f5b ae6dacd436c919c6 dd53e2b487da03fd 02396306d248cda0
# e99f33420f577ee8 ce54b67080a80d1e c69821bcb6a88393 96f9652b6ff72a70'''
    pref2 = 'd131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70'
    # pref2 += target_hex
    pref2_bytes = bytes.fromhex(pref2) #+ pref1_bytes
    # print(hash_file('file1'))
    # print(hash_file('file2'))
    print(md5(pref1_bytes+target_bytes).hexdigest())
    print(md5(pref2_bytes+target_bytes).hexdigest())
    #
    # # Find the correct "nonce"
    # nonce_try = -1
    # while not dict_hash_check(block, difficulty)[0]:
    #     nonce_try += 1
    #     block["nonce"] = nonce_try
    #
    # print('hash: {dict_hash_check(block, difficulty)[1]}')
    # print(f'"nonce" value:pref {nonce_try}')

    # Dict for the solution
    # challenge_solution = {'files': [file1, file2]}

    # Solution POST
    # return solution_post(challenge_name, token, challenge_solution)

def hash_file(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def hash_string(base_string):
    return md5(base_string.encode('UTF-8',"strict")).hexdigest()

def dict_hash_check(block, difficulty):
    ''' Function to check if the sha256 hash of the block fulfills the condition
    for the given difficulty.'''
    # Obtain the str representation of the block with the given conditions
    str_block = str(block).replace("'",'"').replace(' ','')
    str_block = str_block.encode('UTF-8',"strict")
    # Hash
    sha_str = sha256(str_block).hexdigest()
    bytes_0 = difficulty//4 # Difficulty is given in bits, not bytes
    # Return the check and the value of the hash (for debugging)
    return sha_str[:bytes_0] == '0'*bytes_0, sha_str

if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
