from typing import Callable

class Redirect:
    """Map self.write to a function"""

    def __init__(self, func: Callable) -> "Redirect":
        self.func = func

    def write(self, line: str) -> None:
        self.func(line)