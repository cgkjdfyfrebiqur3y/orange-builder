class Ifexists:
    def __init__(self, value, default):
        self.value = value
        self.default = default

    def __call__(self):
        return self.default if not self.value else self.value