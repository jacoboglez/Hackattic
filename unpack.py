from hackattic import data_request, solution_post, read_token
import base64
import struct


def main(token):
    # Name of the challenge
    challenge_name = 'help_me_unpack'

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)

    # Decode the base64 data into bytes
    challenge_bytes = base64.b64decode(challenge_dict['bytes'])

    # Unpack the bytes into their format. The last one is decoded into a string
    # to parse it later as big-endian
    decoded_numbers = struct.unpack('iIhfd8s', challenge_bytes)
    # Convert the last number as big-endian
    challenge_big_doube = struct.unpack('>d',decoded_numbers[5])

    # Assign each value of the answer to its dictionary key
    challenge_solution = {}
    challenge_solution['int'] = decoded_numbers[0]
    challenge_solution['uint'] = decoded_numbers[1]
    challenge_solution['short'] = decoded_numbers[2]
    challenge_solution['float'] = decoded_numbers[3]
    challenge_solution['double'] = decoded_numbers[4]
    challenge_solution['big_endian_double'] = challenge_big_doube[0]

    return solution_post(challenge_name, token, challenge_solution)


if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
