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
from github_openapi.models.user2 import User2
from typing import Optional, Set
from typing_extensions import Self

class Milestone1(BaseModel):
    """
    A collection of related issues and pull requests.
    """ # noqa: E501
    closed_at: Optional[datetime]
    closed_issues: StrictInt
    created_at: datetime
    creator: Optional[User2]
    description: Optional[StrictStr]
    due_on: Optional[datetime]
    html_url: StrictStr
    id: StrictInt
    labels_url: StrictStr
    node_id: StrictStr
    number: StrictInt = Field(description="The number of the milestone.")
    open_issues: StrictInt
    state: StrictStr = Field(description="The state of the milestone.")
    title: StrictStr = Field(description="The title of the milestone.")
    updated_at: datetime
    url: StrictStr
    __properties: ClassVar[List[str]] = ["closed_at", "closed_issues", "created_at", "creator", "description", "due_on", "html_url", "id", "labels_url", "node_id", "number", "open_issues", "state", "title", "updated_at", "url"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['open', 'closed']):
            raise ValueError("must be one of enum values ('open', 'closed')")
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
        """Create an instance of Milestone1 from a JSON string"""
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
        # set to None if closed_at (nullable) is None
        # and model_fields_set contains the field
        if self.closed_at is None and "closed_at" in self.model_fields_set:
            _dict['closed_at'] = None

        # set to None if creator (nullable) is None
        # and model_fields_set contains the field
        if self.creator is None and "creator" in self.model_fields_set:
            _dict['creator'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if due_on (nullable) is None
        # and model_fields_set contains the field
        if self.due_on is None and "due_on" in self.model_fields_set:
            _dict['due_on'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Milestone1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "closed_at": obj.get("closed_at"),
            "closed_issues": obj.get("closed_issues"),
            "created_at": obj.get("created_at"),
            "creator": User2.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "description": obj.get("description"),
            "due_on": obj.get("due_on"),
            "html_url": obj.get("html_url"),
            "id": obj.get("id"),
            "labels_url": obj.get("labels_url"),
            "node_id": obj.get("node_id"),
            "number": obj.get("number"),
            "open_issues": obj.get("open_issues"),
            "state": obj.get("state"),
            "title": obj.get("title"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url")
        })
        return _obj


