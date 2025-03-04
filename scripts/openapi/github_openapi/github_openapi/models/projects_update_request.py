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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProjectsUpdateRequest(BaseModel):
    """
    ProjectsUpdateRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of the project")
    body: Optional[StrictStr] = Field(default=None, description="Body of the project")
    state: Optional[StrictStr] = Field(default=None, description="State of the project; either 'open' or 'closed'")
    organization_permission: Optional[StrictStr] = Field(default=None, description="The baseline permission that all organization members have on this project")
    private: Optional[StrictBool] = Field(default=None, description="Whether or not this project can be seen by everyone.")
    __properties: ClassVar[List[str]] = ["name", "body", "state", "organization_permission", "private"]

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
        """Create an instance of ProjectsUpdateRequest from a JSON string"""
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
        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectsUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "body": obj.get("body"),
            "state": obj.get("state"),
            "organization_permission": obj.get("organization_permission"),
            "private": obj.get("private")
        })
        return _obj


