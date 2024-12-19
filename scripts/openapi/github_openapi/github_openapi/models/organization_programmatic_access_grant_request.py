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
from github_openapi.models.organization_programmatic_access_grant_request_permissions import OrganizationProgrammaticAccessGrantRequestPermissions
from github_openapi.models.simple_user import SimpleUser
from typing import Optional, Set
from typing_extensions import Self

class OrganizationProgrammaticAccessGrantRequest(BaseModel):
    """
    Minimal representation of an organization programmatic access grant request for enumerations
    """ # noqa: E501
    id: StrictInt = Field(description="Unique identifier of the request for access via fine-grained personal access token. The `pat_request_id` used to review PAT requests.")
    reason: Optional[StrictStr] = Field(description="Reason for requesting access.")
    owner: SimpleUser
    repository_selection: StrictStr = Field(description="Type of repository selection requested.")
    repositories_url: StrictStr = Field(description="URL to the list of repositories requested to be accessed via fine-grained personal access token. Should only be followed when `repository_selection` is `subset`.")
    permissions: OrganizationProgrammaticAccessGrantRequestPermissions
    created_at: StrictStr = Field(description="Date and time when the request for access was created.")
    token_id: StrictInt = Field(description="Unique identifier of the user's token. This field can also be found in audit log events and the organization's settings for their PAT grants.")
    token_name: StrictStr = Field(description="The name given to the user's token. This field can also be found in an organization's settings page for Active Tokens.")
    token_expired: StrictBool = Field(description="Whether the associated fine-grained personal access token has expired.")
    token_expires_at: Optional[StrictStr] = Field(description="Date and time when the associated fine-grained personal access token expires.")
    token_last_used_at: Optional[StrictStr] = Field(description="Date and time when the associated fine-grained personal access token was last used for authentication.")
    __properties: ClassVar[List[str]] = ["id", "reason", "owner", "repository_selection", "repositories_url", "permissions", "created_at", "token_id", "token_name", "token_expired", "token_expires_at", "token_last_used_at"]

    @field_validator('repository_selection')
    def repository_selection_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['none', 'all', 'subset']):
            raise ValueError("must be one of enum values ('none', 'all', 'subset')")
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
        """Create an instance of OrganizationProgrammaticAccessGrantRequest from a JSON string"""
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
        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if token_expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.token_expires_at is None and "token_expires_at" in self.model_fields_set:
            _dict['token_expires_at'] = None

        # set to None if token_last_used_at (nullable) is None
        # and model_fields_set contains the field
        if self.token_last_used_at is None and "token_last_used_at" in self.model_fields_set:
            _dict['token_last_used_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganizationProgrammaticAccessGrantRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "reason": obj.get("reason"),
            "owner": SimpleUser.from_dict(obj["owner"]) if obj.get("owner") is not None else None,
            "repository_selection": obj.get("repository_selection"),
            "repositories_url": obj.get("repositories_url"),
            "permissions": OrganizationProgrammaticAccessGrantRequestPermissions.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "created_at": obj.get("created_at"),
            "token_id": obj.get("token_id"),
            "token_name": obj.get("token_name"),
            "token_expired": obj.get("token_expired"),
            "token_expires_at": obj.get("token_expires_at"),
            "token_last_used_at": obj.get("token_last_used_at")
        })
        return _obj

