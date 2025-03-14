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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ReposCreateForAuthenticatedUserRequest(BaseModel):
    """
    ReposCreateForAuthenticatedUserRequest
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the repository.")
    description: Optional[StrictStr] = Field(default=None, description="A short description of the repository.")
    homepage: Optional[StrictStr] = Field(default=None, description="A URL with more information about the repository.")
    private: Optional[StrictBool] = Field(default=False, description="Whether the repository is private.")
    has_issues: Optional[StrictBool] = Field(default=True, description="Whether issues are enabled.")
    has_projects: Optional[StrictBool] = Field(default=True, description="Whether projects are enabled.")
    has_wiki: Optional[StrictBool] = Field(default=True, description="Whether the wiki is enabled.")
    has_discussions: Optional[StrictBool] = Field(default=False, description="Whether discussions are enabled.")
    team_id: Optional[StrictInt] = Field(default=None, description="The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization.")
    auto_init: Optional[StrictBool] = Field(default=False, description="Whether the repository is initialized with a minimal README.")
    gitignore_template: Optional[StrictStr] = Field(default=None, description="The desired language or platform to apply to the .gitignore.")
    license_template: Optional[StrictStr] = Field(default=None, description="The license keyword of the open source license for this repository.")
    allow_squash_merge: Optional[StrictBool] = Field(default=True, description="Whether to allow squash merges for pull requests.")
    allow_merge_commit: Optional[StrictBool] = Field(default=True, description="Whether to allow merge commits for pull requests.")
    allow_rebase_merge: Optional[StrictBool] = Field(default=True, description="Whether to allow rebase merges for pull requests.")
    allow_auto_merge: Optional[StrictBool] = Field(default=False, description="Whether to allow Auto-merge to be used on pull requests.")
    delete_branch_on_merge: Optional[StrictBool] = Field(default=False, description="Whether to delete head branches when pull requests are merged")
    squash_merge_commit_title: Optional[StrictStr] = Field(default=None, description="Required when using `squash_merge_commit_message`.  The default value for a squash merge commit title:  - `PR_TITLE` - default to the pull request's title. - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or the pull request's title (when more than one commit).")
    squash_merge_commit_message: Optional[StrictStr] = Field(default=None, description="The default value for a squash merge commit message:  - `PR_BODY` - default to the pull request's body. - `COMMIT_MESSAGES` - default to the branch's commit messages. - `BLANK` - default to a blank commit message.")
    merge_commit_title: Optional[StrictStr] = Field(default=None, description="Required when using `merge_commit_message`.  The default value for a merge commit title.  - `PR_TITLE` - default to the pull request's title. - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).")
    merge_commit_message: Optional[StrictStr] = Field(default=None, description="The default value for a merge commit message.  - `PR_TITLE` - default to the pull request's title. - `PR_BODY` - default to the pull request's body. - `BLANK` - default to a blank commit message.")
    has_downloads: Optional[StrictBool] = Field(default=True, description="Whether downloads are enabled.")
    is_template: Optional[StrictBool] = Field(default=False, description="Whether this repository acts as a template that can be used to generate new repositories.")
    __properties: ClassVar[List[str]] = ["name", "description", "homepage", "private", "has_issues", "has_projects", "has_wiki", "has_discussions", "team_id", "auto_init", "gitignore_template", "license_template", "allow_squash_merge", "allow_merge_commit", "allow_rebase_merge", "allow_auto_merge", "delete_branch_on_merge", "squash_merge_commit_title", "squash_merge_commit_message", "merge_commit_title", "merge_commit_message", "has_downloads", "is_template"]

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
        """Create an instance of ReposCreateForAuthenticatedUserRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReposCreateForAuthenticatedUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "homepage": obj.get("homepage"),
            "private": obj.get("private") if obj.get("private") is not None else False,
            "has_issues": obj.get("has_issues") if obj.get("has_issues") is not None else True,
            "has_projects": obj.get("has_projects") if obj.get("has_projects") is not None else True,
            "has_wiki": obj.get("has_wiki") if obj.get("has_wiki") is not None else True,
            "has_discussions": obj.get("has_discussions") if obj.get("has_discussions") is not None else False,
            "team_id": obj.get("team_id"),
            "auto_init": obj.get("auto_init") if obj.get("auto_init") is not None else False,
            "gitignore_template": obj.get("gitignore_template"),
            "license_template": obj.get("license_template"),
            "allow_squash_merge": obj.get("allow_squash_merge") if obj.get("allow_squash_merge") is not None else True,
            "allow_merge_commit": obj.get("allow_merge_commit") if obj.get("allow_merge_commit") is not None else True,
            "allow_rebase_merge": obj.get("allow_rebase_merge") if obj.get("allow_rebase_merge") is not None else True,
            "allow_auto_merge": obj.get("allow_auto_merge") if obj.get("allow_auto_merge") is not None else False,
            "delete_branch_on_merge": obj.get("delete_branch_on_merge") if obj.get("delete_branch_on_merge") is not None else False,
            "squash_merge_commit_title": obj.get("squash_merge_commit_title"),
            "squash_merge_commit_message": obj.get("squash_merge_commit_message"),
            "merge_commit_title": obj.get("merge_commit_title"),
            "merge_commit_message": obj.get("merge_commit_message"),
            "has_downloads": obj.get("has_downloads") if obj.get("has_downloads") is not None else True,
            "is_template": obj.get("is_template") if obj.get("is_template") is not None else False
        })
        return _obj


