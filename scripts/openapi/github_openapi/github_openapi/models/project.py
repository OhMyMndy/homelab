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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from typing import Optional, Set
from typing_extensions import Self

class Project(BaseModel):
    """
    Projects are a way to organize columns and cards of work.
    """ # noqa: E501
    owner_url: StrictStr
    url: StrictStr
    html_url: StrictStr
    columns_url: StrictStr
    id: StrictInt
    node_id: StrictStr
    name: StrictStr = Field(description="Name of the project")
    body: Optional[StrictStr] = Field(description="Body of the project")
    number: StrictInt
    state: StrictStr = Field(description="State of the project; either 'open' or 'closed'")
    creator: Optional[NullableSimpleUser]
    created_at: datetime
    updated_at: datetime
    organization_permission: Optional[StrictStr] = Field(default=None, description="The baseline permission that all organization members have on this project. Only present if owner is an organization.")
    private: Optional[StrictBool] = Field(default=None, description="Whether or not this project can be seen by everyone. Only present if owner is an organization.")
    __properties: ClassVar[List[str]] = ["owner_url", "url", "html_url", "columns_url", "id", "node_id", "name", "body", "number", "state", "creator", "created_at", "updated_at", "organization_permission", "private"]

    @field_validator('organization_permission')
    def organization_permission_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['read', 'write', 'admin', 'none']):
            raise ValueError("must be one of enum values ('read', 'write', 'admin', 'none')")
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
        """Create an instance of Project from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        # set to None if creator (nullable) is None
        # and model_fields_set contains the field
        if self.creator is None and "creator" in self.model_fields_set:
            _dict['creator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "owner_url": obj.get("owner_url"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "columns_url": obj.get("columns_url"),
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "name": obj.get("name"),
            "body": obj.get("body"),
            "number": obj.get("number"),
            "state": obj.get("state"),
            "creator": NullableSimpleUser.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "organization_permission": obj.get("organization_permission"),
            "private": obj.get("private")
        })
        return _obj


