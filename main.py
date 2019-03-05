import os
import time
import argparse
import instabot
from dotenv import load_dotenv


load_dotenv()


def get_image_to_upload(images_path):
    if os.path.exists(images_path):
        for image in os.listdir(images_path):
            yield os.path.join(images_path, image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload images to Instagram account')
    parser.add_argument('path', metavar='-p', help='Path to images directory')
    args = parser.parse_args()
    images_path = args.path
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')
    bot = instabot.Bot()
    bot.login(username=user, password=password)
    for image in get_image_to_upload(images_path):
        time.sleep(4)
        bot.upload_photo(image)
