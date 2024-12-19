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
from github_openapi.models.author_association import AuthorAssociation
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from github_openapi.models.reaction_rollup import ReactionRollup
from github_openapi.models.review_comment_links import ReviewCommentLinks
from typing import Optional, Set
from typing_extensions import Self

class ReviewComment(BaseModel):
    """
    Legacy Review Comment
    """ # noqa: E501
    url: StrictStr
    pull_request_review_id: Optional[StrictInt]
    id: StrictInt
    node_id: StrictStr
    diff_hunk: StrictStr
    path: StrictStr
    position: Optional[StrictInt]
    original_position: StrictInt
    commit_id: StrictStr
    original_commit_id: StrictStr
    in_reply_to_id: Optional[StrictInt] = None
    user: Optional[NullableSimpleUser]
    body: StrictStr
    created_at: datetime
    updated_at: datetime
    html_url: StrictStr
    pull_request_url: StrictStr
    author_association: AuthorAssociation
    links: ReviewCommentLinks = Field(alias="_links")
    body_text: Optional[StrictStr] = None
    body_html: Optional[StrictStr] = None
    reactions: Optional[ReactionRollup] = None
    side: Optional[StrictStr] = Field(default='RIGHT', description="The side of the first line of the range for a multi-line comment.")
    start_side: Optional[StrictStr] = Field(default='RIGHT', description="The side of the first line of the range for a multi-line comment.")
    line: Optional[StrictInt] = Field(default=None, description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment")
    original_line: Optional[StrictInt] = Field(default=None, description="The original line of the blob to which the comment applies. The last line of the range for a multi-line comment")
    start_line: Optional[StrictInt] = Field(default=None, description="The first line of the range for a multi-line comment.")
    original_start_line: Optional[StrictInt] = Field(default=None, description="The original first line of the range for a multi-line comment.")
    __properties: ClassVar[List[str]] = ["url", "pull_request_review_id", "id", "node_id", "diff_hunk", "path", "position", "original_position", "commit_id", "original_commit_id", "in_reply_to_id", "user", "body", "created_at", "updated_at", "html_url", "pull_request_url", "author_association", "_links", "body_text", "body_html", "reactions", "side", "start_side", "line", "original_line", "start_line", "original_start_line"]

    @field_validator('side')
    def side_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LEFT', 'RIGHT']):
            raise ValueError("must be one of enum values ('LEFT', 'RIGHT')")
        return value

    @field_validator('start_side')
    def start_side_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LEFT', 'RIGHT']):
            raise ValueError("must be one of enum values ('LEFT', 'RIGHT')")
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
        """Create an instance of ReviewComment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reactions
        if self.reactions:
            _dict['reactions'] = self.reactions.to_dict()
        # set to None if pull_request_review_id (nullable) is None
        # and model_fields_set contains the field
        if self.pull_request_review_id is None and "pull_request_review_id" in self.model_fields_set:
            _dict['pull_request_review_id'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        # set to None if start_side (nullable) is None
        # and model_fields_set contains the field
        if self.start_side is None and "start_side" in self.model_fields_set:
            _dict['start_side'] = None

        # set to None if start_line (nullable) is None
        # and model_fields_set contains the field
        if self.start_line is None and "start_line" in self.model_fields_set:
            _dict['start_line'] = None

        # set to None if original_start_line (nullable) is None
        # and model_fields_set contains the field
        if self.original_start_line is None and "original_start_line" in self.model_fields_set:
            _dict['original_start_line'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReviewComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "pull_request_review_id": obj.get("pull_request_review_id"),
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "diff_hunk": obj.get("diff_hunk"),
            "path": obj.get("path"),
            "position": obj.get("position"),
            "original_position": obj.get("original_position"),
            "commit_id": obj.get("commit_id"),
            "original_commit_id": obj.get("original_commit_id"),
            "in_reply_to_id": obj.get("in_reply_to_id"),
            "user": NullableSimpleUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "body": obj.get("body"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "html_url": obj.get("html_url"),
            "pull_request_url": obj.get("pull_request_url"),
            "author_association": obj.get("author_association"),
            "_links": ReviewCommentLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "body_text": obj.get("body_text"),
            "body_html": obj.get("body_html"),
            "reactions": ReactionRollup.from_dict(obj["reactions"]) if obj.get("reactions") is not None else None,
            "side": obj.get("side") if obj.get("side") is not None else 'RIGHT',
            "start_side": obj.get("start_side") if obj.get("start_side") is not None else 'RIGHT',
            "line": obj.get("line"),
            "original_line": obj.get("original_line"),
            "start_line": obj.get("start_line"),
            "original_start_line": obj.get("original_start_line")
        })
        return _obj

