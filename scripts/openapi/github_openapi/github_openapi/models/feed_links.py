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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.link_with_type import LinkWithType
from typing import Optional, Set
from typing_extensions import Self

class FeedLinks(BaseModel):
    """
    FeedLinks
    """ # noqa: E501
    timeline: LinkWithType
    user: LinkWithType
    security_advisories: Optional[LinkWithType] = None
    current_user: Optional[LinkWithType] = None
    current_user_public: Optional[LinkWithType] = None
    current_user_actor: Optional[LinkWithType] = None
    current_user_organization: Optional[LinkWithType] = None
    current_user_organizations: Optional[List[LinkWithType]] = None
    repository_discussions: Optional[LinkWithType] = None
    repository_discussions_category: Optional[LinkWithType] = None
    __properties: ClassVar[List[str]] = ["timeline", "user", "security_advisories", "current_user", "current_user_public", "current_user_actor", "current_user_organization", "current_user_organizations", "repository_discussions", "repository_discussions_category"]

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
        """Create an instance of FeedLinks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of timeline
        if self.timeline:
            _dict['timeline'] = self.timeline.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_advisories
        if self.security_advisories:
            _dict['security_advisories'] = self.security_advisories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_user
        if self.current_user:
            _dict['current_user'] = self.current_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_user_public
        if self.current_user_public:
            _dict['current_user_public'] = self.current_user_public.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_user_actor
        if self.current_user_actor:
            _dict['current_user_actor'] = self.current_user_actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_user_organization
        if self.current_user_organization:
            _dict['current_user_organization'] = self.current_user_organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in current_user_organizations (list)
        _items = []
        if self.current_user_organizations:
            for _item_current_user_organizations in self.current_user_organizations:
                if _item_current_user_organizations:
                    _items.append(_item_current_user_organizations.to_dict())
            _dict['current_user_organizations'] = _items
        # override the default output from pydantic by calling `to_dict()` of repository_discussions
        if self.repository_discussions:
            _dict['repository_discussions'] = self.repository_discussions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository_discussions_category
        if self.repository_discussions_category:
            _dict['repository_discussions_category'] = self.repository_discussions_category.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeedLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timeline": LinkWithType.from_dict(obj["timeline"]) if obj.get("timeline") is not None else None,
            "user": LinkWithType.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "security_advisories": LinkWithType.from_dict(obj["security_advisories"]) if obj.get("security_advisories") is not None else None,
            "current_user": LinkWithType.from_dict(obj["current_user"]) if obj.get("current_user") is not None else None,
            "current_user_public": LinkWithType.from_dict(obj["current_user_public"]) if obj.get("current_user_public") is not None else None,
            "current_user_actor": LinkWithType.from_dict(obj["current_user_actor"]) if obj.get("current_user_actor") is not None else None,
            "current_user_organization": LinkWithType.from_dict(obj["current_user_organization"]) if obj.get("current_user_organization") is not None else None,
            "current_user_organizations": [LinkWithType.from_dict(_item) for _item in obj["current_user_organizations"]] if obj.get("current_user_organizations") is not None else None,
            "repository_discussions": LinkWithType.from_dict(obj["repository_discussions"]) if obj.get("repository_discussions") is not None else None,
            "repository_discussions_category": LinkWithType.from_dict(obj["repository_discussions_category"]) if obj.get("repository_discussions_category") is not None else None
        })
        return _obj


