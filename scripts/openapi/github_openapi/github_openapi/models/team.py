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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.team_parent import TeamParent
from typing import Optional, Set
from typing_extensions import Self

class Team(BaseModel):
    """
    Groups of organization members that gives permissions on specified repositories.
    """ # noqa: E501
    deleted: Optional[StrictBool] = None
    description: Optional[StrictStr] = Field(default=None, description="Description of the team")
    html_url: Optional[StrictStr] = None
    id: StrictInt = Field(description="Unique identifier of the team")
    members_url: Optional[StrictStr] = None
    name: StrictStr = Field(description="Name of the team")
    node_id: Optional[StrictStr] = None
    parent: Optional[TeamParent] = None
    permission: Optional[StrictStr] = Field(default=None, description="Permission that the team will have for its repositories")
    privacy: Optional[StrictStr] = None
    repositories_url: Optional[StrictStr] = None
    slug: Optional[StrictStr] = None
    url: Optional[StrictStr] = Field(default=None, description="URL for the team")
    __properties: ClassVar[List[str]] = ["deleted", "description", "html_url", "id", "members_url", "name", "node_id", "parent", "permission", "privacy", "repositories_url", "slug", "url"]

    @field_validator('privacy')
    def privacy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'closed', 'secret']):
            raise ValueError("must be one of enum values ('open', 'closed', 'secret')")
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
        """Create an instance of Team from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if parent (nullable) is None
        # and model_fields_set contains the field
        if self.parent is None and "parent" in self.model_fields_set:
            _dict['parent'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Team from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deleted": obj.get("deleted"),
            "description": obj.get("description"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "members_url": obj.get("members_url"),
            "name": obj.get("name"),
            "node_id": obj.get("node_id"),
            "parent": TeamParent.from_dict(obj["parent"]) if obj.get("parent") is not None else None,
            "permission": obj.get("permission"),
            "privacy": obj.get("privacy"),
            "repositories_url": obj.get("repositories_url"),
            "slug": obj.get("slug"),
            "url": obj.get("url")
        })
        return _obj


