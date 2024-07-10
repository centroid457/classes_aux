from typing import *
from object_info import *
import math


# =====================================================================================================================
TYPE__NUMBER = int | float


class Exx__NumberArithm_NoName(Exception):
    pass


# =====================================================================================================================
class NumberArithm:
    """
    TODO: DECIDE
    ------------
    return number or reinited object???

    """
    # SETTINGS --------------------------------------------------------------------------------------------------------
    NUMBER_ARITHM__GETATTR_NAME: str = None     # DEFINE!!! name for ORIGINALVALUE

    # AUX -------------------------------------------------------------------------------------------------------------
    @property
    def NUMBER_ARITHM(self) -> Union[TYPE__NUMBER, NoReturn]:
        if not self.NUMBER_ARITHM__GETATTR_NAME:
            raise Exx__NumberArithm_NoName()

        result = getattr(self, self.NUMBER_ARITHM__GETATTR_NAME)
        if TypeChecker.check__func_or_meth(result):
            result = result()
        return result

    @NUMBER_ARITHM.setter
    def NUMBER_ARITHM(self, other) -> None | NoReturn:
        if not self.NUMBER_ARITHM__GETATTR_NAME:
            raise Exx__NumberArithm_NoName()
        setattr(self, self.NUMBER_ARITHM__GETATTR_NAME, other)

    # CONVERT ---------------------------------------------------------------------------------------------------------
    def __int__(self) -> TYPE__NUMBER:
        return int(self.NUMBER_ARITHM)

    def __float__(self) -> TYPE__NUMBER:
        return float(self.NUMBER_ARITHM)

    # SIGN ------------------------------------------------------------------------------------------------------------
    def __pos__(self) -> TYPE__NUMBER:
        """
        для унарного плюса (+some_object)
        """
        return self.NUMBER_ARITHM

    def __neg__(self) -> TYPE__NUMBER:
        """
        для унарного минуса (-some_object)
        """
        return -self.NUMBER_ARITHM

    def __abs__(self) -> TYPE__NUMBER:
        # return self.__class__(abs(self.NUMBER_ARITHM))
        return abs(self.NUMBER_ARITHM)

    # PARTS -----------------------------------------------------------------------------------------------------------
    def __round__(self, n=None) -> TYPE__NUMBER:
        return round(self.NUMBER_ARITHM, n)

    def __floor__(self) -> TYPE__NUMBER:
        return math.floor(self.NUMBER_ARITHM)

    def __ceil__(self) -> TYPE__NUMBER:
        return math.ceil(self.NUMBER_ARITHM)

    def __trunc__(self) -> TYPE__NUMBER:
        return math.trunc(self.NUMBER_ARITHM)

    # ARITHM ----------------------------------------------------------------------------------------------------------
    def __add__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM + other

    def __sub__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM - other

    def __mul__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM * other

    # def __div__(self, other) -> TYPE__NUMBER:   # THERE IS NO SUCH MAGICMETH!!! use truediv!
    #     return self.NUMBER_ARITHM/other

    def __truediv__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM / other

    def __floordiv__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM // other

    def __mod__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM % other

    def __divmod__(self, other) -> tuple[int, int | float]:
        return divmod(self.NUMBER_ARITHM, other)

    def __pow__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM ** other

    # INLINE ----------------------------------------------------------------------------------------------------------
    def __iadd__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM + other

    def __isub__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM - other

    def __imul__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM * other

    def __itruediv__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM / other

    def __ifloordiv__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM // other

    def __imod__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM % other

    def __ipow__(self, other) -> TYPE__NUMBER:
        return self.NUMBER_ARITHM ** other


# =====================================================================================================================
