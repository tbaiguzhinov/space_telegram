import os
from urllib.parse import unquote, urlparse

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def download_and_save_image(url, folder, params=None):
    response = requests.get(
        url,
        params=params,
        verify=False,
    )
    response.raise_for_status()
    url_path = urlparse(unquote(url)).path
    parent, full_file_name = os.path.split(url_path)
    filename, extension = os.path.splitext(full_file_name)
    os.makedirs(folder, exist_ok=True)
    with open(
            os.path.join(folder, f"{filename}{extension}"),
            mode="wb",
    ) as file:
        file.write(response.content)
