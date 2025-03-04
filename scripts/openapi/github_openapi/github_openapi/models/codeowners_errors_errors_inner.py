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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CodeownersErrorsErrorsInner(BaseModel):
    """
    CodeownersErrorsErrorsInner
    """ # noqa: E501
    line: StrictInt = Field(description="The line number where this errors occurs.")
    column: StrictInt = Field(description="The column number where this errors occurs.")
    source: Optional[StrictStr] = Field(default=None, description="The contents of the line where the error occurs.")
    kind: StrictStr = Field(description="The type of error.")
    suggestion: Optional[StrictStr] = Field(default=None, description="Suggested action to fix the error. This will usually be `null`, but is provided for some common errors.")
    message: StrictStr = Field(description="A human-readable description of the error, combining information from multiple fields, laid out for display in a monospaced typeface (for example, a command-line setting).")
    path: StrictStr = Field(description="The path of the file where the error occured.")
    __properties: ClassVar[List[str]] = ["line", "column", "source", "kind", "suggestion", "message", "path"]

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
        """Create an instance of CodeownersErrorsErrorsInner from a JSON string"""
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
        # set to None if suggestion (nullable) is None
        # and model_fields_set contains the field
        if self.suggestion is None and "suggestion" in self.model_fields_set:
            _dict['suggestion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CodeownersErrorsErrorsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "line": obj.get("line"),
            "column": obj.get("column"),
            "source": obj.get("source"),
            "kind": obj.get("kind"),
            "suggestion": obj.get("suggestion"),
            "message": obj.get("message"),
            "path": obj.get("path")
        })
        return _obj


