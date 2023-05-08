import base64
# from PIL import Image


def imageConverter(image):
    # Open the image file

    # Convert the image to Base64
    image_base64 = base64.b64encode(image).decode('utf-8')

    # Print the Base64 string
    return image_base64