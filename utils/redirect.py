from typing import Callable

class Redirect:
    """
    Maps self.write to a function of choice
    
    ...

    Attributes
    ----------
    func : callalbe
        Function that is mapped to self.write

    """

    def __init__(self, func: Callable) -> "Redirect":
        """
        Parameters
        ----------
        func : callable
            Function that is mapped to self.write, 
            should take a single string as an argument
        """
        self.func = func

    def write(self, line: str) -> None:
        self.func(line)