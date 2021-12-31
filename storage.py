from datetime import datetime
from os import listdir, path, scandir, stat
from shutil import disk_usage
from format import as_table
from source import Source
from hurry.filesize import size


class Storage(Source) :
    def __init__(self, directory : str) :
        self._directory = directory
        self._spaces = {}
        self._total = 0
        self._free = 0

    def name(self) :
        return "Storage"

    def period(self) :
        return 360

    def update(self) :
        total, used, free = disk_usage(self._directory)
        self._total = total

        self._free = free
        self._spaces = {subDirectory : self._get_size(path.join(self._directory, subDirectory)) for subDirectory in listdir(self._directory) if self._is_valid_directory(subDirectory)}

    def _is_valid_directory(self, subDirectory: str) -> bool :
        return subDirectory != 'lost+found' and path.isdir(path.join(self._directory, subDirectory))

    def _get_size(self, path: str) -> int :
        try:
            with scandir(path) as it:
                return sum(self._get_size(entry) for entry in it)
        except NotADirectoryError:
            return stat(path).st_size

    def render(self) :
        tableSize = [35, 35, 35]
        header = [["Name", "Percentage", "Size"]]
        total = [["Total", "--", size(self._total)]]
        data = [[name, format(space / self._total,'.2%'), size(space)] for name, space in self._spaces.items()]
        free = [["Free", format(self._free / self._total,'.2%'), size(self._free)]]
        return as_table(tableSize, header + total + data + free)