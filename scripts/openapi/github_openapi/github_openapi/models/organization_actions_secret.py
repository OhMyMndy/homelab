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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrganizationActionsSecret(BaseModel):
    """
    Secrets for GitHub Actions for an organization.
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the secret.")
    created_at: datetime
    updated_at: datetime
    visibility: StrictStr = Field(description="Visibility of a secret")
    selected_repositories_url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "created_at", "updated_at", "visibility", "selected_repositories_url"]

    @field_validator('visibility')
    def visibility_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['all', 'private', 'selected']):
            raise ValueError("must be one of enum values ('all', 'private', 'selected')")
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
        """Create an instance of OrganizationActionsSecret from a JSON string"""
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
        """Create an instance of OrganizationActionsSecret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "visibility": obj.get("visibility"),
            "selected_repositories_url": obj.get("selected_repositories_url")
        })
        return _obj


