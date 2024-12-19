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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.app12 import App12
from github_openapi.models.label import Label
from github_openapi.models.milestone import Milestone
from github_openapi.models.reactions import Reactions
from github_openapi.models.sub_issues_summary import SubIssuesSummary
from github_openapi.models.user3 import User3
from github_openapi.models.user4 import User4
from github_openapi.models.user5 import User5
from github_openapi.models.webhooks_issue_pull_request import WebhooksIssuePullRequest
from typing import Optional, Set
from typing_extensions import Self

class Issue2(BaseModel):
    """
    The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    """ # noqa: E501
    active_lock_reason: Optional[StrictStr]
    assignee: Optional[User4] = None
    assignees: List[Optional[User5]]
    author_association: StrictStr = Field(description="How the author is associated with the repository.")
    body: Optional[StrictStr] = Field(description="Contents of the issue")
    closed_at: Optional[datetime]
    comments: StrictInt
    comments_url: StrictStr
    created_at: datetime
    draft: Optional[StrictBool] = None
    events_url: StrictStr
    html_url: StrictStr
    id: StrictInt
    labels: Optional[List[Label]] = None
    labels_url: StrictStr
    locked: Optional[StrictBool] = None
    milestone: Optional[Milestone]
    node_id: StrictStr
    number: StrictInt
    performed_via_github_app: Optional[App12] = None
    pull_request: Optional[WebhooksIssuePullRequest] = None
    reactions: Reactions
    repository_url: StrictStr
    sub_issues_summary: Optional[SubIssuesSummary] = None
    state: Optional[StrictStr] = Field(default=None, description="State of the issue; either 'open' or 'closed'")
    state_reason: Optional[StrictStr] = None
    timeline_url: Optional[StrictStr] = None
    title: StrictStr = Field(description="Title of the issue")
    updated_at: datetime
    url: StrictStr = Field(description="URL for the issue")
    user: Optional[User3]
    __properties: ClassVar[List[str]] = ["active_lock_reason", "assignee", "assignees", "author_association", "body", "closed_at", "comments", "comments_url", "created_at", "draft", "events_url", "html_url", "id", "labels", "labels_url", "locked", "milestone", "node_id", "number", "performed_via_github_app", "pull_request", "reactions", "repository_url", "sub_issues_summary", "state", "state_reason", "timeline_url", "title", "updated_at", "url", "user"]

    @field_validator('active_lock_reason')
    def active_lock_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['resolved', 'off-topic', 'too heated', 'spam']):
            raise ValueError("must be one of enum values ('resolved', 'off-topic', 'too heated', 'spam')")
        return value

    @field_validator('author_association')
    def author_association_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIMER', 'FIRST_TIME_CONTRIBUTOR', 'MANNEQUIN', 'MEMBER', 'NONE', 'OWNER']):
            raise ValueError("must be one of enum values ('COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIMER', 'FIRST_TIME_CONTRIBUTOR', 'MANNEQUIN', 'MEMBER', 'NONE', 'OWNER')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open', 'closed']):
            raise ValueError("must be one of enum values ('open', 'closed')")
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
        """Create an instance of Issue2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of assignee
        if self.assignee:
            _dict['assignee'] = self.assignee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item_assignees in self.assignees:
                if _item_assignees:
                    _items.append(_item_assignees.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of milestone
        if self.milestone:
            _dict['milestone'] = self.milestone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of performed_via_github_app
        if self.performed_via_github_app:
            _dict['performed_via_github_app'] = self.performed_via_github_app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pull_request
        if self.pull_request:
            _dict['pull_request'] = self.pull_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reactions
        if self.reactions:
            _dict['reactions'] = self.reactions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_issues_summary
        if self.sub_issues_summary:
            _dict['sub_issues_summary'] = self.sub_issues_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if active_lock_reason (nullable) is None
        # and model_fields_set contains the field
        if self.active_lock_reason is None and "active_lock_reason" in self.model_fields_set:
            _dict['active_lock_reason'] = None

        # set to None if assignee (nullable) is None
        # and model_fields_set contains the field
        if self.assignee is None and "assignee" in self.model_fields_set:
            _dict['assignee'] = None

        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        # set to None if closed_at (nullable) is None
        # and model_fields_set contains the field
        if self.closed_at is None and "closed_at" in self.model_fields_set:
            _dict['closed_at'] = None

        # set to None if milestone (nullable) is None
        # and model_fields_set contains the field
        if self.milestone is None and "milestone" in self.model_fields_set:
            _dict['milestone'] = None

        # set to None if performed_via_github_app (nullable) is None
        # and model_fields_set contains the field
        if self.performed_via_github_app is None and "performed_via_github_app" in self.model_fields_set:
            _dict['performed_via_github_app'] = None

        # set to None if state_reason (nullable) is None
        # and model_fields_set contains the field
        if self.state_reason is None and "state_reason" in self.model_fields_set:
            _dict['state_reason'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Issue2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active_lock_reason": obj.get("active_lock_reason"),
            "assignee": User4.from_dict(obj["assignee"]) if obj.get("assignee") is not None else None,
            "assignees": [User5.from_dict(_item) for _item in obj["assignees"]] if obj.get("assignees") is not None else None,
            "author_association": obj.get("author_association"),
            "body": obj.get("body"),
            "closed_at": obj.get("closed_at"),
            "comments": obj.get("comments"),
            "comments_url": obj.get("comments_url"),
            "created_at": obj.get("created_at"),
            "draft": obj.get("draft"),
            "events_url": obj.get("events_url"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "labels_url": obj.get("labels_url"),
            "locked": obj.get("locked"),
            "milestone": Milestone.from_dict(obj["milestone"]) if obj.get("milestone") is not None else None,
            "node_id": obj.get("node_id"),
            "number": obj.get("number"),
            "performed_via_github_app": App12.from_dict(obj["performed_via_github_app"]) if obj.get("performed_via_github_app") is not None else None,
            "pull_request": WebhooksIssuePullRequest.from_dict(obj["pull_request"]) if obj.get("pull_request") is not None else None,
            "reactions": Reactions.from_dict(obj["reactions"]) if obj.get("reactions") is not None else None,
            "repository_url": obj.get("repository_url"),
            "sub_issues_summary": SubIssuesSummary.from_dict(obj["sub_issues_summary"]) if obj.get("sub_issues_summary") is not None else None,
            "state": obj.get("state"),
            "state_reason": obj.get("state_reason"),
            "timeline_url": obj.get("timeline_url"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "user": User3.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


