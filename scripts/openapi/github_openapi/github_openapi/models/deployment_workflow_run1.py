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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.check_run_pull_request import CheckRunPullRequest
from github_openapi.models.deployment_workflow_run1_head_repository import DeploymentWorkflowRun1HeadRepository
from github_openapi.models.deployment_workflow_run_referenced_workflows_inner import DeploymentWorkflowRunReferencedWorkflowsInner
from github_openapi.models.user2 import User2
from typing import Optional, Set
from typing_extensions import Self

class DeploymentWorkflowRun1(BaseModel):
    """
    DeploymentWorkflowRun1
    """ # noqa: E501
    actor: Optional[User2]
    artifacts_url: Optional[StrictStr] = None
    cancel_url: Optional[StrictStr] = None
    check_suite_id: StrictInt
    check_suite_node_id: StrictStr
    check_suite_url: Optional[StrictStr] = None
    conclusion: Optional[StrictStr]
    created_at: datetime
    display_title: StrictStr
    event: StrictStr
    head_branch: StrictStr
    head_commit: Optional[Dict[str, Any]] = None
    head_repository: Optional[DeploymentWorkflowRun1HeadRepository] = None
    head_sha: StrictStr
    html_url: StrictStr
    id: StrictInt
    jobs_url: Optional[StrictStr] = None
    logs_url: Optional[StrictStr] = None
    name: StrictStr
    node_id: StrictStr
    path: StrictStr
    previous_attempt_url: Optional[StrictStr] = None
    pull_requests: List[CheckRunPullRequest]
    referenced_workflows: Optional[List[DeploymentWorkflowRunReferencedWorkflowsInner]] = None
    repository: Optional[DeploymentWorkflowRun1HeadRepository] = None
    rerun_url: Optional[StrictStr] = None
    run_attempt: StrictInt
    run_number: StrictInt
    run_started_at: datetime
    status: StrictStr
    triggering_actor: Optional[User2]
    updated_at: datetime
    url: StrictStr
    workflow_id: StrictInt
    workflow_url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["actor", "artifacts_url", "cancel_url", "check_suite_id", "check_suite_node_id", "check_suite_url", "conclusion", "created_at", "display_title", "event", "head_branch", "head_commit", "head_repository", "head_sha", "html_url", "id", "jobs_url", "logs_url", "name", "node_id", "path", "previous_attempt_url", "pull_requests", "referenced_workflows", "repository", "rerun_url", "run_attempt", "run_number", "run_started_at", "status", "triggering_actor", "updated_at", "url", "workflow_id", "workflow_url"]

    @field_validator('conclusion')
    def conclusion_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['success', 'failure', 'neutral', 'cancelled', 'timed_out', 'action_required', 'stale']):
            raise ValueError("must be one of enum values ('success', 'failure', 'neutral', 'cancelled', 'timed_out', 'action_required', 'stale')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['requested', 'in_progress', 'completed', 'queued', 'waiting', 'pending']):
            raise ValueError("must be one of enum values ('requested', 'in_progress', 'completed', 'queued', 'waiting', 'pending')")
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
        """Create an instance of DeploymentWorkflowRun1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of head_repository
        if self.head_repository:
            _dict['head_repository'] = self.head_repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pull_requests (list)
        _items = []
        if self.pull_requests:
            for _item_pull_requests in self.pull_requests:
                if _item_pull_requests:
                    _items.append(_item_pull_requests.to_dict())
            _dict['pull_requests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in referenced_workflows (list)
        _items = []
        if self.referenced_workflows:
            for _item_referenced_workflows in self.referenced_workflows:
                if _item_referenced_workflows:
                    _items.append(_item_referenced_workflows.to_dict())
            _dict['referenced_workflows'] = _items
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of triggering_actor
        if self.triggering_actor:
            _dict['triggering_actor'] = self.triggering_actor.to_dict()
        # set to None if actor (nullable) is None
        # and model_fields_set contains the field
        if self.actor is None and "actor" in self.model_fields_set:
            _dict['actor'] = None

        # set to None if conclusion (nullable) is None
        # and model_fields_set contains the field
        if self.conclusion is None and "conclusion" in self.model_fields_set:
            _dict['conclusion'] = None

        # set to None if head_commit (nullable) is None
        # and model_fields_set contains the field
        if self.head_commit is None and "head_commit" in self.model_fields_set:
            _dict['head_commit'] = None

        # set to None if previous_attempt_url (nullable) is None
        # and model_fields_set contains the field
        if self.previous_attempt_url is None and "previous_attempt_url" in self.model_fields_set:
            _dict['previous_attempt_url'] = None

        # set to None if referenced_workflows (nullable) is None
        # and model_fields_set contains the field
        if self.referenced_workflows is None and "referenced_workflows" in self.model_fields_set:
            _dict['referenced_workflows'] = None

        # set to None if triggering_actor (nullable) is None
        # and model_fields_set contains the field
        if self.triggering_actor is None and "triggering_actor" in self.model_fields_set:
            _dict['triggering_actor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeploymentWorkflowRun1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actor": User2.from_dict(obj["actor"]) if obj.get("actor") is not None else None,
            "artifacts_url": obj.get("artifacts_url"),
            "cancel_url": obj.get("cancel_url"),
            "check_suite_id": obj.get("check_suite_id"),
            "check_suite_node_id": obj.get("check_suite_node_id"),
            "check_suite_url": obj.get("check_suite_url"),
            "conclusion": obj.get("conclusion"),
            "created_at": obj.get("created_at"),
            "display_title": obj.get("display_title"),
            "event": obj.get("event"),
            "head_branch": obj.get("head_branch"),
            "head_commit": obj.get("head_commit"),
            "head_repository": DeploymentWorkflowRun1HeadRepository.from_dict(obj["head_repository"]) if obj.get("head_repository") is not None else None,
            "head_sha": obj.get("head_sha"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "jobs_url": obj.get("jobs_url"),
            "logs_url": obj.get("logs_url"),
            "name": obj.get("name"),
            "node_id": obj.get("node_id"),
            "path": obj.get("path"),
            "previous_attempt_url": obj.get("previous_attempt_url"),
            "pull_requests": [CheckRunPullRequest.from_dict(_item) for _item in obj["pull_requests"]] if obj.get("pull_requests") is not None else None,
            "referenced_workflows": [DeploymentWorkflowRunReferencedWorkflowsInner.from_dict(_item) for _item in obj["referenced_workflows"]] if obj.get("referenced_workflows") is not None else None,
            "repository": DeploymentWorkflowRun1HeadRepository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "rerun_url": obj.get("rerun_url"),
            "run_attempt": obj.get("run_attempt"),
            "run_number": obj.get("run_number"),
            "run_started_at": obj.get("run_started_at"),
            "status": obj.get("status"),
            "triggering_actor": User2.from_dict(obj["triggering_actor"]) if obj.get("triggering_actor") is not None else None,
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "workflow_id": obj.get("workflow_id"),
            "workflow_url": obj.get("workflow_url")
        })
        return _obj


