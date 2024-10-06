from typing import Optional
import pydantic
from abc import ABC


class AbstractPost(pydantic.BaseModel, ABC):
    title: str
    description: str
    owner_id: int
    owner_name: str

    @pydantic.field_validator('description')
    @classmethod
    def secure_description(cls, v: str):
        if 'shit' in v:
            raise ValueError('ugh, how indecent!')


class CreatePost(AbstractPost):
    title: str
    description: Optional[str]
    owner_id: int
    owner_name: Optional[str]

