# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from _sdk._models import BaseModel

__all__ = ["TextBlock"]


class TextBlock(BaseModel):
    text: str

    type: Literal["text"]