import os
import random
import argparse
import telegram
from common_functions import get_image_files
from dotenv import load_dotenv


def publish_image(directory, chat_id, bot, image_path=None):
    if image_path:
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
    else:
        images = get_image_files(directory)
        if not images:
            return None  

        random_image = random.choice(images)
        with open(random_image, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    bot = telegram.Bot(token)

    parser = argparse.ArgumentParser(description='Publish an image to a Telegram channel')
    parser.add_argument('--image', help='Path to the image file to publish')
    args = parser.parse_args()


    if args.image:
        publish_image(args.image, chat_id, bot)
    else:
        directory = './images'
        result = publish_image(directory, chat_id, bot)
        if result is None:
            print("There is no specific image input, publish random")
        else:
            print("Image was published successfully.")  








