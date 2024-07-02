from typing import *
import pathlib

import pytest
from pytest import mark
from pytest_aux import *

from classes_aux import *


# =====================================================================================================================


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
        argnames="variant",
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
    def test__inst__cmp__eq(self, variant):
        pytest_func_tester__no_args_kwargs(variant)


# =====================================================================================================================

