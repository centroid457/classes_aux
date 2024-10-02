# FIXME: need to deprecate! see next

from typing import *
from object_info import *
from funcs_aux import *


# =====================================================================================================================
class ClsMiddleGroup:
    """
    NOTE: DONT to deprecate!
    ------------------------
    1. comparing direct methods on objects will not work!!!
        -------------------------
            class Cls:
                def meth(self):
                    pass
                @classmethod
                def cmeth(cls):
                    pass

            class Cls2(Cls):
                pass

            print(Cls.meth == Cls2.meth)        # True
            print(Cls().meth == Cls2().meth)    # false
            print(Cls().cmeth == Cls2().cmeth)  # false
        -------------------------

    2. and even cmp classes - will not work!
        -------------------------
            class Cls:
                def meth(self):
                    pass
                @classmethod
                def cmeth(cls):
                    pass

            class Cls2(Cls):
                pass

            print(Cls.meth is Cls2.meth)
            print(Cls.meth == Cls2.meth)
            print(Cls.cmeth is Cls2.cmeth)
            print(Cls.cmeth == Cls2.cmeth)

            print(Cls.meth)
            print(Cls2.meth)
            print(Cls.cmeth)
            print(Cls2.cmeth)

            #
            True
            True
            False
            False
            <function Cls.meth at 0x000002CC6B525940>
            <function Cls.meth at 0x000002CC6B525940>
            <bound method Cls.cmeth of <class '__main__.Cls'>>
            <bound method Cls.cmeth of <class '__main__.Cls2'>>
        -------------------------

    GOAL
    ----
    if you need to separate cls/inst into several groups by middle nested class.
    main idea is manipulating with grouped methods, not just name in attribute.

    USAGE
    -----
    1. create some middle classes which will define groups.
    2. apply group methods and mention it in MIDDLE_GROUP__CMP_ATTR so objects could be compared not just by names!
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
    but you could forget using MIDDLE_GROUP__CMP_ATTR and exists incorrect cases.

    1. NAME/str attribute as base (always checks first) - MIDDLE_GROUP__NAME
        class Group1(ClsMiddleGroup):
            MIDDLE_GROUP__NAME = "Group1"
            def meth(self):
                pass

        class Group2(ClsMiddleGroup):
            MIDDLE_GROUP__NAME = "Group2"
            def meth(self):
                return True

    2. by other methods in addition - MIDDLE_GROUP__CMP_ATTR
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
    MIDDLE_GROUP__CMP_ATTR: TYPE__ARGS = None       # additional cmp parameters

    @classmethod
    def middle_group__check_equal__cls(cls, other: Any) -> bool | None:
        """
        middle groups could be cmp only by this method!
        """
        if not TypeChecker.check__nested__by_cls_or_inst(other, ClsMiddleGroup):
            return

        other = ensure_class(other)

        # CMP not only by just one name!!! need cmp by equity special methods!
        if cls.MIDDLE_GROUP__NAME != other.MIDDLE_GROUP__NAME:
            return False

        attrs = []
        if cls.MIDDLE_GROUP__CMP_ATTR:
            attrs1 = args__ensure_tuple(cls.MIDDLE_GROUP__CMP_ATTR)
            attrs.extend(attrs1)

        if other.MIDDLE_GROUP__CMP_ATTR:
            attrs2 = args__ensure_tuple(other.MIDDLE_GROUP__CMP_ATTR)
            attrs.extend(attrs2)

        # cmp ------------------
        for attr in attrs:
            try:
                getattr1 = getattr(cls, attr, None)
                getattr2 = getattr(other, attr, None)
                if getattr1 != getattr2:
                    return False
            except:
                return False

        return True

    def middle_group__check_equal__inst(self, other: Any) -> bool | None:
        pass

    # -----------------------------------------------------------------------------------------------------------------
    # EXAMPLE for TCS
    # def startup__group(self):
    #     pass
    # def teardown__group(self):
    #     pass


# =====================================================================================================================
