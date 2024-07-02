from typing import *
from object_info import *


# =====================================================================================================================
class ClsMiddleGroup_Base:
    """
    if you need to separate instances into several groups.

    USAGE
    -----
    create some middle classes which will define groups.


    CREATED SPECIALLY FOR
    ---------------------
    module testplans.
    need to handle testcase classes as some groups!
    there was not enough separating process just by startup_cls and startup_inst!!!
    """
    @classmethod
    def middle_group_name__get(cls) -> str:
        for cls_i in cls.__mro__[1:]:
            if hasattr(cls_i, "middle_group_name__get"):
                return cls_i.__name__

    @classmethod
    def middle_group_name__check_equal(cls, other: Any) -> bool | None:
        if not hasattr(other, "middle_group_name__get"):
            return

        return cls.middle_group_name__get() == other.middle_group_name__get()


class ClsMiddleGroup(ClsMiddleGroup_Base):
    pass

class Cls0:
    pass

class Cls(Cls0, ClsMiddleGroup):
    pass


print(Cls().middle_group_name__get())


# =====================================================================================================================
