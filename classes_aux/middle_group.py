# FIXME: need to deprecate! see next

from typing import *
from object_info import *
from funcs_aux import *


# =====================================================================================================================
class ClsMiddleGroup:
    """
    # FIXME: need to deprecate!
        consider to compare direct methods

    GOAL
    ----
    if you need to separate cls/inst into several groups by middle nested class.
    main idea is manipulating with grouped methods, not just name in attribute.

    USAGE
    -----
    1. create some middle classes which will define groups.
    2. apply group methods and mention it in MIDDLE_GROUP__CMP_METH so objects could be compared not just by names!
    3. do nesting your final classes by Groups

        # BEFORE --------------------------
        class YourClsBase:
            pass

        class Cls1(YourClsBase):
            GROUP__NAME = "Group1"
            def meth(self):
                pass

        class Cls2(YourClsBase):
            GROUP__NAME = "Group2"
            def meth(self):
                return True

        class Cls3(YourClsBase):
            GROUP__NAME = "Group2"
            def meth(self):
                return True

        # AFTER --------------------------
        class Group1(ClsMiddleGroup):
            MIDDLE_GROUP__NAME = "Group1"
            def meth(self):
                pass

        class Group2(ClsMiddleGroup):
            MIDDLE_GROUP__NAME = "Group2"
            def meth(self):
                return True

        class YourClsBase(ClsMiddleGroup):
            pass

        class Cls1(Group1, YourClsBase):
            pass

        class Cls2(Group2, YourClsBase):
            pass

        class Cls3(Group2, YourClsBase):
            pass


    TWO WAYS TO SEPARATE GROUPS
    NOTE: BEST WAY: use only *_CMP_METH! *_NAME useful for issues when you need to know exactly the group name!
    but you could forget using MIDDLE_GROUP__CMP_METH and exists incorrect cases.

    1. NAME/str attribute as base (always checks first) - MIDDLE_GROUP__NAME
        class Group1(ClsMiddleGroup):
            MIDDLE_GROUP__NAME = "Group1"
            def meth(self):
                pass

        class Group2(ClsMiddleGroup):
            MIDDLE_GROUP__NAME = "Group2"
            def meth(self):
                return True

    2. by other methods in addition - MIDDLE_GROUP__CMP_METH
        class GroupBase(ClsMiddleGroup):
            MIDDLE_GROUP__METH_CMP = "meth"
            MIDDLE_GROUP__METH_CMP = ["meth", "meth2"]

        class Group1(GroupBase):
            def meth(self):
                pass

        class Group2(GroupBase):
            def meth(self):
                return True

    CREATED SPECIALLY FOR
    ---------------------
    module testplans.
    need to handle testcase classes as some groups!
    there was not enough separating process just by startup_cls and startup_inst!!! need startup_group!
    """
    MIDDLE_GROUP__NAME: None | str = None           # main cmp meth
    MIDDLE_GROUP__CMP_METH: TYPE__ARGS = None       # additional cmp methods

    @classmethod
    def middle_group__check_equal(cls, other: Any) -> bool | None:
        """
        middle groups could be cmp only by this method!
        """
        if not TypeChecker.check__nested__by_cls_or_inst(other, ClsMiddleGroup):
            return

        # CMP not only by just one name!!! need cmp by equity special methods!
        result = cls.MIDDLE_GROUP__NAME == other.MIDDLE_GROUP__NAME
        if not result:
            return False

        if cls.MIDDLE_GROUP__CMP_METH or other.MIDDLE_GROUP__CMP_METH:
            # collect ------------------
            meths_cmp = []
            if cls.MIDDLE_GROUP__CMP_METH:
                meths_cmp1 = args__ensure_tuple(cls.MIDDLE_GROUP__CMP_METH)
                if meths_cmp1:
                    meths_cmp.extend(meths_cmp1)

            if other.MIDDLE_GROUP__CMP_METH:
                meths_cmp2 = args__ensure_tuple(other.MIDDLE_GROUP__CMP_METH)
                if meths_cmp2:
                    meths_cmp.extend(meths_cmp2)

            # cmp ------------------
            other = ensure_class(other)

            for meth_name in meths_cmp:
                hasattr1 = hasattr(cls, meth_name)
                hasattr2 = hasattr(other, meth_name)
                if not hasattr1 and not hasattr2:
                    continue

                try:
                    getattr1 = getattr(cls, meth_name)
                    getattr2 = getattr(other, meth_name)
                    result &= getattr1 == getattr2
                except:
                    result = False

                if not result:
                    return False

        return result

    # -----------------------------------------------------------------------------------------------------------------
    # EXAMPLE for TCS
    # def startup__group(self):
    #     pass
    # def teardown__group(self):
    #     pass


# =====================================================================================================================
