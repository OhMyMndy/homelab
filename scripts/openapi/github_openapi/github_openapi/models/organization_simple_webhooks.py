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

class OrganizationSimpleWebhooks(BaseModel):
    """
    A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an organization, or when the event occurs from activity in a repository owned by an organization.
    """ # noqa: E501
    login: StrictStr
    id: StrictInt
    node_id: StrictStr
    url: StrictStr
    repos_url: StrictStr
    events_url: StrictStr
    hooks_url: StrictStr
    issues_url: StrictStr
    members_url: StrictStr
    public_members_url: StrictStr
    avatar_url: StrictStr
    description: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["login", "id", "node_id", "url", "repos_url", "events_url", "hooks_url", "issues_url", "members_url", "public_members_url", "avatar_url", "description"]

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
        """Create an instance of OrganizationSimpleWebhooks from a JSON string"""
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
        """Create an instance of OrganizationSimpleWebhooks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "login": obj.get("login"),
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "url": obj.get("url"),
            "repos_url": obj.get("repos_url"),
            "events_url": obj.get("events_url"),
            "hooks_url": obj.get("hooks_url"),
            "issues_url": obj.get("issues_url"),
            "members_url": obj.get("members_url"),
            "public_members_url": obj.get("public_members_url"),
            "avatar_url": obj.get("avatar_url"),
            "description": obj.get("description")
        })
        return _obj

