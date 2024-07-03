from typing import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from classes_aux import *


# =====================================================================================================================
class ClsMiddleGroup01(ClsMiddleGroup):
    pass


class ClsMiddleGroup02(ClsMiddleGroup):
    pass


class ClsMiddleGroup11(ClsMiddleGroup01):
    pass


# =====================================================================================================================
# GROUPS---------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        (True, False),
        (1, False),
        (bool, False),

        (ClsMiddleGroup, True),
        (ClsMiddleGroup(), True),
        (ClsMiddleGroup01, True),
        (ClsMiddleGroup01(), True),
        (ClsMiddleGroup02, True),
        (ClsMiddleGroup02(), True),
        (ClsMiddleGroup11, True),
        (ClsMiddleGroup11(), True),
    ]
)
def test__check_exists(args, _EXPECTED):
    func_link = ClsMiddleGroup.middle_group__check_exists
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# -----------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    argnames="args, _EXPECTED, _MARK",
    argvalues=[
        (True, AttributeError, None),
        (1, AttributeError, None),
        (bool, AttributeError, None),

        (ClsMiddleGroup, "ClsMiddleGroup", mark.xfail),         # DONT TRY TO USE DIRECT TO GROUP!
        (ClsMiddleGroup(), "ClsMiddleGroup", mark.xfail),
        (ClsMiddleGroup01, "ClsMiddleGroup01", mark.xfail),
        (ClsMiddleGroup01(), "ClsMiddleGroup01", mark.xfail),
        (ClsMiddleGroup02, "ClsMiddleGroup02", mark.xfail),
        (ClsMiddleGroup02(), "ClsMiddleGroup02", mark.xfail),
        (ClsMiddleGroup11, "ClsMiddleGroup11", mark.xfail),
        (ClsMiddleGroup11(), "ClsMiddleGroup11", mark.xfail),
    ]
)
def test__group__name_get(args, _EXPECTED, _MARK):
    func_link = lambda obj: obj.middle_group__get()
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED, _MARK)


# =====================================================================================================================
# VICTIM --------------------------------------------------------------------------------------------------------------
class Victim(ClsMiddleGroup):
    pass


class Victim01(ClsMiddleGroup01):
    pass


class Victim02(ClsMiddleGroup02):
    pass


class Victim11(ClsMiddleGroup11):
    pass


# ---------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    argnames="obj, _EXPECTED",
    argvalues=[
        (True, AttributeError),
        (1, AttributeError),
        (bool, AttributeError),

        (Victim, "ClsMiddleGroup"),
        (Victim(), "ClsMiddleGroup"),
        (Victim01, "ClsMiddleGroup01"),
        (Victim01(), "ClsMiddleGroup01"),
        (Victim02, "ClsMiddleGroup02"),
        (Victim02(), "ClsMiddleGroup02"),
        (Victim11, "ClsMiddleGroup11"),
        (Victim11(), "ClsMiddleGroup11"),
    ]
)
def test__victim__name_get(obj, _EXPECTED):
    func_link = lambda: obj.middle_group__get()
    pytest_func_tester__no_args_kwargs(func_link, _EXPECTED)


# ---------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    argnames="obj, other, _EXPECTED",
    argvalues=[
        (Victim, True, None),
        (Victim, 1, None),
        (Victim, bool, None),

        (Victim, Victim, True),
        (Victim, Victim(), True),
        (Victim, Victim01, False),
        (Victim, Victim01(), False),
        (Victim, Victim02, False),
        (Victim, Victim02(), False),
        (Victim, Victim11, False),
        (Victim, Victim11(), False),
    ]
)
def test__victim__check_equal(obj, other, _EXPECTED):
    func_link = lambda: obj.middle_group__check_equal(other)
    pytest_func_tester__no_args_kwargs(func_link, _EXPECTED)


# =====================================================================================================================
