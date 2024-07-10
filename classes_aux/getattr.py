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
    _GETATTR__EXX: Type[Exx__GetattrPrefix] = Exx__GetattrPrefix
    _GETATTR__PREFIXES_INST: list[str] = []

    # BASE --------------------------
    def _attr_name__get_original(self, sample: str | None) -> str | None:
        """
        get attr name in original register
        """
        if not isinstance(sample, str):
            return
        for name in dir(self):
            if name.lower() == sample.lower():
                return name

    def __getattr__(self, item: str):
        for prefix in self._GETATTR__PREFIXES_INST:
            if item.lower().startswith(prefix.lower()):
                item = item[len(prefix):]

                name_original = self._attr_name__get_original(item)
                if name_original is None:
                    raise AttributeError(item)

                return lambda *args, **kwargs: getattr(self, prefix)(meth_name=name_original, args=args, kwargs=kwargs)

        raise AttributeError(item)


# =====================================================================================================================
class GetattrPrefixInst_RaiseIf(GetattrPrefixInst):
    """
    RULES
    -----
    You always need to CALL prefixed result! even if you access to not callable attribute!

    CaseSense
        1. you should use MARKERS in same register as corresponding methods!
        2. but apply on instance in any variant!
    """
    _GETATTR__EXX = Exx__GetattrPrefix_RaiseIf
    _GETATTR__PREFIXES_INST = ["raise_if__", "raise_if_not__"]

    # ---------------------------------------
    # if you need add some new - create same using this as template!
    def raise_if__(self, meth_name: str, args: tuple | None = None, kwargs: dict | None = None, _reverse: bool | None = None) -> None | NoReturn:
        args = args or ()
        kwargs = kwargs or {}
        _comment = None
        if "_comment" in kwargs:
            _comment = kwargs.pop("_comment")

        _reverse = _reverse or False
        meth = getattr(self, meth_name)
        if TypeChecker.check__func_or_meth(meth):
            result = meth(*args, **kwargs)
        else:
            result = meth
        if bool(result) != bool(_reverse):
            raise self._GETATTR__EXX(f"[raise_if__]met conditions {meth_name=}/{args=}/{kwargs=}//{_comment=}")

    def raise_if_not__(self, meth_name: str, args: tuple | None = None, kwargs: dict | None = None) -> None | NoReturn:
        return self.raise_if__(meth_name=meth_name, args=args, kwargs=kwargs, _reverse=True)


# =====================================================================================================================
class GetattrCls_Meta__Template(type):
    """
    NOTE
    ----
    THIS IS ONLY AS EXAMPLE!!! in any situation you need to create specific Meta-class!!!

    GOAL
    ----
    get attributes from CLASS! not instance!

    CREATED SPECIALLY FOR
    ---------------------
    the main goal

    BEST USAGE
    ----------
    for example usages see requirements_checker.ReqCheckStr_Base, annot_attrs. or here _GetattrCls_Meta__Echo

    """
    # dont change markers! use exists!
    _MARKER__BOOL_IF: str = "bool_if__"
    _MARKER__BOOL_IF_NOT: str = "bool_if_not__"
    _MARKER__RAISE_IF: str = "raise_if__"
    _MARKER__RAISE_IF_NOT: str = "raise_if_not__"

    def __getattr__(cls, item: str):
        """if no exists attr/meth
        """
        if item.lower().startswith(cls._MARKER__BOOL_IF.lower()):
            attr_name = item.lower().replace(cls._MARKER__BOOL_IF.lower(), "")
            return lambda: cls.check(values=attr_name, _raise=False, _reverse=False, _meet_true=False)
        elif item.lower().startswith(cls._MARKER__BOOL_IF_NOT.lower()):
            attr_name = item.lower().replace(cls._MARKER__BOOL_IF_NOT.lower(), "")
            return lambda: cls.check(values=attr_name, _raise=False, _reverse=True, _meet_true=False)

        elif item.lower().startswith(cls._MARKER__RAISE_IF.lower()):
            attr_name = item.lower().replace(cls._MARKER__RAISE_IF.lower(), "")
            return lambda: not cls.check(values=attr_name, _raise=True, _reverse=True, _meet_true=False) or None
        elif item.lower().startswith(cls._MARKER__RAISE_IF_NOT.lower()):
            attr_name = item.lower().replace(cls._MARKER__RAISE_IF_NOT.lower(), "")
            return lambda: not cls.check(values=attr_name, _raise=True, _reverse=False, _meet_true=False) or None

        else:
            msg = f"[ERROR] META:'{cls.__name__}' CLASS has no attribute '{item}'"
            raise AttributeError(msg)


# =====================================================================================================================
