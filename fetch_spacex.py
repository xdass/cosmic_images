from utils import *


def fetch_spacex_last_launch():
    api_url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(api_url)
    image_links = response.json()['links'].get('flickr_images')
    for idx, link in enumerate(image_links):
        load_image(link, f"spacex{idx}.jpg")


if __name__ == '__main__':
    fetch_spacex_last_launch()
