import os
import requests


def load_image(url, file_path):
    response = requests.get(url)
    file_name = os.path.basename(file_path)
    dir_path = "images"
    os.makedirs(dir_path, exist_ok=True)

    with open(os.path.join(dir_path, file_name), "wb") as f:
        f.write(response.content)


def get_ext(url):
    return os.path.splitext(url)[-1]


def get_image_to_upload(images_path):
    if not os.path.exists(images_path):
        return None
    for image in os.listdir(images_path):
        yield os.path.join(images_path, image)