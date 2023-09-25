import os
import random
import time
import argparse
from dotenv import load_dotenv
import telegram
from common_functions import get_image_files


def autopublish_images(chat_id, publish_interval):
    base_directory =  os.path.dirname(os.path.abspath(__file__))
    directory = os.path.join(base_directory, "images")
    
    image_files = get_image_files(directory)

    while True:
        random.shuffle(image_files)  
        for image_file in image_files:
            with open(image_file, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(publish_interval)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    bot = telegram.Bot(token)
    
    publish_interval = int(os.getenv('PUBLISH_INTERVAL'))

    autopublish_images(chat_id,publish_interval)
