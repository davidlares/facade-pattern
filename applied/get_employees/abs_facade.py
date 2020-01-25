import abc

# this is an "interface" - methods will be method implemented, just declared
class AbsFacade(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_employees(self):
        pass
