import pathlib
from typing import *
from object_info import *


# =====================================================================================================================
class Exx__GetattrPrefix(Exception):
    pass


class Exx__GetattrPrefix_RaiseIf(Exx__GetattrPrefix):
    pass


# =====================================================================================================================
class GetattrPrefixInst:
    # SETTINGS ----------------------
    _EXX__GETATTR: Type[Exx__GetattrPrefix] = Exx__GetattrPrefix
    _GETATTR_MARKERS__INST: list[str] = []

    def __getattr__(self, item: str):
        meth_name = None
        for marker in self._GETATTR_MARKERS__INST:
            if item.lower().startswith(marker.lower()):
                meth_name = item[len(marker):]
                break

        if not meth_name or meth_name not in dir(self):
            raise AttributeError(item)

        return lambda *args, **kwargs: getattr(self, marker)(meth_name=meth_name, args=args, kwargs=kwargs)


# =====================================================================================================================
class GetattrPrefixInst_RaiseIf(GetattrPrefixInst):
    """
    RULES
    -----
    CaseSense
        1. you should use MARKERS in same register as corresponding methods!
        2. but apply on instance in any variant!
    """
    _EXX__GETATTR = Exx__GetattrPrefix_RaiseIf
    _GETATTR_MARKERS__INST = ["raise_if__", "raise_if_not__"]

    # ---------------------------------------
    # if you need add some new - create same using this as template!
    def raise_if__(self, meth_name: str, args: tuple | None = None, kwargs: dict | None = None, _reverse: bool | None = None) -> None | NoReturn:
        args = args or ()
        kwargs = kwargs or {}
        _reverse = _reverse or False
        meth = getattr(self, meth_name)
        if TypeChecker.check__func_or_meth(meth):
            result = meth(*args, **kwargs)
        else:
            result = meth
        if bool(result) != bool(_reverse):
            raise self._EXX__GETATTR(f"[raise_if__]met conditions {args=}/{kwargs=}")

    def raise_if_not__(self, meth_name: str, args: tuple | None = None, kwargs: dict | None = None) -> None | NoReturn:
        return self.raise_if__(meth_name=meth_name, args=args, kwargs=kwargs, _reverse=True)


# =====================================================================================================================
