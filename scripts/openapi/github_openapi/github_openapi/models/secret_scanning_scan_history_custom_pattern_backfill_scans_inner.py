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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SecretScanningScanHistoryCustomPatternBackfillScansInner(BaseModel):
    """
    SecretScanningScanHistoryCustomPatternBackfillScansInner
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="The type of scan")
    status: Optional[StrictStr] = Field(default=None, description="The state of the scan. Either \"completed\", \"running\", or \"pending\"")
    completed_at: Optional[datetime] = Field(default=None, description="The time that the scan was completed. Empty if the scan is running")
    started_at: Optional[datetime] = Field(default=None, description="The time that the scan was started. Empty if the scan is pending")
    pattern_name: Optional[StrictStr] = Field(default=None, description="Name of the custom pattern for custom pattern scans")
    pattern_scope: Optional[StrictStr] = Field(default=None, description="Level at which the custom pattern is defined, one of \"repository\", \"organization\", or \"enterprise\"")
    __properties: ClassVar[List[str]] = ["type", "status", "completed_at", "started_at", "pattern_name", "pattern_scope"]

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
        """Create an instance of SecretScanningScanHistoryCustomPatternBackfillScansInner from a JSON string"""
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
        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completed_at'] = None

        # set to None if started_at (nullable) is None
        # and model_fields_set contains the field
        if self.started_at is None and "started_at" in self.model_fields_set:
            _dict['started_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SecretScanningScanHistoryCustomPatternBackfillScansInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "status": obj.get("status"),
            "completed_at": obj.get("completed_at"),
            "started_at": obj.get("started_at"),
            "pattern_name": obj.get("pattern_name"),
            "pattern_scope": obj.get("pattern_scope")
        })
        return _obj


