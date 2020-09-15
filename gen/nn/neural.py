

class Neural(object):
    def __init__(self, _layers: int, _learning_rate: float):
        super(Neural, self).__init__()
        self.__nlayers = _layers
        self.__learn_rate = _learning_rate
    

    @property
    def nlayers(self) -> int:
        return self.__nlayers
    @nlayers.setter
    def nlayers(self, other) -> None:
        self.__nlayers = other

n = Neural(1,1)