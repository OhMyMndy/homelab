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
from github_openapi.models.app_permissions import AppPermissions
from github_openapi.models.user2 import User2
from typing import Optional, Set
from typing_extensions import Self

class App11(BaseModel):
    """
    GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    """ # noqa: E501
    created_at: Optional[datetime]
    description: Optional[StrictStr]
    events: Optional[List[StrictStr]] = Field(default=None, description="The list of events for the GitHub app")
    external_url: Optional[StrictStr]
    html_url: StrictStr
    id: Optional[StrictInt] = Field(description="Unique identifier of the GitHub app")
    name: StrictStr = Field(description="The name of the GitHub app")
    node_id: StrictStr
    owner: Optional[User2]
    permissions: Optional[AppPermissions] = None
    slug: Optional[StrictStr] = Field(default=None, description="The slug name of the GitHub app")
    updated_at: Optional[datetime]
    __properties: ClassVar[List[str]] = ["created_at", "description", "events", "external_url", "html_url", "id", "name", "node_id", "owner", "permissions", "slug", "updated_at"]

    @field_validator('events')
    def events_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['branch_protection_rule', 'check_run', 'check_suite', 'code_scanning_alert', 'commit_comment', 'content_reference', 'create', 'delete', 'deployment', 'deployment_review', 'deployment_status', 'deploy_key', 'discussion', 'discussion_comment', 'fork', 'gollum', 'issues', 'issue_comment', 'label', 'member', 'membership', 'milestone', 'organization', 'org_block', 'page_build', 'project', 'project_card', 'project_column', 'public', 'pull_request', 'pull_request_review', 'pull_request_review_comment', 'push', 'registry_package', 'release', 'repository', 'repository_dispatch', 'secret_scanning_alert', 'star', 'status', 'team', 'team_add', 'watch', 'workflow_dispatch', 'workflow_run']):
                raise ValueError("each list item must be one of ('branch_protection_rule', 'check_run', 'check_suite', 'code_scanning_alert', 'commit_comment', 'content_reference', 'create', 'delete', 'deployment', 'deployment_review', 'deployment_status', 'deploy_key', 'discussion', 'discussion_comment', 'fork', 'gollum', 'issues', 'issue_comment', 'label', 'member', 'membership', 'milestone', 'organization', 'org_block', 'page_build', 'project', 'project_card', 'project_column', 'public', 'pull_request', 'pull_request_review', 'pull_request_review_comment', 'push', 'registry_package', 'release', 'repository', 'repository_dispatch', 'secret_scanning_alert', 'star', 'status', 'team', 'team_add', 'watch', 'workflow_dispatch', 'workflow_run')")
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
        """Create an instance of App11 from a JSON string"""
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
        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if external_url (nullable) is None
        # and model_fields_set contains the field
        if self.external_url is None and "external_url" in self.model_fields_set:
            _dict['external_url'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of App11 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "events": obj.get("events"),
            "external_url": obj.get("external_url"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "node_id": obj.get("node_id"),
            "owner": User2.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "permissions": AppPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "slug": obj.get("slug"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


