# =====================================================================================================================
# VERSION = (0, 0, 1)   # use import EXACT_OBJECTS! not *
#   from .main import *                 # INcorrect
#   from .main import EXACT_OBJECTS     # CORRECT


# =====================================================================================================================
# TEMPLATE
# from .main import (
#     # BASE
#     EXACT_OBJECTS,
#
#     # AUX
#
#     # TYPES
#
#     # EXX
# )
# ---------------------------------------------------------------------------------------------------------------------
from .cmp import (
    # BASE
    CmpInst,
    # AUX
    # TYPES
    # EXX
)
from .number import (
    # BASE
    NumberArithmTranslateToAttr,
    # AUX
    # TYPES
    TYPE__NUMBER,
    # EXX
    Exx__NumberArithm_NoName,
)
# ---------------------------------------------------------------------------------------------------------------------
from .getattr_0_echo import (
    # BASE
    GetattrEcho,
    GetattrEchoSpace,
    # AUX
    # TYPES
    # EXX
)
from .getattr_1_aux import (
    # BASE
    GetattrAux,
    # AUX
    # TYPES
    # EXX
)
from .getattr_2_anycase import (
    # BASE
    GetattrAnycase,
    # AUX
    # TYPES
    # EXX
)
from .getattr_3_prefix import (
    # BASE
    GetattrPrefixInst,
    GetattrPrefixInst_RaiseIf,
    # AUX
    GetattrPrefixCls_MetaTemplate,
    # TYPES
    # EXX
    Exx__GetattrPrefix,
    Exx__GetattrPrefix_RaiseIf,
)

# ---------------------------------------------------------------------------------------------------------------------
from .middle_group import (
    # BASE
    ClsMiddleGroup,
    # AUX
    # TYPES
    # EXX
)


# =====================================================================================================================
