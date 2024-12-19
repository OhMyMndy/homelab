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
from typing import Optional, Set
from typing_extensions import Self

class WebhooksRule(BaseModel):
    """
    The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.
    """ # noqa: E501
    admin_enforced: StrictBool
    allow_deletions_enforcement_level: StrictStr
    allow_force_pushes_enforcement_level: StrictStr
    authorized_actor_names: List[StrictStr]
    authorized_actors_only: StrictBool
    authorized_dismissal_actors_only: StrictBool
    create_protected: Optional[StrictBool] = None
    created_at: datetime
    dismiss_stale_reviews_on_push: StrictBool
    id: StrictInt
    ignore_approvals_from_contributors: StrictBool
    linear_history_requirement_enforcement_level: StrictStr
    lock_branch_enforcement_level: StrictStr = Field(description="The enforcement level of the branch lock setting. `off` means the branch is not locked, `non_admins` means the branch is read-only for non_admins, and `everyone` means the branch is read-only for everyone.")
    lock_allows_fork_sync: Optional[StrictBool] = Field(default=None, description="Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow users to pull changes from upstream when the branch is locked. This setting is only applicable for forks.")
    merge_queue_enforcement_level: StrictStr
    name: StrictStr
    pull_request_reviews_enforcement_level: StrictStr
    repository_id: StrictInt
    require_code_owner_review: StrictBool
    require_last_push_approval: Optional[StrictBool] = Field(default=None, description="Whether the most recent push must be approved by someone other than the person who pushed it")
    required_approving_review_count: StrictInt
    required_conversation_resolution_level: StrictStr
    required_deployments_enforcement_level: StrictStr
    required_status_checks: List[StrictStr]
    required_status_checks_enforcement_level: StrictStr
    signature_requirement_enforcement_level: StrictStr
    strict_required_status_checks_policy: StrictBool
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["admin_enforced", "allow_deletions_enforcement_level", "allow_force_pushes_enforcement_level", "authorized_actor_names", "authorized_actors_only", "authorized_dismissal_actors_only", "create_protected", "created_at", "dismiss_stale_reviews_on_push", "id", "ignore_approvals_from_contributors", "linear_history_requirement_enforcement_level", "lock_branch_enforcement_level", "lock_allows_fork_sync", "merge_queue_enforcement_level", "name", "pull_request_reviews_enforcement_level", "repository_id", "require_code_owner_review", "require_last_push_approval", "required_approving_review_count", "required_conversation_resolution_level", "required_deployments_enforcement_level", "required_status_checks", "required_status_checks_enforcement_level", "signature_requirement_enforcement_level", "strict_required_status_checks_policy", "updated_at"]

    @field_validator('allow_deletions_enforcement_level')
    def allow_deletions_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('allow_force_pushes_enforcement_level')
    def allow_force_pushes_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('linear_history_requirement_enforcement_level')
    def linear_history_requirement_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('lock_branch_enforcement_level')
    def lock_branch_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('merge_queue_enforcement_level')
    def merge_queue_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('pull_request_reviews_enforcement_level')
    def pull_request_reviews_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('required_conversation_resolution_level')
    def required_conversation_resolution_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('required_deployments_enforcement_level')
    def required_deployments_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('required_status_checks_enforcement_level')
    def required_status_checks_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
        return value

    @field_validator('signature_requirement_enforcement_level')
    def signature_requirement_enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['off', 'non_admins', 'everyone']):
            raise ValueError("must be one of enum values ('off', 'non_admins', 'everyone')")
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
        """Create an instance of WebhooksRule from a JSON string"""
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
        """Create an instance of WebhooksRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "admin_enforced": obj.get("admin_enforced"),
            "allow_deletions_enforcement_level": obj.get("allow_deletions_enforcement_level"),
            "allow_force_pushes_enforcement_level": obj.get("allow_force_pushes_enforcement_level"),
            "authorized_actor_names": obj.get("authorized_actor_names"),
            "authorized_actors_only": obj.get("authorized_actors_only"),
            "authorized_dismissal_actors_only": obj.get("authorized_dismissal_actors_only"),
            "create_protected": obj.get("create_protected"),
            "created_at": obj.get("created_at"),
            "dismiss_stale_reviews_on_push": obj.get("dismiss_stale_reviews_on_push"),
            "id": obj.get("id"),
            "ignore_approvals_from_contributors": obj.get("ignore_approvals_from_contributors"),
            "linear_history_requirement_enforcement_level": obj.get("linear_history_requirement_enforcement_level"),
            "lock_branch_enforcement_level": obj.get("lock_branch_enforcement_level"),
            "lock_allows_fork_sync": obj.get("lock_allows_fork_sync"),
            "merge_queue_enforcement_level": obj.get("merge_queue_enforcement_level"),
            "name": obj.get("name"),
            "pull_request_reviews_enforcement_level": obj.get("pull_request_reviews_enforcement_level"),
            "repository_id": obj.get("repository_id"),
            "require_code_owner_review": obj.get("require_code_owner_review"),
            "require_last_push_approval": obj.get("require_last_push_approval"),
            "required_approving_review_count": obj.get("required_approving_review_count"),
            "required_conversation_resolution_level": obj.get("required_conversation_resolution_level"),
            "required_deployments_enforcement_level": obj.get("required_deployments_enforcement_level"),
            "required_status_checks": obj.get("required_status_checks"),
            "required_status_checks_enforcement_level": obj.get("required_status_checks_enforcement_level"),
            "signature_requirement_enforcement_level": obj.get("signature_requirement_enforcement_level"),
            "strict_required_status_checks_policy": obj.get("strict_required_status_checks_policy"),
            "updated_at": obj.get("updated_at")
        })
        return _obj

