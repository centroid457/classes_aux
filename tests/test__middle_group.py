from typing import *
import pathlib
import pytest
from pytest import mark
from pytest_aux import *
from classes_aux import *


# =====================================================================================================================
class Victim(ClsMiddleGroup):
    pass


class Victim1(ClsMiddleGroup):
    MIDDLE_GROUP__NAME = "name1"


class Victim2(ClsMiddleGroup):
    MIDDLE_GROUP__NAME = "name2"


class VictimAttr1(ClsMiddleGroup):
    attr = 1

class VictimAttr1Cmp(VictimAttr1):
    MIDDLE_GROUP__CMP_ATTR = "attr"


class VictimAttr1CmpAttr2(VictimAttr1Cmp):
    attr = 2


class VictimAttr1CmpAttr2_TryBreak(VictimAttr1CmpAttr2):
    MIDDLE_GROUP__CMP_ATTR = "tryBreak"


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="obj, other, _EXPECTED",
    argvalues=[
        (Victim, True, None),
        (Victim(), True, None),
        (Victim, 1, None),
        (Victim(), 1, None),
        (Victim, bool, None),
        (Victim(), bool, None),

        (Victim, Victim, True),
        (Victim, Victim(), True),
        (Victim, Victim1, False),
        (Victim, Victim1(), False),

        # VictimAttr1
        (Victim, VictimAttr1, True),
        (Victim, VictimAttr1Cmp, False),

        (VictimAttr1, VictimAttr1CmpAttr2, False),

        (VictimAttr1Cmp, VictimAttr1, True),
        (VictimAttr1Cmp, VictimAttr1CmpAttr2, False),

        (VictimAttr1CmpAttr2_TryBreak, VictimAttr1CmpAttr2, True),
    ]
)
def test__victim__check_equal(obj, other, _EXPECTED):
    func_link = lambda: obj.middle_group__check_equal__cls(other)
    pytest_func_tester__no_args_kwargs(func_link, _EXPECTED)


# =====================================================================================================================
