# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from authentik_openapi.models.intent_enum import IntentEnum
from typing import Optional, Set
from typing_extensions import Self

class PatchedTokenRequest(BaseModel):
    """
    Token Serializer
    """ # noqa: E501
    managed: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.")
    identifier: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    intent: Optional[IntentEnum] = None
    user: Optional[StrictInt] = None
    description: Optional[StrictStr] = None
    expires: Optional[datetime] = None
    expiring: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["managed", "identifier", "intent", "user", "description", "expires", "expiring"]

    @field_validator('identifier')
    def identifier_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
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
        """Create an instance of PatchedTokenRequest from a JSON string"""
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
        # set to None if managed (nullable) is None
        # and model_fields_set contains the field
        if self.managed is None and "managed" in self.model_fields_set:
            _dict['managed'] = None

        # set to None if expires (nullable) is None
        # and model_fields_set contains the field
        if self.expires is None and "expires" in self.model_fields_set:
            _dict['expires'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedTokenRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "managed": obj.get("managed"),
            "identifier": obj.get("identifier"),
            "intent": obj.get("intent"),
            "user": obj.get("user"),
            "description": obj.get("description"),
            "expires": obj.get("expires"),
            "expiring": obj.get("expiring")
        })
        return _obj


