from typing import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from classes_aux import *


# =====================================================================================================================
class Victim(NumberArithm):
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

        assert victim + 1 == 2

        victim += 1
        assert victim == 2


# =====================================================================================================================

