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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrgsCreateInvitationRequest(BaseModel):
    """
    OrgsCreateInvitationRequest
    """ # noqa: E501
    invitee_id: Optional[StrictInt] = Field(default=None, description="**Required unless you provide `email`**. GitHub user ID for the person you are inviting.")
    email: Optional[StrictStr] = Field(default=None, description="**Required unless you provide `invitee_id`**. Email address of the person you are inviting, which can be an existing GitHub user.")
    role: Optional[StrictStr] = Field(default='direct_member', description="The role for the new member.   * `admin` - Organization owners with full administrative rights to the organization and complete access to all repositories and teams.    * `direct_member` - Non-owner organization members with ability to see other members and join teams by invitation.    * `billing_manager` - Non-owner organization members with ability to manage the billing settings of your organization.   * `reinstate` - The previous role assigned to the invitee before they were removed from your organization. Can be one of the roles listed above. Only works if the invitee was previously part of your organization.")
    team_ids: Optional[List[StrictInt]] = Field(default=None, description="Specify IDs for the teams you want to invite new members to.")
    __properties: ClassVar[List[str]] = ["invitee_id", "email", "role", "team_ids"]

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['admin', 'direct_member', 'billing_manager', 'reinstate']):
            raise ValueError("must be one of enum values ('admin', 'direct_member', 'billing_manager', 'reinstate')")
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
        """Create an instance of OrgsCreateInvitationRequest from a JSON string"""
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
        """Create an instance of OrgsCreateInvitationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invitee_id": obj.get("invitee_id"),
            "email": obj.get("email"),
            "role": obj.get("role") if obj.get("role") is not None else 'direct_member',
            "team_ids": obj.get("team_ids")
        })
        return _obj

