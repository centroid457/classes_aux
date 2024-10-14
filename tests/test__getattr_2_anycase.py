from typing import *

import pytest
from pytest import mark
from pytest_aux import *
from classes_aux import *


# =====================================================================================================================
class Victim(GetattrAnycase):
    attr_lowercase = "value"
    ATTR_UPPERCASE = "VALUE"
    Attr_CamelCase = "Value"


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="attr, _EXPECTED",
    argvalues=[
        (None, Exception),
        (True, Exception),
        ("", Exception),
        (" TRUE", Exception),

        ("attr_lowercase", "value"),
        ("ATTR_LOWERCASE", "value"),

        ("ATTR_UPPERCASE", "VALUE"),
        ("attr_uppercase", "VALUE"),
    ]
)
def test__value(attr, _EXPECTED):
    args = (Victim(), attr)
    func_link = getattr
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# =====================================================================================================================
