## Basic decorator syntax

`functools.wraps` is an explicit decorator for defining decorators. Is it necessary? In this directory are two simple examples of the use of decorators — one without and one with `@wraps`.

The [docs](https://docs.python.org/3.5/library/functools.html?highlight=functools.wraps#functools.wraps) explain that `wraps` allows the `__name__` and `__doc__` attributes of the original function to be called correctly:

```
In [1]: import decorator_plain as d1

In [2]: import decorator_with_wraps as d2

In [3]: d1.get_text('A')
Out[3]: '>>> Name: A <<<'

In [4]: d2.get_text('A')
Out[4]: '>>> Name: A <<<'

In [5]: d1.get_text.__name__
Out[5]: 'func_wrapper'

In [6]: d2.get_text.__name__
Out[6]: 'get_text'

In [7]: d1.get_text.__doc__
Out[7]: 'Perform outer functionality wrapping core functionality'

In [8]: d2.get_text.__doc__
Out[8]: 'Perform core functionality'

```

`wraps` is wrapper for [`functools.update_wrapper`](https://docs.python.org/3.5/library/functools.html?highlight=functools.wraps#functools.update_wrapper), which "updates a wrapper function to look like the wrapped function." Here "look like" means updating a number of different module-level constants in addition to the `__name__` and `__doc__` attributes.

[end]
