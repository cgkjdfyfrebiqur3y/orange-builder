import time
import random
import sys
from helpers.ifexists import Ifexists

class RainbowOrangeGenerator:
    defaultcolors = [
        "\033[91m",  # Red
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[96m",  # Cyan
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
    ]

    def __init__(self, colors=None, *, amount=10):
        self.colors = Ifexists(colors, self.defaultcolors)  # callable
        self.amount = amount

    def __iter__(self):
        return self  # make it an iterator

    def __next__(self):
        color_list = self.colors()        # call Ifexists to get the list
        color = random.choice(color_list) # pick a random color
        sys.stdout.write(f"{color}orange \033[0m")
        sys.stdout.flush()
        return "orange"  # return string for __str__ or other uses

    def __str__(self):
        return " ".join(next(self) for _ in range(self.amount))