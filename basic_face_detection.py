from hackattic import *
import cv2


def face_detect(imagePath):
    ''' Code adapted from:
    https://realpython.com/face-recognition-with-python/ '''

    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get image size
    img = cv2.imread(imagePath) 
    H, W, _ = img.shape
    tile_size = (H+W)/2 /8 
    print(f'tile_size = {tile_size}')

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    # Also append the tile position to a list

    face_tiles = []
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Tile number
        x_i = int((x+w//2)//tile_size)
        y_i = int((y+h//2)//tile_size)
        print(f'x: {x_i}, y: {y_i}')
        face_tiles.append([x_i, y_i])

    # cv2.imshow("Faces found", image)
    # cv2.waitKey(0)

    cv2.imwrite('faces_detected.png', image)

    return face_tiles


def main(token):
    # Name of the challenge
    challenge_name = 'basic_face_detection'
    # https://hackattic.com/challenges/basic_face_detection

    # Data of the challenge to a dict
    challenge_dict = data_request(challenge_name, token)

    # Get the file URL
    image_url = challenge_dict['image_url']
    image_request(image_url, image_name = "faces.png")

    face_tiles = face_detect("faces.png")

    # Dict for the solution
    challenge_solution = {"face_tiles": face_tiles}

    # Solution POST
    return solution_post(challenge_name, token, challenge_solution)


if __name__ == "__main__":
    # Token filename
    token = read_token("token.config")
    main(token)
