import os
import requests
import argparse
from common_functions import get_file_extension, download_image
from dotenv import load_dotenv


def fetch_nasa_apod(count, token):
    base_directory =  os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(base_directory, "images")
    os.makedirs(images_directory, exist_ok=True)
    
    params = {
        "api_key": token,
        "count": count,
    }
    
    url = "https://api.nasa.gov/planetary/apod"
    
    response = requests.get(url, params=params)  
    response.raise_for_status()  
    
    apod_pictures = response.json()
    original_urls = [picture["url"] for picture in apod_pictures]
   
    
    for index, image_url in enumerate(original_urls, start=1):
        extension = get_file_extension(image_url)
        filename = f"image{index}{extension}"
        save_path = os.path.join(images_directory, filename)
    
        download_image(image_url, params, save_path)
        print("Image was downloaded and saved successfully.")


def main():
    load_dotenv()
    token = os.getenv('NASA_TOKEN')

    parser = argparse.ArgumentParser(description='Download NASA APOD images')
    parser.add_argument('--count', help='Specify the number of images to download')
    args = parser.parse_args()
    
    fetch_nasa_apod(args.count, token)

        
if __name__ == "__main__":
    main()






