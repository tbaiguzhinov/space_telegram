import os
from datetime import datetime
from urllib.parse import unquote, urljoin, urlparse

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def download_and_save_image(url, folder, params=None):
    response = requests.get(
        url,
        params=params,
        verify=False
        )
    response.raise_for_status()
    url_path = urlparse(unquote(url)).path
    parent, full_file_name = os.path.split(url_path)
    filename, extension = os.path.splitext(full_file_name)
    os.makedirs(folder, exist_ok=True)
    with open(
            os.path.join(folder, f"{filename}{extension}"),
            "wb") as file:
        file.write(response.content)


def fetch_spacex_last_launch(folder):
    spacex_api = "https://api.spacexdata.com/v4/launches"
    response = requests.get(
        spacex_api,
        verify=False)
    response.raise_for_status()
    for item in response.json()[::-1]:
        if item["links"]["patch"]["large"]:
            link = item["links"]["patch"]["large"]
            download_and_save_image(link, folder)
            return


def load_nasa_picture_of_day(number, folder):
    params = {
        "api_key": "j1MJD6p7mREHNaZ6XY6g8a6y83lryVN1acsxr14K",
        "count": number,
    }
    response = requests.get(
        "https://api.nasa.gov/planetary/apod",
        params=params,
        verify=False,
        )
    response.raise_for_status()
    for item in response.json():
        download_and_save_image(item["url"], folder)


def get_nasa_epic_image():
    params = {
        "api_key": "j1MJD6p7mREHNaZ6XY6g8a6y83lryVN1acsxr14K",
    }
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params=params,
        verify=False,
    )
    response.raise_for_status()
    for photo in response.json():
        photo_datetime = datetime.strptime(photo["date"], "%Y-%m-%d %H:%M:%S")
        photo_name = photo["image"]
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photo_datetime.year}/{photo_datetime.month:02d}/{photo_datetime.day:02d}/png/{photo_name}.png"
        download_and_save_image(url, "images", params=params)
