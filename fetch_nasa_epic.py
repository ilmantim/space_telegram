import os
import requests
import argparse
from common_functions import get_file_extension, download_image
from dotenv import load_dotenv


def fetch_nasa_epic(count, token):
    base_directory =  os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(base_directory, "images")
    os.makedirs(images_directory, exist_ok=True)

    params = {
        "api_key": token,
    }

    url = "https://api.nasa.gov/EPIC/api/natural/images"

    response = requests.get(url, params=params)  
    response.raise_for_status()

    epic_pictures = response.json()

    picture_urls = []  
    
    for picture in epic_pictures:
        if count is None or len(picture_urls) >= int(count): 
            break
        date = picture["date"]
        image = picture["image"]
        
        year, month, day = date.split()[0].split('-')
    
        picture_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png"
        picture_urls.append(picture_url)  
    
    for index, image_url in enumerate(picture_urls, start=1):
        extension = get_file_extension(image_url)
        filename = f"image{index}{extension}"
        save_path = os.path.join(images_directory, filename)

        download_image(image_url, params, save_path)
        print("Image was downloaded and saved successfully.")
            

def main():
    load_dotenv()
    token = os.getenv('NASA_TOKEN')

    parser = argparse.ArgumentParser(description='Download NASA EPIC images')
    parser.add_argument('--count', help='Specify the number of images to download')
    args = parser.parse_args()
    
    try:
        fetch_nasa_epic(args.count, token)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    main()