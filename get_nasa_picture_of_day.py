import argparse

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from download_and_save_image import download_and_save_image

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def load_nasa_picture_of_day(
        nasa_api_key=None,
        folder="images",
        number_of_photos=5,
        ):
    params = {
        "api_key": nasa_api_key,
        "count": number_of_photos,
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params,
        verify=False,
    )
    response.raise_for_status()
    for item in response.json():
        download_and_save_image(item["url"], folder)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "nasa_api_key",
        help="API ключ от api.nasa.gov",
        type=str,
    )
    parser.add_argument(
        "folder",
        nargs='?',
        default="images",
        help="Название папки для сохранения фото",
        type=str,
    )
    parser.add_argument(
        "number_of_photos",
        nargs='?',
        default=5,
        help="Количество запрашиваемых фотографий",
        type=int,
    )
    args = parser.parse_args()
    load_nasa_picture_of_day(
        nasa_api_key=args.nasa_api_key,
        folder=args.folder,
        number_of_photos=args.number_of_photos,
    )

if __name__ == "__main__":
    main()
