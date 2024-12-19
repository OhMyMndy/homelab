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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.deployment_workflow_run_head_repository_owner import DeploymentWorkflowRunHeadRepositoryOwner
from typing import Optional, Set
from typing_extensions import Self

class DeploymentWorkflowRunHeadRepository(BaseModel):
    """
    DeploymentWorkflowRunHeadRepository
    """ # noqa: E501
    archive_url: Optional[StrictStr] = None
    assignees_url: Optional[StrictStr] = None
    blobs_url: Optional[StrictStr] = None
    branches_url: Optional[StrictStr] = None
    collaborators_url: Optional[StrictStr] = None
    comments_url: Optional[StrictStr] = None
    commits_url: Optional[StrictStr] = None
    compare_url: Optional[StrictStr] = None
    contents_url: Optional[StrictStr] = None
    contributors_url: Optional[StrictStr] = None
    deployments_url: Optional[StrictStr] = None
    description: Optional[Any] = None
    downloads_url: Optional[StrictStr] = None
    events_url: Optional[StrictStr] = None
    fork: Optional[StrictBool] = None
    forks_url: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    git_commits_url: Optional[StrictStr] = None
    git_refs_url: Optional[StrictStr] = None
    git_tags_url: Optional[StrictStr] = None
    hooks_url: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    issue_comment_url: Optional[StrictStr] = None
    issue_events_url: Optional[StrictStr] = None
    issues_url: Optional[StrictStr] = None
    keys_url: Optional[StrictStr] = None
    labels_url: Optional[StrictStr] = None
    languages_url: Optional[StrictStr] = None
    merges_url: Optional[StrictStr] = None
    milestones_url: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    node_id: Optional[StrictStr] = None
    notifications_url: Optional[StrictStr] = None
    owner: Optional[DeploymentWorkflowRunHeadRepositoryOwner] = None
    private: Optional[StrictBool] = None
    pulls_url: Optional[StrictStr] = None
    releases_url: Optional[StrictStr] = None
    stargazers_url: Optional[StrictStr] = None
    statuses_url: Optional[StrictStr] = None
    subscribers_url: Optional[StrictStr] = None
    subscription_url: Optional[StrictStr] = None
    tags_url: Optional[StrictStr] = None
    teams_url: Optional[StrictStr] = None
    trees_url: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["archive_url", "assignees_url", "blobs_url", "branches_url", "collaborators_url", "comments_url", "commits_url", "compare_url", "contents_url", "contributors_url", "deployments_url", "description", "downloads_url", "events_url", "fork", "forks_url", "full_name", "git_commits_url", "git_refs_url", "git_tags_url", "hooks_url", "html_url", "id", "issue_comment_url", "issue_events_url", "issues_url", "keys_url", "labels_url", "languages_url", "merges_url", "milestones_url", "name", "node_id", "notifications_url", "owner", "private", "pulls_url", "releases_url", "stargazers_url", "statuses_url", "subscribers_url", "subscription_url", "tags_url", "teams_url", "trees_url", "url"]

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
        """Create an instance of DeploymentWorkflowRunHeadRepository from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeploymentWorkflowRunHeadRepository from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archive_url": obj.get("archive_url"),
            "assignees_url": obj.get("assignees_url"),
            "blobs_url": obj.get("blobs_url"),
            "branches_url": obj.get("branches_url"),
            "collaborators_url": obj.get("collaborators_url"),
            "comments_url": obj.get("comments_url"),
            "commits_url": obj.get("commits_url"),
            "compare_url": obj.get("compare_url"),
            "contents_url": obj.get("contents_url"),
            "contributors_url": obj.get("contributors_url"),
            "deployments_url": obj.get("deployments_url"),
            "description": obj.get("description"),
            "downloads_url": obj.get("downloads_url"),
            "events_url": obj.get("events_url"),
            "fork": obj.get("fork"),
            "forks_url": obj.get("forks_url"),
            "full_name": obj.get("full_name"),
            "git_commits_url": obj.get("git_commits_url"),
            "git_refs_url": obj.get("git_refs_url"),
            "git_tags_url": obj.get("git_tags_url"),
            "hooks_url": obj.get("hooks_url"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "issue_comment_url": obj.get("issue_comment_url"),
            "issue_events_url": obj.get("issue_events_url"),
            "issues_url": obj.get("issues_url"),
            "keys_url": obj.get("keys_url"),
            "labels_url": obj.get("labels_url"),
            "languages_url": obj.get("languages_url"),
            "merges_url": obj.get("merges_url"),
            "milestones_url": obj.get("milestones_url"),
            "name": obj.get("name"),
            "node_id": obj.get("node_id"),
            "notifications_url": obj.get("notifications_url"),
            "owner": DeploymentWorkflowRunHeadRepositoryOwner.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "private": obj.get("private"),
            "pulls_url": obj.get("pulls_url"),
            "releases_url": obj.get("releases_url"),
            "stargazers_url": obj.get("stargazers_url"),
            "statuses_url": obj.get("statuses_url"),
            "subscribers_url": obj.get("subscribers_url"),
            "subscription_url": obj.get("subscription_url"),
            "tags_url": obj.get("tags_url"),
            "teams_url": obj.get("teams_url"),
            "trees_url": obj.get("trees_url"),
            "url": obj.get("url")
        })
        return _obj


