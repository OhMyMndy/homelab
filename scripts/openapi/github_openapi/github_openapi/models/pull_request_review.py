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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.author_association import AuthorAssociation
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from github_openapi.models.timeline_reviewed_event_links import TimelineReviewedEventLinks
from typing import Optional, Set
from typing_extensions import Self

class PullRequestReview(BaseModel):
    """
    Pull Request Reviews are reviews on pull requests.
    """ # noqa: E501
    id: StrictInt = Field(description="Unique identifier of the review")
    node_id: StrictStr
    user: Optional[NullableSimpleUser]
    body: StrictStr = Field(description="The text of the review.")
    state: StrictStr
    html_url: StrictStr
    pull_request_url: StrictStr
    links: TimelineReviewedEventLinks = Field(alias="_links")
    submitted_at: Optional[datetime] = None
    commit_id: Optional[StrictStr] = Field(description="A commit SHA for the review. If the commit object was garbage collected or forcibly deleted, then it no longer exists in Git and this value will be `null`.")
    body_html: Optional[StrictStr] = None
    body_text: Optional[StrictStr] = None
    author_association: AuthorAssociation
    __properties: ClassVar[List[str]] = ["id", "node_id", "user", "body", "state", "html_url", "pull_request_url", "_links", "submitted_at", "commit_id", "body_html", "body_text", "author_association"]

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
        """Create an instance of PullRequestReview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if commit_id (nullable) is None
        # and model_fields_set contains the field
        if self.commit_id is None and "commit_id" in self.model_fields_set:
            _dict['commit_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PullRequestReview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "user": NullableSimpleUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "body": obj.get("body"),
            "state": obj.get("state"),
            "html_url": obj.get("html_url"),
            "pull_request_url": obj.get("pull_request_url"),
            "_links": TimelineReviewedEventLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "submitted_at": obj.get("submitted_at"),
            "commit_id": obj.get("commit_id"),
            "body_html": obj.get("body_html"),
            "body_text": obj.get("body_text"),
            "author_association": obj.get("author_association")
        })
        return _obj

