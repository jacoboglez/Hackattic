from hackattic import *
from hashlib import sha256, pbkdf2_hmac, scrypt
import hmac
import base64
from binascii import hexlify
import pyscrypt

def main(token):
    # Name of the challenge
    challenge_name = 'password_hashing'

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)
    print(challenge_dict)
    print()

    # Unpack the elements
    password = challenge_dict['password'].encode(encoding = 'UTF-8')
    print(f'password: {password}')
    salt = base64.b64decode(challenge_dict['salt']) #decode from base64
    print(f'salt: {salt}')
    print(f"salt: {salt.decode(encoding = 'ISO-8859-1')}")
    # PBKDF parameters
    hash_pbkdf2 = challenge_dict['pbkdf2']['hash']
    iterations_pbkdf2 = challenge_dict['pbkdf2']['rounds']
    # scrypt parameters
    scrypt_N = challenge_dict['scrypt']['N']
    scrypt_p = challenge_dict['scrypt']['p']
    scrypt_r = challenge_dict['scrypt']['r']
    scrypt_buflen = challenge_dict['scrypt']['buflen']
    _control = challenge_dict['scrypt']['_control']

    # SHA256
    pass_sha256 = sha256()
    pass_sha256.update(password)
    pass_sha256 = pass_sha256.hexdigest()
    print(f'SHA256: {pass_sha256}')


    # HMAC-SHA256
    pass_hmac = hmac.new(salt, msg = password, digestmod=sha256).hexdigest()
    print(f'HMAC-SHA256: {pass_hmac}')


    # PBKDF-SHA256
    pass_pbkdf2 = pbkdf2_hmac(hash_pbkdf2, password, salt, iterations_pbkdf2)
    pass_pbkdf2 = str(hexlify(pass_pbkdf2), encoding = 'UTF-8')
    print(f'PBKDF-SHA256: {pass_hmac}')


    # scrypt
    # print('scrypt parameters:')
    # print(f'N: {scrypt_N}')
    # print(f'r: {scrypt_r}')
    # print(f'p: {scrypt_p}')
    # print(f'buflen: {scrypt_buflen}')

    # pass_scrypt = pyscrypt.hash(password = bytes('rosebud',encoding = 'UTF-8'),
    #                    salt = bytes('pepper', encoding = 'UTF-8'),
    #                    N = 128,
    #                    r = 4,
    #                    p = 8,
    #                    dkLen = 32)

    # b19a18ea8a50a861d08eb94be602f6cbfe67ab98d2021400a3b83fbe3b8ba698

    pass_scrypt = pyscrypt.hash(password = password,
                       salt = salt,
                       N = scrypt_N,
                       r = scrypt_r,
                       p = scrypt_p,
                       dkLen = 32)

    pass_scrypt = str(hexlify(pass_scrypt), encoding = 'UTF-8')

from hackattic import *
from hashlib import sha256, pbkdf2_hmac, scrypt
import hmac
import base64
from binascii import hexlify
import pyscrypt

def main(token):
    # Name of the challenge
    challenge_name = 'password_hashing'

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)
    print(challenge_dict)
    print()

    # Unpack the elements
    password = challenge_dict['password'].encode(encoding = 'UTF-8')
    print(f'password: {password}')
    salt = base64.b64decode(challenge_dict['salt']) #decode from base64
    print(f'salt: {salt}')
    print(f"salt: {salt.decode(encoding = 'ISO-8859-1')}")
    # PBKDF parameters
    hash_pbkdf2 = challenge_dict['pbkdf2']['hash']
    iterations_pbkdf2 = challenge_dict['pbkdf2']['rounds']
    # scrypt parameters
    scrypt_N = challenge_dict['scrypt']['N']
    scrypt_p = challenge_dict['scrypt']['p']
    scrypt_r = challenge_dict['scrypt']['r']
    scrypt_buflen = challenge_dict['scrypt']['buflen']
    _control = challenge_dict['scrypt']['_control']

    # SHA256
    pass_sha256 = sha256()
    pass_sha256.update(password)
    pass_sha256 = pass_sha256.hexdigest()
    print(f'SHA256: {pass_sha256}')


    # HMAC-SHA256
    pass_hmac = hmac.new(salt, msg = password, digestmod=sha256).hexdigest()
    print(f'HMAC-SHA256: {pass_hmac}')


    # PBKDF-SHA256
    pass_pbkdf2 = pbkdf2_hmac(hash_pbkdf2, password, salt, iterations_pbkdf2)
    pass_pbkdf2 = str(hexlify(pass_pbkdf2), encoding = 'UTF-8')
    print(f'PBKDF-SHA256: {pass_hmac}')


    # scrypt
    # print('scrypt parameters:')
    # print(f'N: {scrypt_N}')
    # print(f'r: {scrypt_r}')
    # print(f'p: {scrypt_p}')
    # print(f'buflen: {scrypt_buflen}')

    # pass_scrypt = pyscrypt.hash(password = bytes('rosebud',encoding = 'UTF-8'),
    #                    salt = bytes('pepper', encoding = 'UTF-8'),
    #                    N = 128,
    #                    r = 4,
    #                    p = 8,
    #                    dkLen = 32)

    # b19a18ea8a50a861d08eb94be602f6cbfe67ab98d2021400a3b83fbe3b8ba698

    pass_scrypt = pyscrypt.hash(password = password,
                       salt = salt,
                       N = scrypt_N,
                       r = scrypt_r,
                       p = scrypt_p,
                       dkLen = 32)

    pass_scrypt = str(hexlify(pass_scrypt), encoding = 'UTF-8')



    # pass_scrypt = input('Introduce scrypt hash: \n')
    print(f'scrypt: {pass_scrypt}')

    # Dict for the solution
    challenge_solution = {'sha256': pass_sha256,
                          'hmac': pass_hmac,
                          'pbkdf2': pass_pbkdf2,
                          'scrypt': pass_scrypt }

    # Solution POST
    return solution_post(challenge_name, token, challenge_solution)

if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)


    # pass_scrypt = input('Introduce scrypt hash: \n')
    print(f'scrypt: {pass_scrypt}')

    # Dict for the solution
    challenge_solution = {'sha256': pass_sha256,
                          'hmac': pass_hmac,
                          'pbkdf2': pass_pbkdf2,
                          'scrypt': pass_scrypt }

    # Solution POST
    return solution_post(challenge_name, token, challenge_solution)

if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
