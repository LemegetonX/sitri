import configparser
import os
import typing

from sitri.providers.base import ConfigProvider


class IniConfigProvider(ConfigProvider):
    """Config provider for Initialization file (Ini)."""

    provider_code = "ini"

    def __init__(
            self,
            ini_path: str = "./config.ini",
    ):
        """

        :param ini_path: path to ini file
        """
        self.configparser = configparser.ConfigParser()

        with open(os.path.abspath(ini_path), 'r') as f:
            self.configparser.read_file(f)

        self._sections = None

    @property
    def sections(self):
        if not self._sections:
            self._sections = list(self.configparser.keys())

        return self._sections

    def get(self, section: str, key: str, default: typing.Any = None, **kwargs) -> typing.Optional[typing.Any]:
        """Get value from ini file.

        :param section: section of ini file
        :param key: key or path for search
        :param default: fallback value if key not found
        """
        if section not in self.sections:
            return None

        return self.configparser[section].get(key, default)

    def keys(self, section: str) -> typing.List[str]:
        """Get keys of section

        :param section: section of ini file
        """
        if section not in self.sections:
            return []

        return list(self.configparser[section].keys())
