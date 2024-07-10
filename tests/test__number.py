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
    def test__exprs(self):
        victim = Victim(1)
        # ObjectInfo(victim).print()
        assert victim.VAL == 1

        victim = victim + 1
        assert victim.VAL == 2

        victim += 1
        assert victim.VAL == 3

        victim = -victim
        assert victim.VAL == -3


# =====================================================================================================================

