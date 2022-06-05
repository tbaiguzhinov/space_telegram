import argparse
from urllib.parse import urljoin

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from download_and_save_image import download_and_save_image


def fetch_spacex_launch(folder="images", launch_id=None):
    spacex_api_url = "https://api.spacexdata.com/v4/launches"
    if launch_id:
        spacex_api_url = urljoin(spacex_api_url, launch_id)
    response = requests.get(
        spacex_api_url,
        verify=False,
    )
    response.raise_for_status()
    if launch_id and item["links"]["flickr"]["original"]:
        links = item["links"]["flickr"]["loriginal"]
    elif not launch_id:
        for item in response.json()[::-1]:
            if item["links"]["flickr"]["original"]:
                links = item["links"]["flickr"]["original"]
    else:
        return
    for link in links:
        download_and_save_image(link, folder)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--folder",
        nargs='?',
        default="images",
        help="Название папки для сохранения фото",
        type=str,
    )
    parser.add_argument(
        "--launch_id",
        nargs='?',
        default=None,
        help="ID запуска SpaceX",
        type=str,
    )
    args = parser.parse_args()
    fetch_spacex_launch(folder=args.folder, launch_id=args.launch_id)

if __name__ == "__main__":
    main()
