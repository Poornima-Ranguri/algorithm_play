from functools import wraps

def decorate(func):
    """Provide decorating function wrapper"""
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        """Perform outer functionality wrapping core functionality"""
        return '>>> {} <<<'.format(func(*args, **kwargs))
    return func_wrapper

@decorate
def get_text(name):
    """Perform core functionality"""
    return 'Name: {}'.format(name)
