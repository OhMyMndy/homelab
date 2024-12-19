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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Root(BaseModel):
    """
    Root
    """ # noqa: E501
    current_user_url: StrictStr
    current_user_authorizations_html_url: StrictStr
    authorizations_url: StrictStr
    code_search_url: StrictStr
    commit_search_url: StrictStr
    emails_url: StrictStr
    emojis_url: StrictStr
    events_url: StrictStr
    feeds_url: StrictStr
    followers_url: StrictStr
    following_url: StrictStr
    gists_url: StrictStr
    hub_url: Optional[StrictStr] = None
    issue_search_url: StrictStr
    issues_url: StrictStr
    keys_url: StrictStr
    label_search_url: StrictStr
    notifications_url: StrictStr
    organization_url: StrictStr
    organization_repositories_url: StrictStr
    organization_teams_url: StrictStr
    public_gists_url: StrictStr
    rate_limit_url: StrictStr
    repository_url: StrictStr
    repository_search_url: StrictStr
    current_user_repositories_url: StrictStr
    starred_url: StrictStr
    starred_gists_url: StrictStr
    topic_search_url: Optional[StrictStr] = None
    user_url: StrictStr
    user_organizations_url: StrictStr
    user_repositories_url: StrictStr
    user_search_url: StrictStr
    __properties: ClassVar[List[str]] = ["current_user_url", "current_user_authorizations_html_url", "authorizations_url", "code_search_url", "commit_search_url", "emails_url", "emojis_url", "events_url", "feeds_url", "followers_url", "following_url", "gists_url", "hub_url", "issue_search_url", "issues_url", "keys_url", "label_search_url", "notifications_url", "organization_url", "organization_repositories_url", "organization_teams_url", "public_gists_url", "rate_limit_url", "repository_url", "repository_search_url", "current_user_repositories_url", "starred_url", "starred_gists_url", "topic_search_url", "user_url", "user_organizations_url", "user_repositories_url", "user_search_url"]

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
        """Create an instance of Root from a JSON string"""
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
        """Create an instance of Root from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current_user_url": obj.get("current_user_url"),
            "current_user_authorizations_html_url": obj.get("current_user_authorizations_html_url"),
            "authorizations_url": obj.get("authorizations_url"),
            "code_search_url": obj.get("code_search_url"),
            "commit_search_url": obj.get("commit_search_url"),
            "emails_url": obj.get("emails_url"),
            "emojis_url": obj.get("emojis_url"),
            "events_url": obj.get("events_url"),
            "feeds_url": obj.get("feeds_url"),
            "followers_url": obj.get("followers_url"),
            "following_url": obj.get("following_url"),
            "gists_url": obj.get("gists_url"),
            "hub_url": obj.get("hub_url"),
            "issue_search_url": obj.get("issue_search_url"),
            "issues_url": obj.get("issues_url"),
            "keys_url": obj.get("keys_url"),
            "label_search_url": obj.get("label_search_url"),
            "notifications_url": obj.get("notifications_url"),
            "organization_url": obj.get("organization_url"),
            "organization_repositories_url": obj.get("organization_repositories_url"),
            "organization_teams_url": obj.get("organization_teams_url"),
            "public_gists_url": obj.get("public_gists_url"),
            "rate_limit_url": obj.get("rate_limit_url"),
            "repository_url": obj.get("repository_url"),
            "repository_search_url": obj.get("repository_search_url"),
            "current_user_repositories_url": obj.get("current_user_repositories_url"),
            "starred_url": obj.get("starred_url"),
            "starred_gists_url": obj.get("starred_gists_url"),
            "topic_search_url": obj.get("topic_search_url"),
            "user_url": obj.get("user_url"),
            "user_organizations_url": obj.get("user_organizations_url"),
            "user_repositories_url": obj.get("user_repositories_url"),
            "user_search_url": obj.get("user_search_url")
        })
        return _obj

