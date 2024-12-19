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

class WebhookRegistryPackagePublishedRegistryPackageOwner(BaseModel):
    """
    WebhookRegistryPackagePublishedRegistryPackageOwner
    """ # noqa: E501
    avatar_url: StrictStr
    events_url: StrictStr
    followers_url: StrictStr
    following_url: StrictStr
    gists_url: StrictStr
    gravatar_id: StrictStr
    html_url: StrictStr
    id: StrictInt
    login: StrictStr
    node_id: StrictStr
    organizations_url: StrictStr
    received_events_url: StrictStr
    repos_url: StrictStr
    site_admin: StrictBool
    starred_url: StrictStr
    subscriptions_url: StrictStr
    type: StrictStr
    url: StrictStr
    user_view_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["avatar_url", "events_url", "followers_url", "following_url", "gists_url", "gravatar_id", "html_url", "id", "login", "node_id", "organizations_url", "received_events_url", "repos_url", "site_admin", "starred_url", "subscriptions_url", "type", "url", "user_view_type"]

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
        """Create an instance of WebhookRegistryPackagePublishedRegistryPackageOwner from a JSON string"""
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
        """Create an instance of WebhookRegistryPackagePublishedRegistryPackageOwner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avatar_url": obj.get("avatar_url"),
            "events_url": obj.get("events_url"),
            "followers_url": obj.get("followers_url"),
            "following_url": obj.get("following_url"),
            "gists_url": obj.get("gists_url"),
            "gravatar_id": obj.get("gravatar_id"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "login": obj.get("login"),
            "node_id": obj.get("node_id"),
            "organizations_url": obj.get("organizations_url"),
            "received_events_url": obj.get("received_events_url"),
            "repos_url": obj.get("repos_url"),
            "site_admin": obj.get("site_admin"),
            "starred_url": obj.get("starred_url"),
            "subscriptions_url": obj.get("subscriptions_url"),
            "type": obj.get("type"),
            "url": obj.get("url"),
            "user_view_type": obj.get("user_view_type")
        })
        return _obj


