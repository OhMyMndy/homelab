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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from github_openapi.models.nullable_simple_user import NullableSimpleUser
from typing import Optional, Set
from typing_extensions import Self

class Status(BaseModel):
    """
    The status of a commit.
    """ # noqa: E501
    url: StrictStr
    avatar_url: Optional[StrictStr]
    id: StrictInt
    node_id: StrictStr
    state: StrictStr
    description: Optional[StrictStr]
    target_url: Optional[StrictStr]
    context: StrictStr
    created_at: StrictStr
    updated_at: StrictStr
    creator: Optional[NullableSimpleUser]
    __properties: ClassVar[List[str]] = ["url", "avatar_url", "id", "node_id", "state", "description", "target_url", "context", "created_at", "updated_at", "creator"]

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
        """Create an instance of Status from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # set to None if avatar_url (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_url is None and "avatar_url" in self.model_fields_set:
            _dict['avatar_url'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if target_url (nullable) is None
        # and model_fields_set contains the field
        if self.target_url is None and "target_url" in self.model_fields_set:
            _dict['target_url'] = None

        # set to None if creator (nullable) is None
        # and model_fields_set contains the field
        if self.creator is None and "creator" in self.model_fields_set:
            _dict['creator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Status from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "avatar_url": obj.get("avatar_url"),
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "state": obj.get("state"),
            "description": obj.get("description"),
            "target_url": obj.get("target_url"),
            "context": obj.get("context"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "creator": NullableSimpleUser.from_dict(obj["creator"]) if obj.get("creator") is not None else None
        })
        return _obj


