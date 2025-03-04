# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from typing import Optional, Set
from typing_extensions import Self

class Reaction(BaseModel):
    """
    Reactions to conversations provide a way to help people express their feelings more simply and effectively.
    """ # noqa: E501
    id: StrictInt
    node_id: StrictStr
    user: Optional[NullableSimpleUser]
    content: StrictStr = Field(description="The reaction to use")
    created_at: datetime
    __properties: ClassVar[List[str]] = ["id", "node_id", "user", "content", "created_at"]

    @field_validator('content')
    def content_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['+1', '-1', 'laugh', 'confused', 'heart', 'hooray', 'rocket', 'eyes']):
            raise ValueError("must be one of enum values ('+1', '-1', 'laugh', 'confused', 'heart', 'hooray', 'rocket', 'eyes')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Reaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Reaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "user": NullableSimpleUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "content": obj.get("content"),
            "created_at": obj.get("created_at")
        })
        return _obj


