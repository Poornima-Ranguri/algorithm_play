class With_Under():
    """Accessor methods make no difference to the attribute's accessibility.

    Attribute _attr is always accessible after With_Under has been
    instantiated, simply by calling it as .
    """
    def __init__(self):
        self._attr = 0

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, value):
        self._attr = value

    @attr.deleter
    def attr(self):
        del self._attr


class With__Dunder():
    """Dunder prefix prevents access to attribute, except through accessors.

    Although With__Dunder can be instantiated in code and an attribute
    __attr attached to it in code, that attribute has no relationship to
    self.__attr below.

    Neither __dir__() nor __getattribute__('__attr') will return it, either.
    """
    def __init__(self):
        self.__attr = 0

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        self.__attr = value

    @attr.deleter
    def attr(self):
        del self.__attr
