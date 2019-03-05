from utils import *


def fetch_hubble_image(image_id):
    hubble_api = f"http://hubblesite.org/api/v3/image/{image_id}"
    response = requests.get(hubble_api)
    best_image = response.json()['image_files'][-1]
    image_ext = get_ext(best_image['file_url'])
    image_url = best_image.get('file_url')
    load_image(image_url, f"{image_id}.{image_ext}")


def get_ids_from_collection(collection):
    api_url = f"http://hubblesite.org/api/v3/images/{collection}"
    response = requests.get(api_url)
    image_ids = [image_id.get('id') for image_id in response.json()]
    return image_ids


if __name__ == '__main__':
    ids = get_ids_from_collection('stsci_gallery')
    for img_id in ids:
        fetch_hubble_image(img_id)
