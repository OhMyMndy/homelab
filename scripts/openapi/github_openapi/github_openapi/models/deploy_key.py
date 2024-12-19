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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DeployKey(BaseModel):
    """
    An SSH key granting access to a single repository.
    """ # noqa: E501
    id: StrictInt
    key: StrictStr
    url: StrictStr
    title: StrictStr
    verified: StrictBool
    created_at: StrictStr
    read_only: StrictBool
    added_by: Optional[StrictStr] = None
    last_used: Optional[StrictStr] = None
    enabled: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "key", "url", "title", "verified", "created_at", "read_only", "added_by", "last_used", "enabled"]

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
        """Create an instance of DeployKey from a JSON string"""
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
        # set to None if added_by (nullable) is None
        # and model_fields_set contains the field
        if self.added_by is None and "added_by" in self.model_fields_set:
            _dict['added_by'] = None

        # set to None if last_used (nullable) is None
        # and model_fields_set contains the field
        if self.last_used is None and "last_used" in self.model_fields_set:
            _dict['last_used'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeployKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "key": obj.get("key"),
            "url": obj.get("url"),
            "title": obj.get("title"),
            "verified": obj.get("verified"),
            "created_at": obj.get("created_at"),
            "read_only": obj.get("read_only"),
            "added_by": obj.get("added_by"),
            "last_used": obj.get("last_used"),
            "enabled": obj.get("enabled")
        })
        return _obj


