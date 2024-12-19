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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.nullable_integration import NullableIntegration
from github_openapi.models.reactions import Reactions
from github_openapi.models.user1 import User1
from typing import Optional, Set
from typing_extensions import Self

class IssueComment(BaseModel):
    """
    The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself.
    """ # noqa: E501
    author_association: StrictStr = Field(description="How the author is associated with the repository.")
    body: StrictStr = Field(description="Contents of the issue comment")
    created_at: datetime
    html_url: StrictStr
    id: StrictInt = Field(description="Unique identifier of the issue comment")
    issue_url: StrictStr
    node_id: StrictStr
    performed_via_github_app: Optional[NullableIntegration]
    reactions: Reactions
    updated_at: datetime
    url: StrictStr = Field(description="URL for the issue comment")
    user: Optional[User1]
    __properties: ClassVar[List[str]] = ["author_association", "body", "created_at", "html_url", "id", "issue_url", "node_id", "performed_via_github_app", "reactions", "updated_at", "url", "user"]

    @field_validator('author_association')
    def author_association_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIMER', 'FIRST_TIME_CONTRIBUTOR', 'MANNEQUIN', 'MEMBER', 'NONE', 'OWNER']):
            raise ValueError("must be one of enum values ('COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIMER', 'FIRST_TIME_CONTRIBUTOR', 'MANNEQUIN', 'MEMBER', 'NONE', 'OWNER')")
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
        """Create an instance of IssueComment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of performed_via_github_app
        if self.performed_via_github_app:
            _dict['performed_via_github_app'] = self.performed_via_github_app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reactions
        if self.reactions:
            _dict['reactions'] = self.reactions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if performed_via_github_app (nullable) is None
        # and model_fields_set contains the field
        if self.performed_via_github_app is None and "performed_via_github_app" in self.model_fields_set:
            _dict['performed_via_github_app'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssueComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "author_association": obj.get("author_association"),
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "issue_url": obj.get("issue_url"),
            "node_id": obj.get("node_id"),
            "performed_via_github_app": NullableIntegration.from_dict(obj["performed_via_github_app"]) if obj.get("performed_via_github_app") is not None else None,
            "reactions": Reactions.from_dict(obj["reactions"]) if obj.get("reactions") is not None else None,
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "user": User1.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj

