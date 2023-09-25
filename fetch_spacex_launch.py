import os
import requests
import argparse
from common_functions import get_file_extension, download_image


def fetch_spacex_launch(launch_id):
    base_directory = os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(base_directory, "images")
    os.makedirs(images_directory, exist_ok=True)

    launch_url = get_launch_url(launch_id)

    response = requests.get(launch_url)
    response.raise_for_status()

    launch_data = response.json()
    original_urls = get_original_image_urls(launch_data)

    if original_urls:
        download_images(original_urls, images_directory)
    else:
        print("No photos found for the latest launch. Trying a different launch...")

        launch_url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
        response = requests.get(launch_url)
        response.raise_for_status()

        launches = response.json()
        original_urls = get_original_image_urls(launches)

        if original_urls:
            download_images(original_urls, images_directory)
        else:
            print("No photos found for the chosen launch.")


def get_launch_url(launch_id):
    if launch_id:
        return f"https://api.spacexdata.com/v5/launches/{launch_id}"
    else:
        return "https://api.spacexdata.com/v5/launches/latest"


def get_original_image_urls(launch_data):
    flickr_links = launch_data["links"]["flickr"]
    return flickr_links.get("original")


def download_images(original_urls, images_directory):
    for index, image_url in enumerate(original_urls, start=1):
        extension = get_file_extension(image_url)
        filename = f"image{index}{extension}"
        save_path = os.path.join(images_directory, filename)

        result = download_image(image_url, save_path)

        if result:
            print("Image was downloaded and saved successfully.")
        else:
            print("Image download failed.")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Download SpaceX launch images')
        parser.add_argument('--launch_id', help='Specify the launch ID to download images from')
        args = parser.parse_args()

        fetch_spacex_launch(args.launch_id)

    except requests.exceptions.RequestException as e:
        print("Error:", e)









