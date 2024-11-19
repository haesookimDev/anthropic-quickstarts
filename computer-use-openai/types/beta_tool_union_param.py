# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from . import BetaToolParam
from . import BetaToolBashParam
from . import BetaToolTextEditorParam
from . import BetaToolComputerUseParam

__all__ = ["BetaToolUnionParam"]

BetaToolUnionParam: TypeAlias = Union[
    BetaToolParam, BetaToolComputerUseParam, BetaToolBashParam, BetaToolTextEditorParam
]