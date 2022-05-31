import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def main():
    try:
        publish_image_to_telegram(
            telegram_token="5456681274:AAFa9ITxfuKFtHSt3bUT7ufGoz499YsJUx8",
            chat_id=-1001156275886,
            folder="images"
            )
    except IndexError:
        logging.error("No images found")
        nasa_api_key = "j1MJD6p7mREHNaZ6XY6g8a6y83lryVN1acsxr14K"
