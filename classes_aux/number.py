from typing import *
from object_info import *
import math


# =====================================================================================================================
TYPE__NUMBER = int | float


class Exx__NumberArithm_NoName(Exception):
    pass


# =====================================================================================================================
class NumberArithmTranslateToAttr:
    """
    GOAL
    ----
    translate all arithmetic functions to exact attribute! always return Self (except direct int/float transform methods).
    So if you need exact NUMBER - just apply int/float()
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
    def __int__(self) -> int:
        return int(self.NUMBER_ARITHM)

    def __float__(self) -> float:
        return float(self.NUMBER_ARITHM)

    # SIGN ------------------------------------------------------------------------------------------------------------
    def __pos__(self) -> Self:
        """
        для унарного плюса (+some_object)
        """
        return self

    def __neg__(self) -> Self:
        """
        для унарного минуса (-some_object)
        """
        self.NUMBER_ARITHM = - self.NUMBER_ARITHM
        return self

    def __abs__(self) -> Self:
        self.NUMBER_ARITHM = abs(self.NUMBER_ARITHM)
        return self

    # PARTS -----------------------------------------------------------------------------------------------------------
    def __round__(self, n=None) -> Self:
        self.NUMBER_ARITHM = round(self.NUMBER_ARITHM, n)
        return self

    def __floor__(self) -> Self:
        self.NUMBER_ARITHM = math.floor(self.NUMBER_ARITHM)
        return self

    def __ceil__(self) -> Self:
        self.NUMBER_ARITHM = math.ceil(self.NUMBER_ARITHM)
        return self

    def __trunc__(self) -> Self:
        self.NUMBER_ARITHM = math.trunc(self.NUMBER_ARITHM)
        return self

    # ARITHM ----------------------------------------------------------------------------------------------------------
    def __add__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM + float(other)
        return self

    def __sub__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM - float(other)
        return self

    def __mul__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM * float(other)
        return self

    # def __div__(self, other) -> Self:   # THERE IS NO SUCH MAGICMETH!!! use truediv!
    #     return self.NUMBER_ARITHM/other
    #     return self

    def __truediv__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM / float(other)
        return self

    def __floordiv__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM // float(other)
        return self

    def __mod__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM % float(other)
        return self

    def __divmod__(self, other) -> tuple[int, int | float]:
        return divmod(self.NUMBER_ARITHM, other)

    def __pow__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM ** float(other)
        return self

    # INLINE ----------------------------------------------------------------------------------------------------------
    def __iadd__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM + float(other)
        return self

    def __isub__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM - float(other)
        return self

    def __imul__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM * float(other)
        return self

    def __itruediv__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM / float(other)
        return self

    def __ifloordiv__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM // float(other)
        return self

    def __imod__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM % float(other)
        return self

    def __ipow__(self, other) -> Self:
        self.NUMBER_ARITHM = self.NUMBER_ARITHM ** float(other)
        return self


# =====================================================================================================================
