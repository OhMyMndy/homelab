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
from github_openapi.models.nullable_license_simple import NullableLicenseSimple
from github_openapi.models.repository_permissions import RepositoryPermissions
from github_openapi.models.simple_user import SimpleUser
from typing import Optional, Set
from typing_extensions import Self

class NullableRepository(BaseModel):
    """
    A repository on GitHub.
    """ # noqa: E501
    id: StrictInt = Field(description="Unique identifier of the repository")
    node_id: StrictStr
    name: StrictStr = Field(description="The name of the repository.")
    full_name: StrictStr
    license: Optional[NullableLicenseSimple]
    forks: StrictInt
    permissions: Optional[RepositoryPermissions] = None
    owner: SimpleUser
    private: StrictBool = Field(description="Whether the repository is private or public.")
    html_url: StrictStr
    description: Optional[StrictStr]
    fork: StrictBool
    url: StrictStr
    archive_url: StrictStr
    assignees_url: StrictStr
    blobs_url: StrictStr
    branches_url: StrictStr
    collaborators_url: StrictStr
    comments_url: StrictStr
    commits_url: StrictStr
    compare_url: StrictStr
    contents_url: StrictStr
    contributors_url: StrictStr
    deployments_url: StrictStr
    downloads_url: StrictStr
    events_url: StrictStr
    forks_url: StrictStr
    git_commits_url: StrictStr
    git_refs_url: StrictStr
    git_tags_url: StrictStr
    git_url: StrictStr
    issue_comment_url: StrictStr
    issue_events_url: StrictStr
    issues_url: StrictStr
    keys_url: StrictStr
    labels_url: StrictStr
    languages_url: StrictStr
    merges_url: StrictStr
    milestones_url: StrictStr
    notifications_url: StrictStr
    pulls_url: StrictStr
    releases_url: StrictStr
    ssh_url: StrictStr
    stargazers_url: StrictStr
    statuses_url: StrictStr
    subscribers_url: StrictStr
    subscription_url: StrictStr
    tags_url: StrictStr
    teams_url: StrictStr
    trees_url: StrictStr
    clone_url: StrictStr
    mirror_url: Optional[StrictStr]
    hooks_url: StrictStr
    svn_url: StrictStr
    homepage: Optional[StrictStr]
    language: Optional[StrictStr]
    forks_count: StrictInt
    stargazers_count: StrictInt
    watchers_count: StrictInt
    size: StrictInt = Field(description="The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.")
    default_branch: StrictStr = Field(description="The default branch of the repository.")
    open_issues_count: StrictInt
    is_template: Optional[StrictBool] = Field(default=False, description="Whether this repository acts as a template that can be used to generate new repositories.")
    topics: Optional[List[StrictStr]] = None
    has_issues: StrictBool = Field(description="Whether issues are enabled.")
    has_projects: StrictBool = Field(description="Whether projects are enabled.")
    has_wiki: StrictBool = Field(description="Whether the wiki is enabled.")
    has_pages: StrictBool
    has_downloads: StrictBool = Field(description="Whether downloads are enabled.")
    has_discussions: Optional[StrictBool] = Field(default=False, description="Whether discussions are enabled.")
    archived: StrictBool = Field(description="Whether the repository is archived.")
    disabled: StrictBool = Field(description="Returns whether or not this repository disabled.")
    visibility: Optional[StrictStr] = Field(default='public', description="The repository visibility: public, private, or internal.")
    pushed_at: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    allow_rebase_merge: Optional[StrictBool] = Field(default=True, description="Whether to allow rebase merges for pull requests.")
    temp_clone_token: Optional[StrictStr] = None
    allow_squash_merge: Optional[StrictBool] = Field(default=True, description="Whether to allow squash merges for pull requests.")
    allow_auto_merge: Optional[StrictBool] = Field(default=False, description="Whether to allow Auto-merge to be used on pull requests.")
    delete_branch_on_merge: Optional[StrictBool] = Field(default=False, description="Whether to delete head branches when pull requests are merged")
    allow_update_branch: Optional[StrictBool] = Field(default=False, description="Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.")
    use_squash_pr_title_as_default: Optional[StrictBool] = Field(default=False, description="Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use `squash_merge_commit_title` instead.")
    squash_merge_commit_title: Optional[StrictStr] = Field(default=None, description="The default value for a squash merge commit title:  - `PR_TITLE` - default to the pull request's title. - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).")
    squash_merge_commit_message: Optional[StrictStr] = Field(default=None, description="The default value for a squash merge commit message:  - `PR_BODY` - default to the pull request's body. - `COMMIT_MESSAGES` - default to the branch's commit messages. - `BLANK` - default to a blank commit message.")
    merge_commit_title: Optional[StrictStr] = Field(default=None, description="The default value for a merge commit title.  - `PR_TITLE` - default to the pull request's title. - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).")
    merge_commit_message: Optional[StrictStr] = Field(default=None, description="The default value for a merge commit message.  - `PR_TITLE` - default to the pull request's title. - `PR_BODY` - default to the pull request's body. - `BLANK` - default to a blank commit message.")
    allow_merge_commit: Optional[StrictBool] = Field(default=True, description="Whether to allow merge commits for pull requests.")
    allow_forking: Optional[StrictBool] = Field(default=None, description="Whether to allow forking this repo")
    web_commit_signoff_required: Optional[StrictBool] = Field(default=False, description="Whether to require contributors to sign off on web-based commits")
    open_issues: StrictInt
    watchers: StrictInt
    master_branch: Optional[StrictStr] = None
    starred_at: Optional[StrictStr] = None
    anonymous_access_enabled: Optional[StrictBool] = Field(default=None, description="Whether anonymous git access is enabled for this repository")
    __properties: ClassVar[List[str]] = ["id", "node_id", "name", "full_name", "license", "forks", "permissions", "owner", "private", "html_url", "description", "fork", "url", "archive_url", "assignees_url", "blobs_url", "branches_url", "collaborators_url", "comments_url", "commits_url", "compare_url", "contents_url", "contributors_url", "deployments_url", "downloads_url", "events_url", "forks_url", "git_commits_url", "git_refs_url", "git_tags_url", "git_url", "issue_comment_url", "issue_events_url", "issues_url", "keys_url", "labels_url", "languages_url", "merges_url", "milestones_url", "notifications_url", "pulls_url", "releases_url", "ssh_url", "stargazers_url", "statuses_url", "subscribers_url", "subscription_url", "tags_url", "teams_url", "trees_url", "clone_url", "mirror_url", "hooks_url", "svn_url", "homepage", "language", "forks_count", "stargazers_count", "watchers_count", "size", "default_branch", "open_issues_count", "is_template", "topics", "has_issues", "has_projects", "has_wiki", "has_pages", "has_downloads", "has_discussions", "archived", "disabled", "visibility", "pushed_at", "created_at", "updated_at", "allow_rebase_merge", "temp_clone_token", "allow_squash_merge", "allow_auto_merge", "delete_branch_on_merge", "allow_update_branch", "use_squash_pr_title_as_default", "squash_merge_commit_title", "squash_merge_commit_message", "merge_commit_title", "merge_commit_message", "allow_merge_commit", "allow_forking", "web_commit_signoff_required", "open_issues", "watchers", "master_branch", "starred_at", "anonymous_access_enabled"]

    @field_validator('squash_merge_commit_title')
    def squash_merge_commit_title_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PR_TITLE', 'COMMIT_OR_PR_TITLE']):
            raise ValueError("must be one of enum values ('PR_TITLE', 'COMMIT_OR_PR_TITLE')")
        return value

    @field_validator('squash_merge_commit_message')
    def squash_merge_commit_message_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PR_BODY', 'COMMIT_MESSAGES', 'BLANK']):
            raise ValueError("must be one of enum values ('PR_BODY', 'COMMIT_MESSAGES', 'BLANK')")
        return value

    @field_validator('merge_commit_title')
    def merge_commit_title_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PR_TITLE', 'MERGE_MESSAGE']):
            raise ValueError("must be one of enum values ('PR_TITLE', 'MERGE_MESSAGE')")
        return value

    @field_validator('merge_commit_message')
    def merge_commit_message_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PR_BODY', 'PR_TITLE', 'BLANK']):
            raise ValueError("must be one of enum values ('PR_BODY', 'PR_TITLE', 'BLANK')")
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
        """Create an instance of NullableRepository from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of license
        if self.license:
            _dict['license'] = self.license.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # set to None if license (nullable) is None
        # and model_fields_set contains the field
        if self.license is None and "license" in self.model_fields_set:
            _dict['license'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if mirror_url (nullable) is None
        # and model_fields_set contains the field
        if self.mirror_url is None and "mirror_url" in self.model_fields_set:
            _dict['mirror_url'] = None

        # set to None if homepage (nullable) is None
        # and model_fields_set contains the field
        if self.homepage is None and "homepage" in self.model_fields_set:
            _dict['homepage'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if pushed_at (nullable) is None
        # and model_fields_set contains the field
        if self.pushed_at is None and "pushed_at" in self.model_fields_set:
            _dict['pushed_at'] = None

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
        """Create an instance of NullableRepository from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "name": obj.get("name"),
            "full_name": obj.get("full_name"),
            "license": NullableLicenseSimple.from_dict(obj["license"]) if obj.get("license") is not None else None,
            "forks": obj.get("forks"),
            "permissions": RepositoryPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "owner": SimpleUser.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "private": obj.get("private") if obj.get("private") is not None else False,
            "html_url": obj.get("html_url"),
            "description": obj.get("description"),
            "fork": obj.get("fork"),
            "url": obj.get("url"),
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
            "downloads_url": obj.get("downloads_url"),
            "events_url": obj.get("events_url"),
            "forks_url": obj.get("forks_url"),
            "git_commits_url": obj.get("git_commits_url"),
            "git_refs_url": obj.get("git_refs_url"),
            "git_tags_url": obj.get("git_tags_url"),
            "git_url": obj.get("git_url"),
            "issue_comment_url": obj.get("issue_comment_url"),
            "issue_events_url": obj.get("issue_events_url"),
            "issues_url": obj.get("issues_url"),
            "keys_url": obj.get("keys_url"),
            "labels_url": obj.get("labels_url"),
            "languages_url": obj.get("languages_url"),
            "merges_url": obj.get("merges_url"),
            "milestones_url": obj.get("milestones_url"),
            "notifications_url": obj.get("notifications_url"),
            "pulls_url": obj.get("pulls_url"),
            "releases_url": obj.get("releases_url"),
            "ssh_url": obj.get("ssh_url"),
            "stargazers_url": obj.get("stargazers_url"),
            "statuses_url": obj.get("statuses_url"),
            "subscribers_url": obj.get("subscribers_url"),
            "subscription_url": obj.get("subscription_url"),
            "tags_url": obj.get("tags_url"),
            "teams_url": obj.get("teams_url"),
            "trees_url": obj.get("trees_url"),
            "clone_url": obj.get("clone_url"),
            "mirror_url": obj.get("mirror_url"),
            "hooks_url": obj.get("hooks_url"),
            "svn_url": obj.get("svn_url"),
            "homepage": obj.get("homepage"),
            "language": obj.get("language"),
            "forks_count": obj.get("forks_count"),
            "stargazers_count": obj.get("stargazers_count"),
            "watchers_count": obj.get("watchers_count"),
            "size": obj.get("size"),
            "default_branch": obj.get("default_branch"),
            "open_issues_count": obj.get("open_issues_count"),
            "is_template": obj.get("is_template") if obj.get("is_template") is not None else False,
            "topics": obj.get("topics"),
            "has_issues": obj.get("has_issues") if obj.get("has_issues") is not None else True,
            "has_projects": obj.get("has_projects") if obj.get("has_projects") is not None else True,
            "has_wiki": obj.get("has_wiki") if obj.get("has_wiki") is not None else True,
            "has_pages": obj.get("has_pages"),
            "has_downloads": obj.get("has_downloads") if obj.get("has_downloads") is not None else True,
            "has_discussions": obj.get("has_discussions") if obj.get("has_discussions") is not None else False,
            "archived": obj.get("archived") if obj.get("archived") is not None else False,
            "disabled": obj.get("disabled"),
            "visibility": obj.get("visibility") if obj.get("visibility") is not None else 'public',
            "pushed_at": obj.get("pushed_at"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "allow_rebase_merge": obj.get("allow_rebase_merge") if obj.get("allow_rebase_merge") is not None else True,
            "temp_clone_token": obj.get("temp_clone_token"),
            "allow_squash_merge": obj.get("allow_squash_merge") if obj.get("allow_squash_merge") is not None else True,
            "allow_auto_merge": obj.get("allow_auto_merge") if obj.get("allow_auto_merge") is not None else False,
            "delete_branch_on_merge": obj.get("delete_branch_on_merge") if obj.get("delete_branch_on_merge") is not None else False,
            "allow_update_branch": obj.get("allow_update_branch") if obj.get("allow_update_branch") is not None else False,
            "use_squash_pr_title_as_default": obj.get("use_squash_pr_title_as_default") if obj.get("use_squash_pr_title_as_default") is not None else False,
            "squash_merge_commit_title": obj.get("squash_merge_commit_title"),
            "squash_merge_commit_message": obj.get("squash_merge_commit_message"),
            "merge_commit_title": obj.get("merge_commit_title"),
            "merge_commit_message": obj.get("merge_commit_message"),
            "allow_merge_commit": obj.get("allow_merge_commit") if obj.get("allow_merge_commit") is not None else True,
            "allow_forking": obj.get("allow_forking"),
            "web_commit_signoff_required": obj.get("web_commit_signoff_required") if obj.get("web_commit_signoff_required") is not None else False,
            "open_issues": obj.get("open_issues"),
            "watchers": obj.get("watchers"),
            "master_branch": obj.get("master_branch"),
            "starred_at": obj.get("starred_at"),
            "anonymous_access_enabled": obj.get("anonymous_access_enabled")
        })
        return _obj


