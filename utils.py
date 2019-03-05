import os
import requests


def load_image(url, file_path):
    response = requests.get(url)
    file_name = os.path.basename(file_path)
    dir_path = "images"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(os.path.join(dir_path, file_name), "wb") as f:
        f.write(response.content)
        print(f"Файл {file_name} загружен")


def get_ext(url):
    return url.split('.')[-1]