import os
import logging
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from dotenv import load_dotenv

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from fetch_spacex_images import fetch_spacex_launch
from get_nasa_epic_images import get_nasa_epic_image
from get_nasa_picture_of_day import load_nasa_picture_of_day
from publish_image_to_telegram import publish_image_to_telegram


def main():
    load_dotenv()
    while True:
        try:
            publish_image_to_telegram(
                telegram_token=os.getenv("TELEGRAM_TOKEN"),
                chat_id=os.getenv("CHAT_ID"),
                folder="images",
            )
            time.sleep(int(os.getenv("SETBACK", default=4))*60*60)
        except (IndexError, FileNotFoundError):
            logging.error("Фотографии отсутствуют")
            fetch_spacex_launch(folder="images")
            get_nasa_epic_image(
                nasa_api_key=os.getenv("NASA_API_KEY"),
                folder="images",
                number_of_photos=5,
            )
            load_nasa_picture_of_day(
                nasa_api_key=os.getenv("NASA_API_KEY"),
                folder="images",
                number_of_photos=5,
            )


if __name__ == "__main__":
    main()
