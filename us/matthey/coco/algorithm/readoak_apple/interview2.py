"""
Design and implement a system to support multiple operating systems platforms.
The system should be able to handle: disk, windows, network and monitor components.
The supported platforms are: Mac, Linux, etc.
DiskDriver
	* read_file()
	* write_file()
WindowManager
	* show_window()
	* close_window()
NetworkAdapter
	* connect()
	* disconnect()
Monitor
	* cpu()
	* mem()
	* io()
"""
from abc import ABC, abstractmethod
from aifc import Error


class AC(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self):
        pass

class Mac(AC):
    def read_file(self):
        return 'On Mac'

class Linux(AC):
    def read_file(self):
        return 'On Linux'

class Window(AC):
    def read_file(self):
        return 'On Window'

class NewDevice(AC):
    def write_file(self):
        raise Error('unsupported operatoin')

def generateF(name):
    d = {'mac': Mac.__class__}
    if name in d:
        return d[name]