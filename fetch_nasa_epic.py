import os
import requests
import argparse
from common_functions import get_file_extension, download_image
from dotenv import load_dotenv


def fetch_nasa_epic(count):
    base_directory =  os.path.dirname(os.path.abspath(__file__))
    images_directory = os.path.join(base_directory, "images")
    os.makedirs(images_directory, exist_ok=True)

    params = {
        "api_key": token,
    }

    url = "https://api.nasa.gov/EPIC/api/natural/images"

    response = requests.get(url, params=params)  
    response.raise_for_status()

    epic_json = response.json()

    download_urls = []  
    
    for picture in epic_json:
        if count is None or len(download_urls) >= int(count): 
            break
        date = picture["date"]
        image = picture["image"]
        
        year, month, day = date.split()[0].split('-')
    
        download_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image}.png"
        download_urls.append(download_url)  
    
    for index, image_url in enumerate(download_urls, start=1):
        extension = get_file_extension(image_url)
        filename = f"image{index}{extension}"
        save_path = os.path.join(images_directory, filename)

        try:
            download_image(image_url, params, save_path)
            print("Image was downloaded and saved successfully.")
            
        except:
             print(f"Image {index} download failed.")

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('NASA_TOKEN')

    try:                  
        parser = argparse.ArgumentParser(description='Download NASA EPIC images')
        parser.add_argument('--count', help='Specify the number of images to download')
        args = parser.parse_args()
        
        fetch_nasa_epic(args.count) 

    except requests.exceptions.RequestException as e:
        print("Error:", e)