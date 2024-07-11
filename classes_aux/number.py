from typing import *
from object_info import *
import math
from classes_aux import CmpInst


# =====================================================================================================================
TYPE__NUMBER = int | float


class Exx__NumberArithm_NoName(Exception):
    pass


# =====================================================================================================================
class NumberArithmTranslateToAttr(CmpInst):
    """
    GOAL
    ----
    translate all arithmetic operations to exact attribute (expected as number)!

    NOTE
    ----
    MAINLY fom the beginning:
    always return Self for any operation (except direct int/float transform methods).
    So if you need exact NUMBER - just apply float() (int is incorrect!).

    MAYBE IN FUTURE:
    IF FUNC - return number, if operation - return Self.
    I'm not really know what is the best decision but in future it may be changed for real implementation

    CREATED SPECIALLY FOR
    ---------------------
    funcs_aux.Value_WithUnit and further ising in Uart Responses

    BEST USAGE
    ----------
    see tests!

    REFERENCE
    ---------
    https://docs.python.org/3/library/operator.html
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
    # MAIN --------------------------------------
    def __int__(self) -> int:
        return int(self.NUMBER_ARITHM)

    def __float__(self) -> float:
        return float(self.NUMBER_ARITHM)

    def __hash__(self) -> int:
        return hash(self.NUMBER_ARITHM)

    # OTHER --------------------------------------
    def __bool__(self) -> bool:
        return bool(self.NUMBER_ARITHM)

    def __str__(self) -> str:
        return str(self.NUMBER_ARITHM)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.NUMBER_ARITHM})"

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
        return divmod(self.NUMBER_ARITHM, float(other))

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

    # CMP -------------------------------------------------------------------------------------------------------------
    def __cmp__(self, other) -> int | NoReturn:
        """
        do try to resolve Exceptions!!! sometimes it is ok to get it!!!

        RETURN
        ------
            1=self>other
            0=self==other
            -1=self<other
        """
        if float(self.NUMBER_ARITHM) == float(other) or other == float(self.NUMBER_ARITHM):
            return 0
        if float(self.NUMBER_ARITHM) > float(other) or other < float(self.NUMBER_ARITHM):
            return 1
        if float(self.NUMBER_ARITHM) < float(other) or other > float(self.NUMBER_ARITHM):
            return -1


# =====================================================================================================================
