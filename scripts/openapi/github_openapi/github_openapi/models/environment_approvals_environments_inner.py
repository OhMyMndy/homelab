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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EnvironmentApprovalsEnvironmentsInner(BaseModel):
    """
    EnvironmentApprovalsEnvironmentsInner
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The id of the environment.")
    node_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the environment.")
    url: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = Field(default=None, description="The time that the environment was created, in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="The time that the environment was last updated, in ISO 8601 format.")
    __properties: ClassVar[List[str]] = ["id", "node_id", "name", "url", "html_url", "created_at", "updated_at"]

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
        """Create an instance of EnvironmentApprovalsEnvironmentsInner from a JSON string"""
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
        """Create an instance of EnvironmentApprovalsEnvironmentsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "name": obj.get("name"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

