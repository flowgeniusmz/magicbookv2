import base64

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    encoded_image = base64.b64decode(image_file.read()).decode('utf-8')
    return encoded_image
    