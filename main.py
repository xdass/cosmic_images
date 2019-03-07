import os
import time
import argparse
from utils import get_image_to_upload
import instabot
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
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
