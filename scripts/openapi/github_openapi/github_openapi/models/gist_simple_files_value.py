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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GistSimpleFilesValue(BaseModel):
    """
    GistSimpleFilesValue
    """ # noqa: E501
    filename: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    language: Optional[StrictStr] = None
    raw_url: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    truncated: Optional[StrictBool] = None
    content: Optional[StrictStr] = None
    encoding: Optional[StrictStr] = Field(default='utf-8', description="The encoding used for `content`. Currently, `\"utf-8\"` and `\"base64\"` are supported.")
    __properties: ClassVar[List[str]] = ["filename", "type", "language", "raw_url", "size", "truncated", "content", "encoding"]

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
        """Create an instance of GistSimpleFilesValue from a JSON string"""
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
        """Create an instance of GistSimpleFilesValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filename": obj.get("filename"),
            "type": obj.get("type"),
            "language": obj.get("language"),
            "raw_url": obj.get("raw_url"),
            "size": obj.get("size"),
            "truncated": obj.get("truncated"),
            "content": obj.get("content"),
            "encoding": obj.get("encoding") if obj.get("encoding") is not None else 'utf-8'
        })
        return _obj


