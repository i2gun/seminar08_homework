class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class LenNameError(Exception):
    def __init__(self, txt):
        self.txt = txt