# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateUserOption(BaseModel):
    """
    CreateUserOption create user options
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, description="For explicitly setting the user creation timestamp. Useful when users are migrated from other systems. When omitted, the user's creation timestamp will be set to \"now\".")
    email: StrictStr
    full_name: Optional[StrictStr] = None
    login_name: Optional[StrictStr] = None
    must_change_password: Optional[StrictBool] = None
    password: Optional[StrictStr] = None
    restricted: Optional[StrictBool] = None
    send_notify: Optional[StrictBool] = None
    source_id: Optional[StrictInt] = None
    username: StrictStr
    visibility: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "email", "full_name", "login_name", "must_change_password", "password", "restricted", "send_notify", "source_id", "username", "visibility"]

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
        """Create an instance of CreateUserOption from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateUserOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "email": obj.get("email"),
            "full_name": obj.get("full_name"),
            "login_name": obj.get("login_name"),
            "must_change_password": obj.get("must_change_password"),
            "password": obj.get("password"),
            "restricted": obj.get("restricted"),
            "send_notify": obj.get("send_notify"),
            "source_id": obj.get("source_id"),
            "username": obj.get("username"),
            "visibility": obj.get("visibility")
        })
        return _obj

