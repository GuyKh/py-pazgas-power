# This file contains common classes
from dataclasses import field

from mashumaro import DataClassDictMixin, field_options
from mashumaro.config import BaseConfig


class APIMRequest(DataClassDictMixin):
    """Base class for all APIm requests"""

    pass


class PazGasRequest(DataClassDictMixin):
    """Base class for all PazGas requests"""

    path: str = field(metadata=field_options(alias="path"))
    data: APIMRequest = field(metadata=field_options(alias="data"))

    class Config(BaseConfig):
        serialize_by_alias = True
