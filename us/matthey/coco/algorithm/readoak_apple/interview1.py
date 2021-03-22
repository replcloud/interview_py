# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from abc import ABC, abstractmethod


class AC(ABC):
    def __int__(self, val):
        self.val = val
        super(Some, self).__int__()

    @abstractmethod
    def calc(self):
        pass

class Some(AC):
    def calc(self):
        return 'Some here'

class Some2(AC):
    def calc(self):
        return super(Some2, self).calc() #'Some2 here'

def f(class_name):
    if class_name == 'Some':
        return Some()
    elif class_name == 'Some2':
        return Some2()
    else:
        return

def print_sorted_dict():
    d = {"a": 1, "b": 2, "d": 4, "c": 3}
    sorted_keys = [k for k in sorted(d)]
    for x in sorted_keys:
        print(f'{x}={d[x]}', end=' ')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Some().calc())
    print(Some2().calc())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
