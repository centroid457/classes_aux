from typing import *
from object_info import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from classes_aux import *


# =====================================================================================================================
class Victim(NumberArithmTranslateToAttr):
    NUMBER_ARITHM__GETATTR_NAME = "VAL"

    def __init__(self, val):
        self.VAL = val


# =====================================================================================================================
class Test__Number:
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
    def test__arithm(self):
        victim = Victim(1)
        # ObjectInfo(victim).print()
        assert victim.VAL == 1

        victim = victim + 1
        assert victim.VAL == 2

        victim += 1
        assert victim.VAL == 3

        victim = -victim
        assert victim.VAL == -3

    def test__cmp(self):
        assert Victim(1) == 1

        assert Victim(0.9) < 1
        assert Victim(0.9) > -1

        assert Victim(0.9) > 0.8
        assert Victim(-0.9) < 0.8

    def test__precision(self):
        assert Victim(0.001) == 0.001
        assert Victim(0.001) - 0.001 == 0
        assert round(Victim(0.001) - 0.0001, 3) == 0.001
        assert round(Victim(0.001) + 0.0001, 3) == 0.001
        assert round(Victim(0.001) + 0.0005, 3) == 0.002

    def test__str(self):
        assert str(Victim(1)) == "1"
        assert str(Victim(1.1)) == "1.1"
        assert str(Victim(1.1) + 0.1) == "1.2"
        assert str(Victim(1.111222) + 0.000111222) == "1.111333"

        assert str(Victim(0)) == "0"
        assert str(Victim(0.0)) == "0"

        assert str(Victim(0.000000111)) == "0"
        assert str(Victim(0.000002111)) == "0.000002"


# =====================================================================================================================
