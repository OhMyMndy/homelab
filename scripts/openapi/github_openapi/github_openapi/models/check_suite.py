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
from github_openapi.models.minimal_repository import MinimalRepository
from github_openapi.models.nullable_integration import NullableIntegration
from github_openapi.models.pull_request_minimal import PullRequestMinimal
from github_openapi.models.simple_commit import SimpleCommit
from typing import Optional, Set
from typing_extensions import Self

class CheckSuite(BaseModel):
    """
    A suite of checks performed on the code of a given code change
    """ # noqa: E501
    id: StrictInt
    node_id: StrictStr
    head_branch: Optional[StrictStr]
    head_sha: StrictStr = Field(description="The SHA of the head commit that is being checked.")
    status: Optional[StrictStr] = Field(description="The phase of the lifecycle that the check suite is currently in. Statuses of waiting, requested, and pending are reserved for GitHub Actions check suites.")
    conclusion: Optional[StrictStr]
    url: Optional[StrictStr]
    before: Optional[StrictStr]
    after: Optional[StrictStr]
    pull_requests: Optional[List[PullRequestMinimal]]
    app: Optional[NullableIntegration]
    repository: MinimalRepository
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    head_commit: SimpleCommit
    latest_check_runs_count: StrictInt
    check_runs_url: StrictStr
    rerequestable: Optional[StrictBool] = None
    runs_rerequestable: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "node_id", "head_branch", "head_sha", "status", "conclusion", "url", "before", "after", "pull_requests", "app", "repository", "created_at", "updated_at", "head_commit", "latest_check_runs_count", "check_runs_url", "rerequestable", "runs_rerequestable"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['queued', 'in_progress', 'completed', 'waiting', 'requested', 'pending']):
            raise ValueError("must be one of enum values ('queued', 'in_progress', 'completed', 'waiting', 'requested', 'pending')")
        return value

    @field_validator('conclusion')
    def conclusion_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['success', 'failure', 'neutral', 'cancelled', 'skipped', 'timed_out', 'action_required', 'startup_failure', 'stale']):
            raise ValueError("must be one of enum values ('success', 'failure', 'neutral', 'cancelled', 'skipped', 'timed_out', 'action_required', 'startup_failure', 'stale')")
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
        """Create an instance of CheckSuite from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pull_requests (list)
        _items = []
        if self.pull_requests:
            for _item_pull_requests in self.pull_requests:
                if _item_pull_requests:
                    _items.append(_item_pull_requests.to_dict())
            _dict['pull_requests'] = _items
        # override the default output from pydantic by calling `to_dict()` of app
        if self.app:
            _dict['app'] = self.app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of head_commit
        if self.head_commit:
            _dict['head_commit'] = self.head_commit.to_dict()
        # set to None if head_branch (nullable) is None
        # and model_fields_set contains the field
        if self.head_branch is None and "head_branch" in self.model_fields_set:
            _dict['head_branch'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if conclusion (nullable) is None
        # and model_fields_set contains the field
        if self.conclusion is None and "conclusion" in self.model_fields_set:
            _dict['conclusion'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if before (nullable) is None
        # and model_fields_set contains the field
        if self.before is None and "before" in self.model_fields_set:
            _dict['before'] = None

        # set to None if after (nullable) is None
        # and model_fields_set contains the field
        if self.after is None and "after" in self.model_fields_set:
            _dict['after'] = None

        # set to None if pull_requests (nullable) is None
        # and model_fields_set contains the field
        if self.pull_requests is None and "pull_requests" in self.model_fields_set:
            _dict['pull_requests'] = None

        # set to None if app (nullable) is None
        # and model_fields_set contains the field
        if self.app is None and "app" in self.model_fields_set:
            _dict['app'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CheckSuite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "head_branch": obj.get("head_branch"),
            "head_sha": obj.get("head_sha"),
            "status": obj.get("status"),
            "conclusion": obj.get("conclusion"),
            "url": obj.get("url"),
            "before": obj.get("before"),
            "after": obj.get("after"),
            "pull_requests": [PullRequestMinimal.from_dict(_item) for _item in obj["pull_requests"]] if obj.get("pull_requests") is not None else None,
            "app": NullableIntegration.from_dict(obj["app"]) if obj.get("app") is not None else None,
            "repository": MinimalRepository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "head_commit": SimpleCommit.from_dict(obj["head_commit"]) if obj.get("head_commit") is not None else None,
            "latest_check_runs_count": obj.get("latest_check_runs_count"),
            "check_runs_url": obj.get("check_runs_url"),
            "rerequestable": obj.get("rerequestable"),
            "runs_rerequestable": obj.get("runs_rerequestable")
        })
        return _obj

