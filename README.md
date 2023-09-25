# Space Telegram

This project automates the collection and publishing of space-related images to a Telegram channel. 

## How to install

Python3 should already be installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

A Telegram channel where you have administrative privileges. You'll need the chat ID for this channel.

### Obtain API Tokens

#### NASA API Token
To collect space photos, you'll need an API token from NASA. You can obtain one by visiting the [NASA API website](https://api.nasa.gov/).

#### Telegram Bot Token
Create a Telegram bot using [BotFather](https://t.me/botfather) and obtain an API token for your bot.

### Configuration

Create a .env file in the project's root directory.

Add the following environment variables:

```bash
NASA_TOKEN=YOUR_NASA_API_TOKEN
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
TG_CHAT_ID=YOUR_CHANNEL_ID
PUBLISH_INTERVAL=14400
```
Replace YOUR_NASA_API_TOKEN with your NASA API token, 

YOUR_TELEGRAM_BOT_TOKEN with your Telegram bot's API token, 

YOUR_CHANNEL_ID with your Telegram channel's ID, and

PUBLISH_INTERVAL with your desired publication interval in seconds (default is 4 hours).

## How to run Scripts

### Fetch SpaceX Launch Images

The fetch_spacex_launch.py script allows you to fetch and download images from the last SpaceX launch.

To use this script, run the following command:

```bash
python fetch_spacex_launch.py [--launch_id LAUNCH_ID]
```
--launch_id (optional): Specify the launch ID to download images from a specific launch.

### Fetch NASA APOD (Astronomy Picture of the Day) Images

The fetch_nasa_apod.py script fetches images from NASA's Astronomy Picture of the Day.

To use this script, run the following command:

```bash
python fetch_nasa_apod.py [--count COUNT]
```
--count: Specify the number of images to download.

### Fetch NASA EPIC (Earth Polychromatic Imaging Camera) Images

The fetch_nasa_epic.py script allows you to fetch images from NASA's EPIC service.

To use this script, run the following command:

```bash
python fetch_nasa_epic.py [--count COUNT]
```
--count: Specify the number of images to download.

### Publish Images to Telegram

The publish_image.py script publishes image to your Telegram channel. 

You can either specify a specific image to publish or let the script choose a random 

image from a directory.

To publish a specific image, run:

```bash
python publish_image.py --image IMAGE_PATH
```
--image: Path to the image file you want to publish.

To publish a random image from a directory, run:

```bash
python publish_image.py 
```
### AutoPublish Images to Telegram

You can automate the process of publishing images at regular intervals using the autopublish_images.py script.

To use this script, run the following command:

```bash
python autopublish_images.py
```

## Project Goals
The code is written for educational purposes on online-course for web-developers, dvmn.org.



