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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NullableSimpleUser(BaseModel):
    """
    A GitHub user.
    """ # noqa: E501
    name: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    login: StrictStr
    id: StrictInt
    node_id: StrictStr
    avatar_url: StrictStr
    gravatar_id: Optional[StrictStr]
    url: StrictStr
    html_url: StrictStr
    followers_url: StrictStr
    following_url: StrictStr
    gists_url: StrictStr
    starred_url: StrictStr
    subscriptions_url: StrictStr
    organizations_url: StrictStr
    repos_url: StrictStr
    events_url: StrictStr
    received_events_url: StrictStr
    type: StrictStr
    site_admin: StrictBool
    starred_at: Optional[StrictStr] = None
    user_view_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["name", "email", "login", "id", "node_id", "avatar_url", "gravatar_id", "url", "html_url", "followers_url", "following_url", "gists_url", "starred_url", "subscriptions_url", "organizations_url", "repos_url", "events_url", "received_events_url", "type", "site_admin", "starred_at", "user_view_type"]

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
        """Create an instance of NullableSimpleUser from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if gravatar_id (nullable) is None
        # and model_fields_set contains the field
        if self.gravatar_id is None and "gravatar_id" in self.model_fields_set:
            _dict['gravatar_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NullableSimpleUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "login": obj.get("login"),
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "avatar_url": obj.get("avatar_url"),
            "gravatar_id": obj.get("gravatar_id"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "followers_url": obj.get("followers_url"),
            "following_url": obj.get("following_url"),
            "gists_url": obj.get("gists_url"),
            "starred_url": obj.get("starred_url"),
            "subscriptions_url": obj.get("subscriptions_url"),
            "organizations_url": obj.get("organizations_url"),
            "repos_url": obj.get("repos_url"),
            "events_url": obj.get("events_url"),
            "received_events_url": obj.get("received_events_url"),
            "type": obj.get("type"),
            "site_admin": obj.get("site_admin"),
            "starred_at": obj.get("starred_at"),
            "user_view_type": obj.get("user_view_type")
        })
        return _obj


