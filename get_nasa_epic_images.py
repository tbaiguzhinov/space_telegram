import argparse
from datetime import datetime

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from download_and_save_image import download_and_save_image


def get_nasa_epic_image(
        nasa_api_key=None,
        folder="images",
        number_of_photos=5,
        ):
    params = {
        "api_key": nasa_api_key,
    }
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params=params,
        verify=False,
    )
    response.raise_for_status()
    photos = response.json()
    for photo in photos[:number_of_photos]:
        photo_datetime = datetime.strptime(
            photo["date"],
            "%Y-%m-%d %H:%M:%S"
        )
        photo_name = photo["image"]
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photo_datetime.year}/{photo_datetime.month:02d}/{photo_datetime.day:02d}/png/{photo_name}.png"
        download_and_save_image(url, folder, params=params)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "nasa_api_key",
        help="API ключ от api.nasa.gov",
        type=str,
    )
    parser.add_argument(
        "--folder",
        nargs='?',
        default="images",
        help="Название папки для сохранения фото",
        type=str,
    )
    parser.add_argument(
        "--number_of_photos",
        nargs='?',
        default=5,
        help="Количество запрашиваемых фотографий",
        type=int,
    )
    args = parser.parse_args()
    get_nasa_epic_image(
        nasa_api_key=args.nasa_api_key,
        folder=args.folder,
        number_of_photos=args.number_of_photos,
    )

if __name__ == "__main__":
    main()
