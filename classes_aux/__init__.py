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

from .getattr import (
    # BASE
    GetattrPrefixInst,
    GetattrPrefixInst_RaiseIf,

    # AUX
    GetattrCls_Meta__Template,

    # TYPES

    # EXX
    Exx__GetattrPrefix,
    Exx__GetattrPrefix_RaiseIf,
)


# =====================================================================================================================
