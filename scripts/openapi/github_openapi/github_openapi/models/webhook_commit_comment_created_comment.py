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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.reactions import Reactions
from github_openapi.models.user1 import User1
from typing import Optional, Set
from typing_extensions import Self

class WebhookCommitCommentCreatedComment(BaseModel):
    """
    The [commit comment](${externalDocsUpapp/api/description/components/schemas/webhooks/issue-comment-created.yamlrl}/rest/commits/comments#get-a-commit-comment) resource.
    """ # noqa: E501
    author_association: StrictStr = Field(description="How the author is associated with the repository.")
    body: StrictStr = Field(description="The text of the comment.")
    commit_id: StrictStr = Field(description="The SHA of the commit to which the comment applies.")
    created_at: StrictStr
    html_url: StrictStr
    id: StrictInt = Field(description="The ID of the commit comment.")
    line: Optional[StrictInt] = Field(description="The line of the blob to which the comment applies. The last line of the range for a multi-line comment")
    node_id: StrictStr = Field(description="The node ID of the commit comment.")
    path: Optional[StrictStr] = Field(description="The relative path of the file to which the comment applies.")
    position: Optional[StrictInt] = Field(description="The line index in the diff to which the comment applies.")
    reactions: Optional[Reactions] = None
    updated_at: StrictStr
    url: StrictStr
    user: Optional[User1]
    __properties: ClassVar[List[str]] = ["author_association", "body", "commit_id", "created_at", "html_url", "id", "line", "node_id", "path", "position", "reactions", "updated_at", "url", "user"]

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
        """Create an instance of WebhookCommitCommentCreatedComment from a JSON string"""
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

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookCommitCommentCreatedComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "author_association": obj.get("author_association"),
            "body": obj.get("body"),
            "commit_id": obj.get("commit_id"),
            "created_at": obj.get("created_at"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "line": obj.get("line"),
            "node_id": obj.get("node_id"),
            "path": obj.get("path"),
            "position": obj.get("position"),
            "reactions": Reactions.from_dict(obj["reactions"]) if obj.get("reactions") is not None else None,
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "user": User1.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


