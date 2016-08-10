import abc

class NotConcrete(metaclass=abc.ABCMeta):
    """Cannot be instantiated because of metaclass and decorators."""
    @abc.abstractmethod
    def abstract_method(self):
        print('in abstract method')

    @abc.abstractproperty
    def abstract_property(self):
        print('in abstract property')

class Concrete():
    """*Can* be instantiated because no metaclass."""
    @abc.abstractmethod
    def abstract_method(self):
        print('in abstract method')

    @abc.abstractproperty
    def abstract_property(self):
        print('in abstract property')
