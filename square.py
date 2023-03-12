# Hard coded values:
# MIN: 1, 1, 10
# MAX: 9, -1, 0
class Square:
    def __init__(self, parent=None):
        # Hard coded value of square can be adjusted to allow for different sudoku alphabets.
        self.__square__ = 1
        self.__child__ = None
        self.__parent__ = parent
    def get_leaf(self):
        if self.__child__:
            return self.__child__.get_leaf()
        return self
    def get_square(self):
        return self.__square__
    def increment(self):
        # Increment logic depends on the sudoku alphabet.
        self.__square__ += 1
        if self.__square__ == 10:
            if self.__parent__ is None:
                # This is the root node. The search has finished.
                return False
            self.__parent__.increment()
            self.__parent__.unset_child()
        return True
    def set_child(self, child):
        self.__child__ = child
    def unset_child(self):
        self.__child__ = None
    def get_path(self):
        yield self.__square__
        if self.__child__:
            yield from self.__child__.get_path()
            #for square in self.__child__.get_path():
            #             yield square
