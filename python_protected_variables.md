## Python protected variables

Combining `__`-prefixing with an explicit getter syntax (using @property) makes instance attribute accessible only through the getter by normal means.

```
In [1]: class C():
    def __init__(self):
        self._under = 'Under'
        self.__dunder = 'Dunder'

    @property
    def under(self):
        """Getter for casually non-public instance attribute."""
        return self._under

    @property
    def dunder(self):
        """Getter for truly protected instance attribute."""
        return self.__dunder
   ....:

In [2]: c = C()

In [3]: c.under
Out[3]: 'Under'

In [4]: c.dunder
Out[4]: 'Dunder'

In [5]: c._under
Out[5]: 'Under'

In [6]: c.__dunder
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-19-5d171ef73e24> in <module>()
----> 1 c.__dunder

AttributeError: 'C' object has no attribute '__dunder'
```

However, by prepending `_` and the name of the class (so `_C`) to the attribute, it is in fact accessible. This is called "name mangling".

```
In [7]: c._C__dunder
Out[7]: 'Dunder'

In [8]: c._C__dunder = 'q'

In [9]: c._C__dunder
Out[9]: 'q'
```

[end]