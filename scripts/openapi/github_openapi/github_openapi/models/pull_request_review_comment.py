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
from github_openapi.models.reactions import Reactions
from github_openapi.models.user1 import User1
from github_openapi.models.webhooks_review_comment_links import WebhooksReviewCommentLinks
from typing import Optional, Set
from typing_extensions import Self

class PullRequestReviewComment(BaseModel):
    """
    The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself.
    """ # noqa: E501
    links: WebhooksReviewCommentLinks = Field(alias="_links")
    author_association: StrictStr = Field(description="How the author is associated with the repository.")
    body: StrictStr = Field(description="The text of the comment.")
    commit_id: StrictStr = Field(description="The SHA of the commit to which the comment applies.")
    created_at: datetime
    diff_hunk: StrictStr = Field(description="The diff of the line that the comment refers to.")
    html_url: StrictStr = Field(description="HTML URL for the pull request review comment.")
    id: StrictInt = Field(description="The ID of the pull request review comment.")
    in_reply_to_id: Optional[StrictInt] = Field(default=None, description="The comment ID to reply to.")
    line: Optional[StrictInt] = Field(description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment")
    node_id: StrictStr = Field(description="The node ID of the pull request review comment.")
    original_commit_id: StrictStr = Field(description="The SHA of the original commit to which the comment applies.")
    original_line: Optional[StrictInt] = Field(description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment")
    original_position: StrictInt = Field(description="The index of the original line in the diff to which the comment applies.")
    original_start_line: Optional[StrictInt] = Field(description="The first line of the range for a multi-line comment.")
    path: StrictStr = Field(description="The relative path of the file to which the comment applies.")
    position: Optional[StrictInt] = Field(description="The line index in the diff to which the comment applies.")
    pull_request_review_id: Optional[StrictInt] = Field(description="The ID of the pull request review to which the comment belongs.")
    pull_request_url: StrictStr = Field(description="URL for the pull request that the review comment belongs to.")
    reactions: Reactions
    side: StrictStr = Field(description="The side of the first line of the range for a multi-line comment.")
    start_line: Optional[StrictInt] = Field(description="The first line of the range for a multi-line comment.")
    start_side: Optional[StrictStr] = Field(description="The side of the first line of the range for a multi-line comment.")
    subject_type: Optional[StrictStr] = Field(default=None, description="The level at which the comment is targeted, can be a diff line or a file.")
    updated_at: datetime
    url: StrictStr = Field(description="URL for the pull request review comment")
    user: Optional[User1]
    __properties: ClassVar[List[str]] = ["_links", "author_association", "body", "commit_id", "created_at", "diff_hunk", "html_url", "id", "in_reply_to_id", "line", "node_id", "original_commit_id", "original_line", "original_position", "original_start_line", "path", "position", "pull_request_review_id", "pull_request_url", "reactions", "side", "start_line", "start_side", "subject_type", "updated_at", "url", "user"]

    @field_validator('author_association')
    def author_association_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIMER', 'FIRST_TIME_CONTRIBUTOR', 'MANNEQUIN', 'MEMBER', 'NONE', 'OWNER']):
            raise ValueError("must be one of enum values ('COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIMER', 'FIRST_TIME_CONTRIBUTOR', 'MANNEQUIN', 'MEMBER', 'NONE', 'OWNER')")
        return value

    @field_validator('side')
    def side_validate_enum(cls, value):
        """Validates the enum"""
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

    @field_validator('subject_type')
    def subject_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['line', 'file']):
            raise ValueError("must be one of enum values ('line', 'file')")
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
        """Create an instance of PullRequestReviewComment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reactions
        if self.reactions:
            _dict['reactions'] = self.reactions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if line (nullable) is None
        # and model_fields_set contains the field
        if self.line is None and "line" in self.model_fields_set:
            _dict['line'] = None

        # set to None if original_line (nullable) is None
        # and model_fields_set contains the field
        if self.original_line is None and "original_line" in self.model_fields_set:
            _dict['original_line'] = None

        # set to None if original_start_line (nullable) is None
        # and model_fields_set contains the field
        if self.original_start_line is None and "original_start_line" in self.model_fields_set:
            _dict['original_start_line'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if pull_request_review_id (nullable) is None
        # and model_fields_set contains the field
        if self.pull_request_review_id is None and "pull_request_review_id" in self.model_fields_set:
            _dict['pull_request_review_id'] = None

        # set to None if start_line (nullable) is None
        # and model_fields_set contains the field
        if self.start_line is None and "start_line" in self.model_fields_set:
            _dict['start_line'] = None

        # set to None if start_side (nullable) is None
        # and model_fields_set contains the field
        if self.start_side is None and "start_side" in self.model_fields_set:
            _dict['start_side'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PullRequestReviewComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_links": WebhooksReviewCommentLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "author_association": obj.get("author_association"),
            "body": obj.get("body"),
            "commit_id": obj.get("commit_id"),
            "created_at": obj.get("created_at"),
            "diff_hunk": obj.get("diff_hunk"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "in_reply_to_id": obj.get("in_reply_to_id"),
            "line": obj.get("line"),
            "node_id": obj.get("node_id"),
            "original_commit_id": obj.get("original_commit_id"),
            "original_line": obj.get("original_line"),
            "original_position": obj.get("original_position"),
            "original_start_line": obj.get("original_start_line"),
            "path": obj.get("path"),
            "position": obj.get("position"),
            "pull_request_review_id": obj.get("pull_request_review_id"),
            "pull_request_url": obj.get("pull_request_url"),
            "reactions": Reactions.from_dict(obj["reactions"]) if obj.get("reactions") is not None else None,
            "side": obj.get("side"),
            "start_line": obj.get("start_line"),
            "start_side": obj.get("start_side") if obj.get("start_side") is not None else 'RIGHT',
            "subject_type": obj.get("subject_type"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "user": User1.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


