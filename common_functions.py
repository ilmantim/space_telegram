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


if __name__ == '__main__':
    try:
        image_url = "https://example.com/image.jpg"  
        save_path = "image.jpg" 

        if download_image(image_url, save_path):
            print("Image downloaded successfully.")
        else:
            print("Image download failed.")
    except requests.exceptions.RequestException as e:
        print("Error downloading the image:", str(e))

