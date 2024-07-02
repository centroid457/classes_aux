from typing import *
from object_info import *


# =====================================================================================================================
class ClsMiddleGroup:
    """
    if you need to separate instances into several groups.
    main ide is manipulating with grouped methods? not just to keep name in attribute.

    USAGE
    -----
    !. dont use this class as final! only middle!
    1. create some middle classes which will define groups.
    2. do nesting your final classes by Groups

    CREATED SPECIALLY FOR
    ---------------------
    module testplans.
    need to handle testcase classes as some groups!
    there was not enough separating process just by startup_cls and startup_inst!!!
    """

    @staticmethod
    def middle_group_name__check_exists(other: Any) -> bool:
        return hasattr(other, "middle_group_name__get")

    @classmethod
    def middle_group_name__get(cls) -> str:
        for cls_i in cls.__mro__[1:]:
            if hasattr(cls_i, "middle_group_name__get"):
                return cls_i.__name__

    @classmethod
    def middle_group_name__check_equal(cls, other: Any) -> bool | None:
        if not ClsMiddleGroup.middle_group_name__check_exists(other):
            return

        return cls.middle_group_name__get() == other.middle_group_name__get()

    # -----------------------------------------------------------------------------------------------------------------
    # EXAMPLE for TCS
    # def startup__group(self):
    #     pass
    # def teardown__group(self):
    #     pass


# =====================================================================================================================
