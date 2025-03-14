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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Organization(BaseModel):
    """
    Organization
    """ # noqa: E501
    avatar_url: StrictStr
    description: Optional[StrictStr]
    events_url: StrictStr
    hooks_url: StrictStr
    html_url: Optional[StrictStr] = None
    id: StrictInt
    issues_url: StrictStr
    login: StrictStr
    members_url: StrictStr
    node_id: StrictStr
    public_members_url: StrictStr
    repos_url: StrictStr
    url: StrictStr
    __properties: ClassVar[List[str]] = ["avatar_url", "description", "events_url", "hooks_url", "html_url", "id", "issues_url", "login", "members_url", "node_id", "public_members_url", "repos_url", "url"]

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
        """Create an instance of Organization from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Organization from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avatar_url": obj.get("avatar_url"),
            "description": obj.get("description"),
            "events_url": obj.get("events_url"),
            "hooks_url": obj.get("hooks_url"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "issues_url": obj.get("issues_url"),
            "login": obj.get("login"),
            "members_url": obj.get("members_url"),
            "node_id": obj.get("node_id"),
            "public_members_url": obj.get("public_members_url"),
            "repos_url": obj.get("repos_url"),
            "url": obj.get("url")
        })
        return _obj


