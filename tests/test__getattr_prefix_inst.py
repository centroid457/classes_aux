from typing import *

import pytest
from pytest import mark
from pytest_aux import *
from classes_aux import *


# =====================================================================================================================
class Victim(GetattrPrefixInst):
    _GETATTR__PREFIXES = ["bool__", ]
    TRUE = True
    NONE = None

    def bool__(self, value: Any = None) -> bool | NoReturn:
        return bool(value)

    def meth_true(self):
        return True

    def meth_echo(self, value):
        return value


victim = Victim()


# =====================================================================================================================
def test__direct():
    assert victim.bool__() == False
    assert victim.bool__(True) == True

    assert victim.bool__true() == True
    assert victim.bool__meth_true() == True

    try:
        victim.bool__meth_echo()
        assert False
    except:
        assert True

    assert victim.bool__meth_echo(1) == True
    assert victim.bool__meth_echo(0) == False
    assert victim.bool__meth_echo(True) == True
    assert victim.bool__meth_echo(False) == False


@pytest.mark.parametrize(
    argnames="meth, args, _EXPECTED",
    argvalues=[
        ("bool__", (),  False),
        ("BOOL__", (), False),

        ("bool11__true111", (), Exception),
        ("bool__true111", (), Exception),
        ("bool__true", (), True),
        ("BOOL__TRUE", (), True),
        ("BOOL__NONE", (), False),

        ("BOOL__meth_true", (), True),
        ("BOOL__meth_true", (123, ), Exception),

        ("BOOL__meth_echo", (), Exception),
        ("BOOL__meth_echo", (1, ), True),
        ("BOOL__meth_echo", ("123", ), True),

    ]
)
def test__1(meth, args, _EXPECTED):
    func = lambda *_args: getattr(victim, meth)(*_args)
    pytest_func_tester__no_kwargs(func, args, _EXPECTED)


# =====================================================================================================================
