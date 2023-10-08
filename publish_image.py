import os
import random
import argparse
import telegram
from common_functions import get_image_files
from dotenv import load_dotenv

publish = lambda image_path, chat_id, bot: bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    bot = telegram.Bot(token)

    parser = argparse.ArgumentParser(description='Publish an image to a Telegram channel')
    parser.add_argument('--image', help='Path to the image file to publish')
    args = parser.parse_args()

    if args.image:
        publish(args.image, chat_id, bot)
    else:
        directory = './images'
        images = get_image_files(directory)
        
        if not images:
            print("No images found in the directory.")
        else:
            random_image = random.choice(images)
            publish(random_image, chat_id, bot)
  









