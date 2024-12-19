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
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.public_user_plan import PublicUserPlan
from typing import Optional, Set
from typing_extensions import Self

class PublicUser(BaseModel):
    """
    Public User
    """ # noqa: E501
    login: StrictStr
    id: StrictInt
    user_view_type: Optional[StrictStr] = None
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
    name: Optional[StrictStr]
    company: Optional[StrictStr]
    blog: Optional[StrictStr]
    location: Optional[StrictStr]
    email: Optional[StrictStr]
    notification_email: Optional[StrictStr] = None
    hireable: Optional[StrictBool]
    bio: Optional[StrictStr]
    twitter_username: Optional[StrictStr] = None
    public_repos: StrictInt
    public_gists: StrictInt
    followers: StrictInt
    following: StrictInt
    created_at: datetime
    updated_at: datetime
    plan: Optional[PublicUserPlan] = None
    private_gists: Optional[StrictInt] = None
    total_private_repos: Optional[StrictInt] = None
    owned_private_repos: Optional[StrictInt] = None
    disk_usage: Optional[StrictInt] = None
    collaborators: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["login", "id", "user_view_type", "node_id", "avatar_url", "gravatar_id", "url", "html_url", "followers_url", "following_url", "gists_url", "starred_url", "subscriptions_url", "organizations_url", "repos_url", "events_url", "received_events_url", "type", "site_admin", "name", "company", "blog", "location", "email", "notification_email", "hireable", "bio", "twitter_username", "public_repos", "public_gists", "followers", "following", "created_at", "updated_at", "plan", "private_gists", "total_private_repos", "owned_private_repos", "disk_usage", "collaborators"]

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
        """Create an instance of PublicUser from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of plan
        if self.plan:
            _dict['plan'] = self.plan.to_dict()
        # set to None if gravatar_id (nullable) is None
        # and model_fields_set contains the field
        if self.gravatar_id is None and "gravatar_id" in self.model_fields_set:
            _dict['gravatar_id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if company (nullable) is None
        # and model_fields_set contains the field
        if self.company is None and "company" in self.model_fields_set:
            _dict['company'] = None

        # set to None if blog (nullable) is None
        # and model_fields_set contains the field
        if self.blog is None and "blog" in self.model_fields_set:
            _dict['blog'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if notification_email (nullable) is None
        # and model_fields_set contains the field
        if self.notification_email is None and "notification_email" in self.model_fields_set:
            _dict['notification_email'] = None

        # set to None if hireable (nullable) is None
        # and model_fields_set contains the field
        if self.hireable is None and "hireable" in self.model_fields_set:
            _dict['hireable'] = None

        # set to None if bio (nullable) is None
        # and model_fields_set contains the field
        if self.bio is None and "bio" in self.model_fields_set:
            _dict['bio'] = None

        # set to None if twitter_username (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_username is None and "twitter_username" in self.model_fields_set:
            _dict['twitter_username'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "login": obj.get("login"),
            "id": obj.get("id"),
            "user_view_type": obj.get("user_view_type"),
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
            "name": obj.get("name"),
            "company": obj.get("company"),
            "blog": obj.get("blog"),
            "location": obj.get("location"),
            "email": obj.get("email"),
            "notification_email": obj.get("notification_email"),
            "hireable": obj.get("hireable"),
            "bio": obj.get("bio"),
            "twitter_username": obj.get("twitter_username"),
            "public_repos": obj.get("public_repos"),
            "public_gists": obj.get("public_gists"),
            "followers": obj.get("followers"),
            "following": obj.get("following"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "plan": PublicUserPlan.from_dict(obj["plan"]) if obj.get("plan") is not None else None,
            "private_gists": obj.get("private_gists"),
            "total_private_repos": obj.get("total_private_repos"),
            "owned_private_repos": obj.get("owned_private_repos"),
            "disk_usage": obj.get("disk_usage"),
            "collaborators": obj.get("collaborators")
        })
        return _obj


