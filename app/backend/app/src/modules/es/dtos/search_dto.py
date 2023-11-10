from __future__ import annotations
from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class SingleFieldQuery:
    field: str
    value: str
    size: int


class BasicSearchDto(BaseModel):
    query: SingleFieldQuery
