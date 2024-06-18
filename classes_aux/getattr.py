import pathlib
from typing import *
from object_info import *


# =====================================================================================================================
class Exx__GetattrRaiseIf(Exception):
    pass


# =====================================================================================================================
class ClsGetattrInst:
    # SETTINGS ----------------------
    _EXX__GETATTR_RAISE_IF: Type[Exception] = Exx__GetattrRaiseIf
    _GETATTR_MARKERS__INST: list[str] = ["raise_if__", "raise_if_not__"]

    def __getattr__(self, item: str):
        meth_name = None
        for marker in self._GETATTR_MARKERS__INST:
            if item.lower().startswith(marker.lower()):
                meth_name = item[len(marker):]
                break

        if not meth_name or meth_name not in dir(self):
            raise AttributeError(item)

        return lambda *args, **kwargs: getattr(self, marker)(meth_name=meth_name, args=args, kwargs=kwargs)

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
            raise self._EXX__GETATTR_RAISE_IF(f"[raise_if__]met conditions {args=}/{kwargs=}")

    def raise_if_not__(self, meth_name: str, args: tuple | None = None, kwargs: dict | None = None) -> None | NoReturn:
        return self.raise_if__(meth_name=meth_name, args=args, kwargs=kwargs, _reverse=True)


# =====================================================================================================================
