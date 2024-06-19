import os
import time

import pytest
import pathlib
import shutil
from tempfile import TemporaryDirectory
from typing import *
from configparser import ConfigParser

from pytest_aux import *
from classes_aux import *


# =====================================================================================================================
class Victim(GetattrPrefixInst_RaiseIf):
    TRUE = True
    FALSE = False
    NONE = None

    def meth(self, value: Any):
        return value


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        (None, None),
        (True, None),
        ("", None),
        (" TRUE", None),

        ("TRUE", "TRUE"),
        ("True", "TRUE"),
        ("true", "TRUE"),

        ("meth", "meth"),
    ]
)
def test___attr_name__get_original(args, _EXPECTED):
    func_link = Victim()._attr_name__get_original
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# =====================================================================================================================
def test__register():
    # --------------------------------
    assert Victim().TRUE is True

    try:
        assert Victim().true is True
    except AttributeError:
        pass
    else:
        assert False

    # --------------------------------
    try:
        Victim().raise_if__true()
    except Exx__GetattrPrefix_RaiseIf:
        pass
    else:
        assert False
    try:
        Victim().raise_if__TRUE()
    except Exx__GetattrPrefix_RaiseIf:
        pass
    else:
        assert False
    try:
        Victim().RAISE_IF__TRUE()
    except Exx__GetattrPrefix_RaiseIf:
        pass
    else:
        assert False

    # --------------------------------
    assert Victim().raise_if_not__TRUE() is None
    assert Victim().raise_if_not__true() is None
    assert Victim().RAISE_IF_NOT__TRUE() is None


# =====================================================================================================================
def test__attr__not_exists():
    # TRUE ---------------------
    try:
        Victim().raise_if__HELLO()
    except AttributeError:
        pass
    else:
        assert False


# ---------------------------------------------------------------------------------------------------------------------
def test__attr__static():
    # TRUE ---------------------
    assert Victim().TRUE is True

    try:
        Victim().raise_if__TRUE()
    except Exx__GetattrPrefix_RaiseIf:
        pass
    else:
        assert False
    assert Victim().raise_if_not__TRUE() is None
    assert Victim().raise_if_not__true() is None
    assert Victim().RAISE_IF_NOT__TRUE() is None

    # FALSE ---------------------
    assert Victim().FALSE is False

    try:
        Victim().raise_if_not__FALSE()
    except Exx__GetattrPrefix_RaiseIf:
        pass
    else:
        assert False
    assert Victim().raise_if__FALSE() is None

    # NONE ---------------------
    assert Victim().NONE is None

    try:
        Victim().raise_if_not__NONE()
    except Exx__GetattrPrefix_RaiseIf:
        pass
    else:
        assert False
    assert Victim().raise_if__NONE() is None


# =====================================================================================================================
def test__METH():
    # TRUE ---------------------
    assert Victim().TRUE is True



















# =====================================================================================================================

