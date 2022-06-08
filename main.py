import os
import logging
import requests
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from dotenv import load_dotenv

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from load_spacex_images import load_spacex_launch
from load_nasa_epic_images import load_nasa_epic_images
from load_nasa_picture_of_day import load_nasa_picture_of_day
from publish_image_to_telegram import publish_image_to_telegram, get_random_filepath


def main():
    load_dotenv()
    while True:
        try:
            file_path = get_random_filepath(folder="images")
            publish_image_to_telegram(
                telegram_token=os.getenv("TELEGRAM_TOKEN"),
                chat_id=os.getenv("CHAT_ID"),
                file_path=file_path,
            )
            os.remove(file_path)
            time.sleep(int(os.getenv("SETBACK", default=4))*60*60)
        except (IndexError, FileNotFoundError):
            logging.error("Фотографии отсутствуют")
            load_spacex_launch(folder="images")
            load_nasa_epic_images(
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
