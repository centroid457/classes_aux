from typing import *
from object_info import *
from funcs_aux import *

from .getattr_1_aux import GetattrAux
from funcs_aux.valid_aux import ValidAux


# =====================================================================================================================
class Exx__GetattrPrefix(Exception):
    pass


class Exx__GetattrPrefix_RaiseIf(Exx__GetattrPrefix):
    pass


# =====================================================================================================================
class GetattrPrefixInst(GetattrAux):
    _GETATTR__PREFIXES: list[str] = []

    def __getattr__(self, item: str) -> Any | Callable | NoReturn:
        """
        NOTE
        ----
        all args/kwargs goes for value! not for the prefix!
        prefix - callable with just one first parameter as catching value (may be callable) and other params used directly only for prefix
        """
        for prefix in self._GETATTR__PREFIXES:
            prefix_original = self._attr_anycase__get_name(prefix, self)
            if not prefix_original:
                continue
            prefix_meth = getattr(self, prefix_original)

            if item.lower() == prefix.lower():
                return lambda *args, **kwargs: ValidAux.get_result(source=prefix_meth, args=args, kwargs=kwargs)

            if prefix_original and item.lower().startswith(prefix.lower()):
                item = item[len(prefix):]
                item_value = self._attr_anycase__get_value(item, self)

                return lambda *args, **kwargs: ValidAux.get_result(source=prefix_meth, args=[ValidAux.get_result(source=item_value, args=args, kwargs=kwargs), ])
            # TODO: maybe need to add prefix_kwargs???? for _comments for example? but how...

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
    _GETATTR__PREFIXES = ["raise_if__", "raise_if_not__"]

    # ---------------------------------------
    # if you need add some new - create same using this as template!
    def raise_if__(self, source: Any, _reverse: bool | None = None) -> None | NoReturn:
        _reverse = _reverse or False
        result = ValidAux.get_result_or_exx(source=source)
        if TypeChecker.check__exception(result) or bool(result) != bool(_reverse):
            raise Exx__GetattrPrefix_RaiseIf(f"[raise_if__{_reverse=}]met conditions {source=}")

    def raise_if_not__(self, source: Any) -> None | NoReturn:
        return self.raise_if__(source=source, _reverse=True)


# =====================================================================================================================
class GetattrPrefixCls_MetaTemplate(type):
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

    # TODO: add tests!
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
