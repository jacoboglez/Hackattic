import requests
import json

def image_request(image_url, image_name = "image.png"):
    res = requests.get(image_url)
    res.raise_for_status()

    with open(image_name, 'wb') as handler:
        handler.write(res.content)
    print('Image obtained.')



def read_token(token_file):
    with open(token_file,'r') as file_handler:
        token = file_handler.readline()
        return token.rstrip()


def data_request(challenge_name, token):
    # Construct the challenge URL
    challenge_url = r'https://hackattic.com/challenges/'+challenge_name+'/'
    # Request of the data
    res = requests.get(challenge_url+'problem?access_token='+token.strip())
    res.raise_for_status()

    # Data of the challenge to a dict
    challenge_dict = res.json()

    return challenge_dict

def solution_post(challenge_name, token, challenge_solution):
    # Construct the challenge URL
    challenge_url = r'https://hackattic.com/challenges/'+challenge_name+'/'
    # Dump the dict of the solution into a json to do the POST
    challenge_sol_json = json.dumps(challenge_solution)

    # POST request with the solution
    headers = {'content-type': 'application/json'}
    res = requests.post(challenge_url+'solve?access_token='+token,
    data = challenge_sol_json,
    headers = headers)

    res.raise_for_status()

    response = res.json()

    # Check if solved -> Go playground mode
    if "message" in response.keys():
        print(response["message"])
    if "hint" in response.keys():
        print(response["hint"])
        if "&playground=1" in response["hint"].split(' '):
            print('Sending in playground mode.')
            res = requests.post(challenge_url+'solve?access_token='+token+'&playground=1',
            data = challenge_sol_json,
            headers = headers)
            res.raise_for_status()
            response = res.json()

    # Output of the challenges
    if "rejected" in response.keys():
        print('FAILED Attempt:')
        print(response["rejected"])
        return 1
    if "result" in response.keys() and "passed" in response["result"].split(' '):
        print('PASSED')
        return 0
    else:
        print('ERROR: Unexpected case')
        return 1
