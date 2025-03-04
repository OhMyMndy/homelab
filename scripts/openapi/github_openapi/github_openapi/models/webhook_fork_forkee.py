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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.deployment_workflow_run_head_repository_owner import DeploymentWorkflowRunHeadRepositoryOwner
from github_openapi.models.repository_permissions import RepositoryPermissions
from typing import Optional, Set
from typing_extensions import Self

class WebhookForkForkee(BaseModel):
    """
    The created [`repository`](https://docs.github.com/rest/repos/repos#get-a-repository) resource.
    """ # noqa: E501
    allow_auto_merge: Optional[StrictBool] = Field(default=False, description="Whether to allow auto-merge for pull requests.")
    allow_forking: Optional[StrictBool] = None
    allow_merge_commit: Optional[StrictBool] = Field(default=True, description="Whether to allow merge commits for pull requests.")
    allow_rebase_merge: Optional[StrictBool] = Field(default=True, description="Whether to allow rebase merges for pull requests.")
    allow_squash_merge: Optional[StrictBool] = Field(default=True, description="Whether to allow squash merges for pull requests.")
    allow_update_branch: Optional[StrictBool] = None
    archive_url: StrictStr
    archived: StrictBool
    assignees_url: StrictStr
    blobs_url: StrictStr
    branches_url: StrictStr
    clone_url: StrictStr
    collaborators_url: StrictStr
    comments_url: StrictStr
    commits_url: StrictStr
    compare_url: StrictStr
    contents_url: StrictStr
    contributors_url: StrictStr
    created_at: StrictStr
    default_branch: StrictStr
    delete_branch_on_merge: Optional[StrictBool] = Field(default=False, description="Whether to delete head branches when pull requests are merged")
    deployments_url: StrictStr
    description: Optional[StrictStr]
    disabled: Optional[StrictBool] = None
    downloads_url: StrictStr
    events_url: StrictStr
    fork: StrictBool
    forks: StrictInt
    forks_count: StrictInt
    forks_url: StrictStr
    full_name: StrictStr
    git_commits_url: StrictStr
    git_refs_url: StrictStr
    git_tags_url: StrictStr
    git_url: StrictStr
    has_downloads: StrictBool
    has_issues: StrictBool
    has_pages: StrictBool
    has_projects: StrictBool
    has_wiki: StrictBool
    homepage: Optional[StrictStr]
    hooks_url: StrictStr
    html_url: StrictStr
    id: StrictInt
    is_template: Optional[StrictBool] = None
    issue_comment_url: StrictStr
    issue_events_url: StrictStr
    issues_url: StrictStr
    keys_url: StrictStr
    labels_url: StrictStr
    language: Optional[Any]
    languages_url: StrictStr
    license: Optional[Dict[str, Any]]
    master_branch: Optional[StrictStr] = None
    merges_url: StrictStr
    milestones_url: StrictStr
    mirror_url: Optional[Any]
    name: StrictStr
    node_id: StrictStr
    notifications_url: StrictStr
    open_issues: StrictInt
    open_issues_count: StrictInt
    organization: Optional[StrictStr] = None
    owner: DeploymentWorkflowRunHeadRepositoryOwner
    permissions: Optional[RepositoryPermissions] = None
    private: StrictBool
    public: Optional[StrictBool] = None
    pulls_url: StrictStr
    pushed_at: StrictStr
    releases_url: StrictStr
    role_name: Optional[StrictStr] = None
    size: StrictInt
    ssh_url: StrictStr
    stargazers: Optional[StrictInt] = None
    stargazers_count: StrictInt
    stargazers_url: StrictStr
    statuses_url: StrictStr
    subscribers_url: StrictStr
    subscription_url: StrictStr
    svn_url: StrictStr
    tags_url: StrictStr
    teams_url: StrictStr
    topics: List[Any]
    trees_url: StrictStr
    updated_at: StrictStr
    url: StrictStr
    visibility: StrictStr
    watchers: StrictInt
    watchers_count: StrictInt
    web_commit_signoff_required: Optional[StrictBool] = Field(default=None, description="Whether to require contributors to sign off on web-based commits")
    __properties: ClassVar[List[str]] = ["allow_auto_merge", "allow_forking", "allow_merge_commit", "allow_rebase_merge", "allow_squash_merge", "allow_update_branch", "archive_url", "archived", "assignees_url", "blobs_url", "branches_url", "clone_url", "collaborators_url", "comments_url", "commits_url", "compare_url", "contents_url", "contributors_url", "created_at", "default_branch", "delete_branch_on_merge", "deployments_url", "description", "disabled", "downloads_url", "events_url", "fork", "forks", "forks_count", "forks_url", "full_name", "git_commits_url", "git_refs_url", "git_tags_url", "git_url", "has_downloads", "has_issues", "has_pages", "has_projects", "has_wiki", "homepage", "hooks_url", "html_url", "id", "is_template", "issue_comment_url", "issue_events_url", "issues_url", "keys_url", "labels_url", "language", "languages_url", "license", "master_branch", "merges_url", "milestones_url", "mirror_url", "name", "node_id", "notifications_url", "open_issues", "open_issues_count", "organization", "owner", "permissions", "private", "public", "pulls_url", "pushed_at", "releases_url", "role_name", "size", "ssh_url", "stargazers", "stargazers_count", "stargazers_url", "statuses_url", "subscribers_url", "subscription_url", "svn_url", "tags_url", "teams_url", "topics", "trees_url", "updated_at", "url", "visibility", "watchers", "watchers_count", "web_commit_signoff_required"]

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
        """Create an instance of WebhookForkForkee from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if homepage (nullable) is None
        # and model_fields_set contains the field
        if self.homepage is None and "homepage" in self.model_fields_set:
            _dict['homepage'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if license (nullable) is None
        # and model_fields_set contains the field
        if self.license is None and "license" in self.model_fields_set:
            _dict['license'] = None

        # set to None if mirror_url (nullable) is None
        # and model_fields_set contains the field
        if self.mirror_url is None and "mirror_url" in self.model_fields_set:
            _dict['mirror_url'] = None

        # set to None if role_name (nullable) is None
        # and model_fields_set contains the field
        if self.role_name is None and "role_name" in self.model_fields_set:
            _dict['role_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookForkForkee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allow_auto_merge": obj.get("allow_auto_merge") if obj.get("allow_auto_merge") is not None else False,
            "allow_forking": obj.get("allow_forking"),
            "allow_merge_commit": obj.get("allow_merge_commit") if obj.get("allow_merge_commit") is not None else True,
            "allow_rebase_merge": obj.get("allow_rebase_merge") if obj.get("allow_rebase_merge") is not None else True,
            "allow_squash_merge": obj.get("allow_squash_merge") if obj.get("allow_squash_merge") is not None else True,
            "allow_update_branch": obj.get("allow_update_branch"),
            "archive_url": obj.get("archive_url"),
            "archived": obj.get("archived"),
            "assignees_url": obj.get("assignees_url"),
            "blobs_url": obj.get("blobs_url"),
            "branches_url": obj.get("branches_url"),
            "clone_url": obj.get("clone_url"),
            "collaborators_url": obj.get("collaborators_url"),
            "comments_url": obj.get("comments_url"),
            "commits_url": obj.get("commits_url"),
            "compare_url": obj.get("compare_url"),
            "contents_url": obj.get("contents_url"),
            "contributors_url": obj.get("contributors_url"),
            "created_at": obj.get("created_at"),
            "default_branch": obj.get("default_branch"),
            "delete_branch_on_merge": obj.get("delete_branch_on_merge") if obj.get("delete_branch_on_merge") is not None else False,
            "deployments_url": obj.get("deployments_url"),
            "description": obj.get("description"),
            "disabled": obj.get("disabled"),
            "downloads_url": obj.get("downloads_url"),
            "events_url": obj.get("events_url"),
            "fork": obj.get("fork"),
            "forks": obj.get("forks"),
            "forks_count": obj.get("forks_count"),
            "forks_url": obj.get("forks_url"),
            "full_name": obj.get("full_name"),
            "git_commits_url": obj.get("git_commits_url"),
            "git_refs_url": obj.get("git_refs_url"),
            "git_tags_url": obj.get("git_tags_url"),
            "git_url": obj.get("git_url"),
            "has_downloads": obj.get("has_downloads"),
            "has_issues": obj.get("has_issues"),
            "has_pages": obj.get("has_pages"),
            "has_projects": obj.get("has_projects"),
            "has_wiki": obj.get("has_wiki"),
            "homepage": obj.get("homepage"),
            "hooks_url": obj.get("hooks_url"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "is_template": obj.get("is_template"),
            "issue_comment_url": obj.get("issue_comment_url"),
            "issue_events_url": obj.get("issue_events_url"),
            "issues_url": obj.get("issues_url"),
            "keys_url": obj.get("keys_url"),
            "labels_url": obj.get("labels_url"),
            "language": obj.get("language"),
            "languages_url": obj.get("languages_url"),
            "license": obj.get("license"),
            "master_branch": obj.get("master_branch"),
            "merges_url": obj.get("merges_url"),
            "milestones_url": obj.get("milestones_url"),
            "mirror_url": obj.get("mirror_url"),
            "name": obj.get("name"),
            "node_id": obj.get("node_id"),
            "notifications_url": obj.get("notifications_url"),
            "open_issues": obj.get("open_issues"),
            "open_issues_count": obj.get("open_issues_count"),
            "organization": obj.get("organization"),
            "owner": DeploymentWorkflowRunHeadRepositoryOwner.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "permissions": RepositoryPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "private": obj.get("private"),
            "public": obj.get("public"),
            "pulls_url": obj.get("pulls_url"),
            "pushed_at": obj.get("pushed_at"),
            "releases_url": obj.get("releases_url"),
            "role_name": obj.get("role_name"),
            "size": obj.get("size"),
            "ssh_url": obj.get("ssh_url"),
            "stargazers": obj.get("stargazers"),
            "stargazers_count": obj.get("stargazers_count"),
            "stargazers_url": obj.get("stargazers_url"),
            "statuses_url": obj.get("statuses_url"),
            "subscribers_url": obj.get("subscribers_url"),
            "subscription_url": obj.get("subscription_url"),
            "svn_url": obj.get("svn_url"),
            "tags_url": obj.get("tags_url"),
            "teams_url": obj.get("teams_url"),
            "topics": obj.get("topics"),
            "trees_url": obj.get("trees_url"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "visibility": obj.get("visibility"),
            "watchers": obj.get("watchers"),
            "watchers_count": obj.get("watchers_count"),
            "web_commit_signoff_required": obj.get("web_commit_signoff_required")
        })
        return _obj


