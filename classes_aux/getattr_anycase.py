from typing import *
from .getattr_aux import GetattrAux


# =====================================================================================================================
class GetattrAnycase(GetattrAux):
    def __getattr__(self, item: str) -> Any | NoReturn:
        return self._attr_anycase__get_value(item, self)


# =====================================================================================================================
