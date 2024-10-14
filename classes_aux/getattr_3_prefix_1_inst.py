from typing import *
from object_info import *

from funcs_aux.valid_aux import ValidAux
from .getattr_1_aux import GetattrAux


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
                return lambda *prefix_args, **prefix_kwargs: ValidAux.get_result(source=prefix_meth, args=prefix_args, kwargs=prefix_kwargs)

            if prefix_original and item.lower().startswith(prefix.lower()):
                item = item[len(prefix):]
                item_value = self._attr_anycase__get_value(item, self)

                return lambda *meth_args, **meth_kwargs: ValidAux.get_result(
                    source=prefix_meth,
                    args=[ValidAux.get_result(source=item_value, args=meth_args, kwargs={k:v for k,v in meth_kwargs.items() if k != "prefix_kwargs"}), ],
                    kwargs=meth_kwargs.get("prefix_kwargs") or {}
                )

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
    def raise_if__(self, source: Any, _reverse: bool | None = None, comment: str = "") -> None | NoReturn:
        _reverse = _reverse or False
        result = ValidAux.get_result_or_exx(source=source)
        if TypeChecker.check__exception(result) or bool(result) != bool(_reverse):
            raise Exx__GetattrPrefix_RaiseIf(f"[raise_if__/{_reverse=}]met conditions ({source=}/{comment=})")

    def raise_if_not__(self, source: Any, comment: str = "") -> None | NoReturn:
        return self.raise_if__(source=source, _reverse=True)


# =====================================================================================================================
