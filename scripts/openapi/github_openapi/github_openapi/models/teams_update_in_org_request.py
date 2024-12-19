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

class TeamsUpdateInOrgRequest(BaseModel):
    """
    TeamsUpdateInOrgRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the team.")
    description: Optional[StrictStr] = Field(default=None, description="The description of the team.")
    privacy: Optional[StrictStr] = Field(default=None, description="The level of privacy this team should have. Editing teams without specifying this parameter leaves `privacy` intact. When a team is nested, the `privacy` for parent teams cannot be `secret`. The options are:   **For a non-nested team:**    * `secret` - only visible to organization owners and members of this team.    * `closed` - visible to all members of this organization.   **For a parent or child team:**    * `closed` - visible to all members of this organization.")
    notification_setting: Optional[StrictStr] = Field(default=None, description="The notification setting the team has chosen. Editing teams without specifying this parameter leaves `notification_setting` intact. The options are:   * `notifications_enabled` - team members receive notifications when the team is @mentioned.    * `notifications_disabled` - no one receives notifications.")
    permission: Optional[StrictStr] = Field(default='pull', description="**Closing down notice**. The permission that new repositories will be added to the team with when none is specified.")
    parent_team_id: Optional[StrictInt] = Field(default=None, description="The ID of a team to set as the parent team.")
    __properties: ClassVar[List[str]] = ["name", "description", "privacy", "notification_setting", "permission", "parent_team_id"]

    @field_validator('privacy')
    def privacy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['secret', 'closed']):
            raise ValueError("must be one of enum values ('secret', 'closed')")
        return value

    @field_validator('notification_setting')
    def notification_setting_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['notifications_enabled', 'notifications_disabled']):
            raise ValueError("must be one of enum values ('notifications_enabled', 'notifications_disabled')")
        return value

    @field_validator('permission')
    def permission_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pull', 'push', 'admin']):
            raise ValueError("must be one of enum values ('pull', 'push', 'admin')")
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
        """Create an instance of TeamsUpdateInOrgRequest from a JSON string"""
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
        # set to None if parent_team_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_team_id is None and "parent_team_id" in self.model_fields_set:
            _dict['parent_team_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TeamsUpdateInOrgRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "privacy": obj.get("privacy"),
            "notification_setting": obj.get("notification_setting"),
            "permission": obj.get("permission") if obj.get("permission") is not None else 'pull',
            "parent_team_id": obj.get("parent_team_id")
        })
        return _obj


