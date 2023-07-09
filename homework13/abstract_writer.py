from abc import ABC, abstractmethod


class Writer:
    @abstractmethod
    def write_to_file(self, data): ...
