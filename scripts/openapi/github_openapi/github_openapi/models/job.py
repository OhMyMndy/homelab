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
from github_openapi.models.job_steps_inner import JobStepsInner
from typing import Optional, Set
from typing_extensions import Self

class Job(BaseModel):
    """
    Information of a job execution in a workflow run
    """ # noqa: E501
    id: StrictInt = Field(description="The id of the job.")
    run_id: StrictInt = Field(description="The id of the associated workflow run.")
    run_url: StrictStr
    run_attempt: Optional[StrictInt] = Field(default=None, description="Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run.")
    node_id: StrictStr
    head_sha: StrictStr = Field(description="The SHA of the commit that is being run.")
    url: StrictStr
    html_url: Optional[StrictStr]
    status: StrictStr = Field(description="The phase of the lifecycle that the job is currently in.")
    conclusion: Optional[StrictStr] = Field(description="The outcome of the job.")
    created_at: datetime = Field(description="The time that the job created, in ISO 8601 format.")
    started_at: datetime = Field(description="The time that the job started, in ISO 8601 format.")
    completed_at: Optional[datetime] = Field(description="The time that the job finished, in ISO 8601 format.")
    name: StrictStr = Field(description="The name of the job.")
    steps: Optional[List[JobStepsInner]] = Field(default=None, description="Steps in this job.")
    check_run_url: StrictStr
    labels: List[StrictStr] = Field(description="Labels for the workflow job. Specified by the \"runs_on\" attribute in the action's workflow file.")
    runner_id: Optional[StrictInt] = Field(description="The ID of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)")
    runner_name: Optional[StrictStr] = Field(description="The name of the runner to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)")
    runner_group_id: Optional[StrictInt] = Field(description="The ID of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)")
    runner_group_name: Optional[StrictStr] = Field(description="The name of the runner group to which this job has been assigned. (If a runner hasn't yet been assigned, this will be null.)")
    workflow_name: Optional[StrictStr] = Field(description="The name of the workflow.")
    head_branch: Optional[StrictStr] = Field(description="The name of the current branch.")
    __properties: ClassVar[List[str]] = ["id", "run_id", "run_url", "run_attempt", "node_id", "head_sha", "url", "html_url", "status", "conclusion", "created_at", "started_at", "completed_at", "name", "steps", "check_run_url", "labels", "runner_id", "runner_name", "runner_group_id", "runner_group_name", "workflow_name", "head_branch"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['queued', 'in_progress', 'completed', 'waiting', 'requested', 'pending']):
            raise ValueError("must be one of enum values ('queued', 'in_progress', 'completed', 'waiting', 'requested', 'pending')")
        return value

    @field_validator('conclusion')
    def conclusion_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['success', 'failure', 'neutral', 'cancelled', 'skipped', 'timed_out', 'action_required']):
            raise ValueError("must be one of enum values ('success', 'failure', 'neutral', 'cancelled', 'skipped', 'timed_out', 'action_required')")
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
        """Create an instance of Job from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # set to None if html_url (nullable) is None
        # and model_fields_set contains the field
        if self.html_url is None and "html_url" in self.model_fields_set:
            _dict['html_url'] = None

        # set to None if conclusion (nullable) is None
        # and model_fields_set contains the field
        if self.conclusion is None and "conclusion" in self.model_fields_set:
            _dict['conclusion'] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completed_at'] = None

        # set to None if runner_id (nullable) is None
        # and model_fields_set contains the field
        if self.runner_id is None and "runner_id" in self.model_fields_set:
            _dict['runner_id'] = None

        # set to None if runner_name (nullable) is None
        # and model_fields_set contains the field
        if self.runner_name is None and "runner_name" in self.model_fields_set:
            _dict['runner_name'] = None

        # set to None if runner_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.runner_group_id is None and "runner_group_id" in self.model_fields_set:
            _dict['runner_group_id'] = None

        # set to None if runner_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.runner_group_name is None and "runner_group_name" in self.model_fields_set:
            _dict['runner_group_name'] = None

        # set to None if workflow_name (nullable) is None
        # and model_fields_set contains the field
        if self.workflow_name is None and "workflow_name" in self.model_fields_set:
            _dict['workflow_name'] = None

        # set to None if head_branch (nullable) is None
        # and model_fields_set contains the field
        if self.head_branch is None and "head_branch" in self.model_fields_set:
            _dict['head_branch'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Job from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "run_id": obj.get("run_id"),
            "run_url": obj.get("run_url"),
            "run_attempt": obj.get("run_attempt"),
            "node_id": obj.get("node_id"),
            "head_sha": obj.get("head_sha"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "status": obj.get("status"),
            "conclusion": obj.get("conclusion"),
            "created_at": obj.get("created_at"),
            "started_at": obj.get("started_at"),
            "completed_at": obj.get("completed_at"),
            "name": obj.get("name"),
            "steps": [JobStepsInner.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "check_run_url": obj.get("check_run_url"),
            "labels": obj.get("labels"),
            "runner_id": obj.get("runner_id"),
            "runner_name": obj.get("runner_name"),
            "runner_group_id": obj.get("runner_group_id"),
            "runner_group_name": obj.get("runner_group_name"),
            "workflow_name": obj.get("workflow_name"),
            "head_branch": obj.get("head_branch")
        })
        return _obj

