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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from github_openapi.models.org_membership_permissions import OrgMembershipPermissions
from github_openapi.models.organization_simple import OrganizationSimple
from typing import Optional, Set
from typing_extensions import Self

class OrgMembership(BaseModel):
    """
    Org Membership
    """ # noqa: E501
    url: StrictStr
    state: StrictStr = Field(description="The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation.")
    role: StrictStr = Field(description="The user's membership type in the organization.")
    organization_url: StrictStr
    organization: OrganizationSimple
    user: Optional[NullableSimpleUser]
    permissions: Optional[OrgMembershipPermissions] = None
    __properties: ClassVar[List[str]] = ["url", "state", "role", "organization_url", "organization", "user", "permissions"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['active', 'pending']):
            raise ValueError("must be one of enum values ('active', 'pending')")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['admin', 'member', 'billing_manager']):
            raise ValueError("must be one of enum values ('admin', 'member', 'billing_manager')")
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
        """Create an instance of OrgMembership from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrgMembership from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "state": obj.get("state"),
            "role": obj.get("role"),
            "organization_url": obj.get("organization_url"),
            "organization": OrganizationSimple.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "user": NullableSimpleUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "permissions": OrgMembershipPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None
        })
        return _obj


