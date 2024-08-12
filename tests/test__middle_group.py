from typing import *
import pathlib
import pytest
from pytest import mark
from pytest_aux import *
from classes_aux import *


# =====================================================================================================================
class Victim(ClsMiddleGroup):
    pass


class Victim10(ClsMiddleGroup):
    MIDDLE_GROUP__NAME = "name1"
    pass


class Victim20(ClsMiddleGroup):
    MIDDLE_GROUP__NAME = "name2"
    pass


class VictimMeth(ClsMiddleGroup):
    def meth_cmp(self):
        pass
    pass


class VictimMethCmp(VictimMeth):
    MIDDLE_GROUP__CMP_METH = "meth_cmp"


class VictimMethCmpMeth(VictimMethCmp):
    def meth_cmp(self):
        pass


class VictimMethCmpMeth_TryBreak(VictimMethCmpMeth):
    MIDDLE_GROUP__CMP_METH = "meth_cmp222"


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="obj, other, _EXPECTED",
    argvalues=[
        (Victim, True, None),
        (Victim, 1, None),
        (Victim, bool, None),

        (Victim, Victim, True),
        (Victim, Victim(), True),
        (Victim, Victim10, False),
        (Victim, Victim10(), False),

        # VictimMeth
        (Victim, VictimMeth, True),
        (Victim(), VictimMeth, True),
        (Victim(), VictimMeth(), True),
        (Victim, VictimMeth(), True),

        (Victim, VictimMethCmp, False),
        (Victim(), VictimMeth, True),
        (Victim(), VictimMeth(), True),
        (Victim, VictimMeth(), True),

        (VictimMeth, VictimMethCmpMeth, False),
        (VictimMeth, VictimMethCmpMeth(), False),
        (VictimMethCmp, VictimMethCmpMeth, False),
        (VictimMethCmp, VictimMethCmpMeth(), False),

        (VictimMethCmpMeth_TryBreak, VictimMethCmpMeth(), True),
    ]
)
def test__victim__check_equal(obj, other, _EXPECTED):
    func_link = lambda: obj.middle_group__check_equal(other)
    pytest_func_tester__no_args_kwargs(func_link, _EXPECTED)


# =====================================================================================================================
