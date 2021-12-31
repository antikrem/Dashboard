from datetime import datetime
from os import listdir, path, scandir, stat
from shutil import disk_usage
from typing import Dict, Union
from format import as_table, format_bytes
from source import Source


class Storage(Source) :
    def __init__(self, directory : str, alias : Union[Dict[str, str], None]) :
        self._directory = directory
        self._alias = alias
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
        self._spaces = {
            self._directory_name(subDirectory) : self._get_size(path.join(self._directory, subDirectory)) 
            for subDirectory in listdir(self._directory) if self._is_valid_directory(subDirectory)
        }

    def _directory_name(self, subDirectory: str) :
        if (self._alias is not None and subDirectory in self._alias) :
            return self._alias[subDirectory]
        return subDirectory

    def _is_valid_directory(self, subDirectory: str) -> bool :
        return subDirectory != 'lost+found' and path.isdir(path.join(self._directory, subDirectory))

    def _get_size(self, path: str) -> int :
        try:
            with scandir(path) as it:
                sizes = [self._get_size(entry) for entry in it]
                if (len(sizes) == 0) :
                    return [0, 0]
                return [sum(i) for i in zip(*sizes)]
        except NotADirectoryError:
            return [stat(path).st_size, 1]

    def render(self) :
        tableSize = [30, 30, 30, 30]
        header = [["Name", "Used", "Size", "Files"]]
        total = [["Total", "100.00%", format_bytes(self._total), "--"]]
        data = [[name, format(space[0] / self._total,'.2%'), format_bytes(space[0]), str(space[1])] for name, space in self._spaces.items()]
        free = [["Free", format(self._free / self._total,'.2%'), format_bytes(self._free), "--"]]
        return as_table(tableSize, header + total + data + free)