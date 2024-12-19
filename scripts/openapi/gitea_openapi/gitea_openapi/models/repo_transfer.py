# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.

    The version of the OpenAPI document: {{AppVer | JSEscape}}
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from gitea_openapi.models.team import Team
from gitea_openapi.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class RepoTransfer(BaseModel):
    """
    RepoTransfer represents a pending repo transfer
    """ # noqa: E501
    doer: Optional[User] = None
    recipient: Optional[User] = None
    teams: Optional[List[Team]] = None
    __properties: ClassVar[List[str]] = ["doer", "recipient", "teams"]

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
        """Create an instance of RepoTransfer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of doer
        if self.doer:
            _dict['doer'] = self.doer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item_teams in self.teams:
                if _item_teams:
                    _items.append(_item_teams.to_dict())
            _dict['teams'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RepoTransfer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "doer": User.from_dict(obj["doer"]) if obj.get("doer") is not None else None,
            "recipient": User.from_dict(obj["recipient"]) if obj.get("recipient") is not None else None,
            "teams": [Team.from_dict(_item) for _item in obj["teams"]] if obj.get("teams") is not None else None
        })
        return _obj


