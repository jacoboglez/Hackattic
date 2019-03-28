from hackattic import *
from hashlib import sha256

def main(token):
    # Name of the challenge
    challenge_name = 'mini_miner'

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)

    # Test data
    # challenge_dict = {'difficulty':8,
    #                   'block': {"data":[],"nonce":None}}

    # Unpack the elements
    block = challenge_dict['block']
    difficulty = challenge_dict['difficulty']

    # Re-order the dict keys (possible from python 3.7)
    del block['nonce']
    block['nonce'] = None

    print(f'difficulty: {challenge_dict["difficulty"]}')

    # Find the correct "nonce"
    nonce_try = -1
    while not dict_hash_check(block, difficulty)[0]:
        nonce_try += 1
        block["nonce"] = nonce_try

    print('hash: {dict_hash_check(block, difficulty)[1]}')
    print(f'"nonce" value: {nonce_try}')

    # Dict for the solution
    challenge_solution = {"nonce": nonce_try}

    # Solution POST
    return solution_post(challenge_name, token, challenge_solution)


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
