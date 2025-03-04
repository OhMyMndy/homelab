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
from github_openapi.models.app_permissions import AppPermissions
from github_openapi.models.installation_account import InstallationAccount
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from typing import Optional, Set
from typing_extensions import Self

class Installation(BaseModel):
    """
    Installation
    """ # noqa: E501
    id: StrictInt = Field(description="The ID of the installation.")
    account: Optional[InstallationAccount]
    repository_selection: StrictStr = Field(description="Describe whether all repositories have been selected or there's a selection involved")
    access_tokens_url: StrictStr
    repositories_url: StrictStr
    html_url: StrictStr
    app_id: StrictInt
    target_id: StrictInt = Field(description="The ID of the user or organization this token is being scoped to.")
    target_type: StrictStr
    permissions: AppPermissions
    events: List[StrictStr]
    created_at: datetime
    updated_at: datetime
    single_file_name: Optional[StrictStr]
    has_multiple_single_files: Optional[StrictBool] = None
    single_file_paths: Optional[List[StrictStr]] = None
    app_slug: StrictStr
    suspended_by: Optional[NullableSimpleUser]
    suspended_at: Optional[datetime]
    contact_email: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "account", "repository_selection", "access_tokens_url", "repositories_url", "html_url", "app_id", "target_id", "target_type", "permissions", "events", "created_at", "updated_at", "single_file_name", "has_multiple_single_files", "single_file_paths", "app_slug", "suspended_by", "suspended_at", "contact_email"]

    @field_validator('repository_selection')
    def repository_selection_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['all', 'selected']):
            raise ValueError("must be one of enum values ('all', 'selected')")
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
        """Create an instance of Installation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of suspended_by
        if self.suspended_by:
            _dict['suspended_by'] = self.suspended_by.to_dict()
        # set to None if account (nullable) is None
        # and model_fields_set contains the field
        if self.account is None and "account" in self.model_fields_set:
            _dict['account'] = None

        # set to None if single_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.single_file_name is None and "single_file_name" in self.model_fields_set:
            _dict['single_file_name'] = None

        # set to None if suspended_by (nullable) is None
        # and model_fields_set contains the field
        if self.suspended_by is None and "suspended_by" in self.model_fields_set:
            _dict['suspended_by'] = None

        # set to None if suspended_at (nullable) is None
        # and model_fields_set contains the field
        if self.suspended_at is None and "suspended_at" in self.model_fields_set:
            _dict['suspended_at'] = None

        # set to None if contact_email (nullable) is None
        # and model_fields_set contains the field
        if self.contact_email is None and "contact_email" in self.model_fields_set:
            _dict['contact_email'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Installation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "account": InstallationAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "repository_selection": obj.get("repository_selection"),
            "access_tokens_url": obj.get("access_tokens_url"),
            "repositories_url": obj.get("repositories_url"),
            "html_url": obj.get("html_url"),
            "app_id": obj.get("app_id"),
            "target_id": obj.get("target_id"),
            "target_type": obj.get("target_type"),
            "permissions": AppPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "events": obj.get("events"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "single_file_name": obj.get("single_file_name"),
            "has_multiple_single_files": obj.get("has_multiple_single_files"),
            "single_file_paths": obj.get("single_file_paths"),
            "app_slug": obj.get("app_slug"),
            "suspended_by": NullableSimpleUser.from_dict(obj["suspended_by"]) if obj.get("suspended_by") is not None else None,
            "suspended_at": obj.get("suspended_at"),
            "contact_email": obj.get("contact_email")
        })
        return _obj


