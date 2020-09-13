from inspect import signature, Signature
from typing import Callable, Any, Mapping
from collections import defaultdict
from functools import wraps

__all__ = ['overload']


overloaded: Mapping[str, Mapping[Signature, Callable]] = defaultdict(dict)


def overload(f: Callable):
    sig = signature(f)
    if any(int(par.kind) in (2, 4) for par in sig.parameters.values()):
        raise TypeError("cannot overload variable-length argument lists")
    overloaded[f.__name__][sig] = f

    @wraps(f)
    def wrapper(*args, **kwargs):
        all_args = args + tuple(kwargs.values())
        for sig, func in overloaded[f.__name__].items():
            if (len(all_args) == len(sig.parameters)
                and all(
                    par.annotation is Any
                    or par.annotation is par.empty
                    or (isinstance(arg, par.annotation)
                        for par, arg in zip(sig.parameters.values(), all_args))
            )):
                return func(*args, **kwargs)
        raise TypeError('No function with this signature exists')
    return wrapper
