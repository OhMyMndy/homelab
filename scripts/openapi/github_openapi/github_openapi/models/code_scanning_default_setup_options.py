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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CodeScanningDefaultSetupOptions(BaseModel):
    """
    Feature options for code scanning default setup
    """ # noqa: E501
    runner_type: Optional[StrictStr] = Field(default=None, description="Whether to use labeled runners or standard GitHub runners.")
    runner_label: Optional[StrictStr] = Field(default=None, description="The label of the runner to use for code scanning default setup when runner_type is 'labeled'.")
    __properties: ClassVar[List[str]] = ["runner_type", "runner_label"]

    @field_validator('runner_type')
    def runner_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['standard', 'labeled', 'not_set']):
            raise ValueError("must be one of enum values ('standard', 'labeled', 'not_set')")
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
        """Create an instance of CodeScanningDefaultSetupOptions from a JSON string"""
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
        # set to None if runner_label (nullable) is None
        # and model_fields_set contains the field
        if self.runner_label is None and "runner_label" in self.model_fields_set:
            _dict['runner_label'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CodeScanningDefaultSetupOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "runner_type": obj.get("runner_type"),
            "runner_label": obj.get("runner_label")
        })
        return _obj


