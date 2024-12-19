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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DiffEntry(BaseModel):
    """
    Diff Entry
    """ # noqa: E501
    sha: StrictStr
    filename: StrictStr
    status: StrictStr
    additions: StrictInt
    deletions: StrictInt
    changes: StrictInt
    blob_url: StrictStr
    raw_url: StrictStr
    contents_url: StrictStr
    patch: Optional[StrictStr] = None
    previous_filename: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["sha", "filename", "status", "additions", "deletions", "changes", "blob_url", "raw_url", "contents_url", "patch", "previous_filename"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['added', 'removed', 'modified', 'renamed', 'copied', 'changed', 'unchanged']):
            raise ValueError("must be one of enum values ('added', 'removed', 'modified', 'renamed', 'copied', 'changed', 'unchanged')")
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
        """Create an instance of DiffEntry from a JSON string"""
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
        """Create an instance of DiffEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sha": obj.get("sha"),
            "filename": obj.get("filename"),
            "status": obj.get("status"),
            "additions": obj.get("additions"),
            "deletions": obj.get("deletions"),
            "changes": obj.get("changes"),
            "blob_url": obj.get("blob_url"),
            "raw_url": obj.get("raw_url"),
            "contents_url": obj.get("contents_url"),
            "patch": obj.get("patch"),
            "previous_filename": obj.get("previous_filename")
        })
        return _obj


