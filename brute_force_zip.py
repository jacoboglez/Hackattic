from hackattic import *
from zipfile import ZipFile
from os import remove

def main(token):
    # Name of the challenge
    challenge_name = 'brute_force_zip'
    # https://hackattic.com/challenges/brute_force_zip

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)

    # Get the file URL
    zip_url = challenge_dict['zip_url']
    file_request(zip_url, zip_name = "zipfile.zip")

    # Exctract the file
    with ZipFile('zipfile.zip') as zipfile:
        zipfile.extractall(pwd=bytes('pass', encoding = 'UTF-8'))


    # # Dict for the solution
    # challenge_solution = {"secret": '0'}
    #
    # # Solution POST
    # return solution_post(challenge_name, token, challenge_solution)


if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
