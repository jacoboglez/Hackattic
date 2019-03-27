from hackattic import data_request, solution_post, image_request, read_token
from pyzbar.pyzbar import decode
from PIL import Image
from os import remove

def main(token):
    # Name of the challenge
    challenge_name = 'reading_qr'

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)

    # Get the image from the obtained URL
    challenge_image = image_request(challenge_dict["image_url"], "qr_image.png")

    # Decode de QR code
    decoded = decode(Image.open("qr_image.png"))
    final = decoded[0].data.decode("utf-8")

    # Remove the image file from disk
    remove("qr_image.png")

    # Generating the dict and sending the solution
    challenge_solution = {}
    challenge_solution['code'] = final

    return solution_post(challenge_name, token, challenge_solution)


if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
