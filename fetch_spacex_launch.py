import os
import requests
import argparse
from common_functions import get_file_extension, download_image


def fetch_spacex_launch(launch_id):
    base_directory = os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(base_directory, "images")
    os.makedirs(images_directory, exist_ok=True)

    launch_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(launch_url)
    response.raise_for_status()
    launch_pictures = response.json()

    flickr_links = launch_pictures["links"]["flickr"]
    original_urls = flickr_links.get("original")

    for index, image_url in enumerate(original_urls, start=1):
        extension = get_file_extension(image_url)
        filename = f"image{index}{extension}"
        save_path = os.path.join(images_directory, filename)
                                 
        download_image(image_url, save_path, params=None)
        print(f"Image {index} downloaded successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download SpaceX launch images')
    parser.add_argument('--launch_id', default='latest', help='Specify the launch ID to download images from')
    args = parser.parse_args()
    
    fetch_spacex_launch(args.launch_id)