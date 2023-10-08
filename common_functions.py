import os
import requests
from urllib.parse import urlparse, unquote, urlsplit


def get_file_extension(url):
    parser = urlsplit(url)
    path = unquote(parser.path)
    directory, filename = os.path.split(path)
    name, extension = os.path.splitext(filename)
    return extension


def download_image(image_url, params, save_path):
    response = requests.get(image_url, params=params)
    response.raise_for_status()

    with open(save_path, "wb") as file:
        file.write(response.content)
    return True


def get_image_files(directory):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            image_files.append(os.path.join(root, file))

    return image_files

