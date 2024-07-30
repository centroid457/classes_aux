from typing import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from classes_aux import *


# =====================================================================================================================
class Victim(CmpInst):
    def __init__(self, val):
        self.VAL = val

    def __len__(self):
        try:
            return len(self.VAL)
        except:
            pass

        return int(self.VAL)

    def __cmp__(self, other):
        other = self.__class__(other)

        # equel ----------------------
        if len(self) == len(other):
            return 0

        # final ------------
        return int(len(self) > len(other)) or -1


# =====================================================================================================================
class Test__Cmp:
    # @classmethod
    # def setup_class(cls):
    #     pass
    #     cls.Victim = Victim
    # @classmethod
    # def teardown_class(cls):
    #     pass
    #
    # def setup_method(self, method):
    #     pass
    #
    # def teardown_method(self, method):
    #     pass

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="expr",
        argvalues=[
            # INT ----------------
            Victim(1) == 1,
            Victim(1) != 11,

            Victim(1) < 2,
            Victim(1) <= 2,
            Victim(1) <= 1,

            Victim(1) > 0,
            Victim(1) >= 0,
            Victim(1) >= 1,

            # STR ----------------
            Victim("a") == "a",
            Victim("a") == "b",
            Victim("a") == 1,
            Victim("aa") > 1,
        ]
    )
    def test__inst__cmp__eq(self, expr):
        pytest_func_tester__no_args_kwargs(expr)

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="expr, _EXPECTED",
        argvalues=[
            (Victim(0).ltgt(1, 3), False),
            (Victim(1).ltgt(1, 3), False),
            (Victim(2).ltgt(1, 3), True),
            (Victim(3).ltgt(1, 3), False),
            (Victim(4).ltgt(1, 3), False),

            (Victim(0).ltge(1, 3), False),
            (Victim(1).ltge(1, 3), False),
            (Victim(2).ltge(1, 3), True),
            (Victim(3).ltge(1, 3), True),
            (Victim(4).ltge(1, 3), False),

            (Victim(0).legt(1, 3), False),
            (Victim(1).legt(1, 3), True),
            (Victim(2).legt(1, 3), True),
            (Victim(3).legt(1, 3), False),
            (Victim(4).legt(1, 3), False),

            (Victim(0).lege(1, 3), False),
            (Victim(1).lege(1, 3), True),
            (Victim(2).lege(1, 3), True),
            (Victim(3).lege(1, 3), True),
            (Victim(4).lege(1, 3), False),
        ]
    )
    def test__inst__cmp__lg(self, expr, _EXPECTED):
        pytest_func_tester__no_args_kwargs(expr, _EXPECTED)


# =====================================================================================================================

