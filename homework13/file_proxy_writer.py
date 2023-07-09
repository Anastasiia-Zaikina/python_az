"""Implement writer for proxy pattern from the lesson"""
from homework13.abstract_writer import Writer
from homework13.txt_writer import TxtWriter
import os


class TxtProxyWriter(Writer):
    def __init__(self, txt_path: str, mode: str):
        self.__writer = TxtWriter(txt_path, mode)
        self.__txt_path = txt_path

    def write_to_file(self, data):
        if os.path.exists(self.__txt_path):
            raise TypeError('file already exist')
        else:
            self.__writer.write_to_file(data)
