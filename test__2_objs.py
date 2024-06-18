from typing import *
import pytest

import pathlib
import shutil
from tempfile import TemporaryDirectory
from configparser import ConfigParser
from pytest_aux import *


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS SOURCE!!!
from classes_aux import *


# =====================================================================================================================
class Test__888888888888:
    Victim: Type[NEW_CLASS____]
    victim: NEW_CLASS____

    @classmethod
    def setup_class(cls):
        pass
        cls.Victim = type("VICTIM", (NEW_CLASS____,), {})

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    # -----------------------------------------------------------------------------------------------------------------
    def test__1_direct(self):
        assert True

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (("1",), 1),
            (("hello",), Exception),
        ]
    )
    def test__2_parametrized_by_one_func(self, args, _EXPECTED):
        func_link = int
        pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)
        
    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(argnames="func_link", argvalues=[int, bool, ])
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (("1",), 1),
            (("hello",), Exception),
        ]
    )
    def test__3_parametrized_by_several_funcs(self, func_link, args, _EXPECTED):
        pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# =====================================================================================================================
