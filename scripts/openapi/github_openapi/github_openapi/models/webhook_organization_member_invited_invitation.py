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
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from github_openapi.models.user2 import User2
from typing import Optional, Set
from typing_extensions import Self

class WebhookOrganizationMemberInvitedInvitation(BaseModel):
    """
    The invitation for the user or email if the action is `member_invited`.
    """ # noqa: E501
    created_at: datetime
    email: Optional[StrictStr]
    failed_at: Optional[datetime]
    failed_reason: Optional[StrictStr]
    id: Union[StrictFloat, StrictInt]
    invitation_teams_url: StrictStr
    inviter: Optional[User2]
    login: Optional[StrictStr]
    node_id: StrictStr
    role: StrictStr
    team_count: Union[StrictFloat, StrictInt]
    invitation_source: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "email", "failed_at", "failed_reason", "id", "invitation_teams_url", "inviter", "login", "node_id", "role", "team_count", "invitation_source"]

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
        """Create an instance of WebhookOrganizationMemberInvitedInvitation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of inviter
        if self.inviter:
            _dict['inviter'] = self.inviter.to_dict()
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if failed_at (nullable) is None
        # and model_fields_set contains the field
        if self.failed_at is None and "failed_at" in self.model_fields_set:
            _dict['failed_at'] = None

        # set to None if failed_reason (nullable) is None
        # and model_fields_set contains the field
        if self.failed_reason is None and "failed_reason" in self.model_fields_set:
            _dict['failed_reason'] = None

        # set to None if inviter (nullable) is None
        # and model_fields_set contains the field
        if self.inviter is None and "inviter" in self.model_fields_set:
            _dict['inviter'] = None

        # set to None if login (nullable) is None
        # and model_fields_set contains the field
        if self.login is None and "login" in self.model_fields_set:
            _dict['login'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookOrganizationMemberInvitedInvitation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "email": obj.get("email"),
            "failed_at": obj.get("failed_at"),
            "failed_reason": obj.get("failed_reason"),
            "id": obj.get("id"),
            "invitation_teams_url": obj.get("invitation_teams_url"),
            "inviter": User2.from_dict(obj["inviter"]) if obj.get("inviter") is not None else None,
            "login": obj.get("login"),
            "node_id": obj.get("node_id"),
            "role": obj.get("role"),
            "team_count": obj.get("team_count"),
            "invitation_source": obj.get("invitation_source")
        })
        return _obj

