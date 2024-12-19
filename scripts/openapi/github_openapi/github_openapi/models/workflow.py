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
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Workflow(BaseModel):
    """
    A GitHub Actions workflow
    """ # noqa: E501
    id: StrictInt
    node_id: StrictStr
    name: StrictStr
    path: StrictStr
    state: StrictStr
    created_at: datetime
    updated_at: datetime
    url: StrictStr
    html_url: StrictStr
    badge_url: StrictStr
    deleted_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "node_id", "name", "path", "state", "created_at", "updated_at", "url", "html_url", "badge_url", "deleted_at"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['active', 'deleted', 'disabled_fork', 'disabled_inactivity', 'disabled_manually']):
            raise ValueError("must be one of enum values ('active', 'deleted', 'disabled_fork', 'disabled_inactivity', 'disabled_manually')")
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
        """Create an instance of Workflow from a JSON string"""
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
        """Create an instance of Workflow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "node_id": obj.get("node_id"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "state": obj.get("state"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "html_url": obj.get("html_url"),
            "badge_url": obj.get("badge_url"),
            "deleted_at": obj.get("deleted_at")
        })
        return _obj

