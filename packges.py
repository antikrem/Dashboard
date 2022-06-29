from typing import Tuple, Union
from requests import get
from requests.models import Response
from source import Source
from dateutil import parser
from format import as_table
from datetime import datetime, timezone


class Packages(Source):

    def __init__(self, *args : str) :
        self._pakages = dict.fromkeys(args, None)
 
    def name(self) :
        return "Nuget Packages"

    def period(self) :
        return 15

    def update(self) :
        self._pakages = { k: self._get_package(k) or v for k, v in self._pakages.items()}

    def render(self) :
        size = [30, 30, 30, 30]
        header = [["Package", "Published", "Version", "Online"]]
        data = [self._parse_row(v) for v in self._pakages.values() if v is not None]
        return as_table(size, header + data)

    def _get_package(self, name: str) -> Union[Tuple[str, str, str], None] :
        endpoint = f'https://api.nuget.org/v3/registration5-semver1/{name}/index.json'

        response = get(endpoint)
        if (response is None or response.status_code != 200) :
            return None
        
        latestPackage = response.json()['items'][0]['items'][-1]['catalogEntry']

        return [latestPackage['id'], latestPackage['published'], latestPackage['version']]

    def _parse_row(self, row) :
        published = parser.parse(row[1])
        offset = datetime.now().replace(tzinfo=timezone.utc)  - published
        return [row[0], published.strftime("%d/%m/%Y %H:%M"), row[2], str(offset)]
