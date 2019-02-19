import abc


class Model(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def to_db(self):
        pass

    @abc.abstractmethod
    def from_db(self):
        pass
